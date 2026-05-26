from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QObject, QTimer, pyqtSignal
import subprocess


class ClipboardMonitor(QObject):
    new_clip = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self._enabled = True
        self._last_text = self._read_clipboard()
        # Poll clipboard every 500ms
        self._timer = QTimer()
        self._timer.timeout.connect(self._check_clipboard)
        self._timer.start(500)

    def _read_clipboard(self) -> str:
        try:
            result = subprocess.run(
                ["xclip", "-selection", "clipboard", "-o"],
                capture_output=True, text=True, timeout=1
            )
            return result.stdout if result.returncode == 0 else ""
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return QApplication.clipboard().text() or ""

    def _check_clipboard(self):
        if not self._enabled:
            return
        text = self._read_clipboard()
        if text and text != self._last_text:
            self._last_text = text
            self.new_clip.emit(text)

    def set_enabled(self, enabled: bool):
        self._enabled = enabled

    def is_enabled(self) -> bool:
        return self._enabled
