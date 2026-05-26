import sys
import os
from PyQt6.QtWidgets import QApplication
from clipboard_monitor import ClipboardMonitor
from tray import TrayIcon
from window import MainWindow
import database


def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    app.setApplicationName("CopyClip")

    icon_path = os.path.join(os.path.dirname(__file__), "resources", "icon.png")

    monitor = ClipboardMonitor()
    window = MainWindow(monitor)
    tray = TrayIcon(monitor, window, icon_path)

    def on_new_clip(text):
        database.add_clip(text)
        window.refresh_list()
        tray.refresh()

    monitor.new_clip.connect(on_new_clip)
    tray.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
