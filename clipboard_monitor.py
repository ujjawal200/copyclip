from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QObject, pyqtSignal


class ClipboardMonitor(QObject):
    new_clip = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self._enabled = True
        self._last_text = ""
        clipboard = QApplication.clipboard()
        clipboard.dataChanged.connect(self._on_change)

    def _on_change(self):
        if not self._enabled:
            return
        clipboard = QApplication.clipboard()
        text = clipboard.text()
        if text and text != self._last_text:
            self._last_text = text
            self.new_clip.emit(text)

    def set_enabled(self, enabled: bool):
        self._enabled = enabled

    def is_enabled(self) -> bool:
        return self._enabled
