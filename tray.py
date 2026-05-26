from PyQt6.QtWidgets import QSystemTrayIcon, QMenu
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import QApplication
import database


class TrayIcon(QSystemTrayIcon):
    def __init__(self, monitor, window, icon_path):
        super().__init__(QIcon(icon_path))
        self._monitor = monitor
        self._window = window
        self.setToolTip("CopyClip")
        self.activated.connect(self._on_activated)
        self._build_menu()

    def _on_activated(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            self._build_menu()
            self.contextMenu().popup(self.geometry().bottomLeft())

    def _build_menu(self):
        menu = QMenu()
        clips = database.get_clips()

        if not clips:
            action = menu.addAction("No clips yet")
            action.setEnabled(False)
        else:
            for _, text, _ in clips:
                display = text[:50] + "..." if len(text) > 50 else text
                display = display.replace("\n", " ")
                action = menu.addAction(display)
                action.setData(text)
                action.triggered.connect(lambda checked, t=text: self._copy(t))

        menu.addSeparator()
        open_action = menu.addAction("Open CopyClip")
        open_action.triggered.connect(self._window.show_window)
        quit_action = menu.addAction("Quit")
        quit_action.triggered.connect(QApplication.quit)

        self.setContextMenu(menu)

    def _copy(self, text: str):
        self._monitor.set_enabled(False)
        QApplication.clipboard().setText(text)
        self._monitor.set_enabled(True)
