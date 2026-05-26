from PyQt6.QtWidgets import QSystemTrayIcon, QMenu, QApplication
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QTimer
import database
import subprocess


class TrayIcon(QSystemTrayIcon):
    def __init__(self, monitor, window, icon_path):
        super().__init__(QIcon(icon_path))
        self._monitor = monitor
        self._window = window
        self._menu = QMenu()
        self._menu.triggered.connect(self._on_menu_action)
        self._menu.aboutToShow.connect(self._refresh_menu)
        self.setContextMenu(self._menu)
        self.setToolTip("CopyClip")
        self.activated.connect(self._on_activated)
        self._refresh_menu()

    def _on_activated(self, reason):
        self._refresh_menu()

    def refresh(self):
        self._refresh_menu()

    def _refresh_menu(self):
        self._menu.clear()
        clips = database.get_clips()

        if not clips:
            action = self._menu.addAction("No clips yet")
            action.setEnabled(False)
        else:
            for _, text, _ in clips:
                display = text[:50] + "..." if len(text) > 50 else text
                display = display.replace("\n", " ")
                action = self._menu.addAction(display)
                action.setData(text)

        self._menu.addSeparator()
        open_action = self._menu.addAction("Open CopyClip")
        open_action.setData("__open__")
        quit_action = self._menu.addAction("Quit")
        quit_action.setData("__quit__")

    def _on_menu_action(self, action):
        data = action.data()
        if data == "__open__":
            self._window.show_window()
        elif data == "__quit__":
            QApplication.quit()
        elif data:
            self._copy(data)

    def _copy(self, text: str):
        self._monitor.set_enabled(False)
        # Use xclip to set clipboard - works reliably on GNOME without needing a visible window
        try:
            process = subprocess.Popen(
                ["xclip", "-selection", "clipboard"],
                stdin=subprocess.PIPE
            )
            process.communicate(text.encode("utf-8"))
        except FileNotFoundError:
            # Fallback to xsel
            try:
                process = subprocess.Popen(
                    ["xsel", "--clipboard", "--input"],
                    stdin=subprocess.PIPE
                )
                process.communicate(text.encode("utf-8"))
            except FileNotFoundError:
                # Last fallback - Qt clipboard
                QApplication.clipboard().setText(text)
        # Update Qt clipboard to stay in sync
        QTimer.singleShot(100, lambda: self._monitor.set_enabled(True))
