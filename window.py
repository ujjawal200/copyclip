from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QListWidget, QListWidgetItem, QPushButton, QLabel, QToggleButton
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication
import database


class MainWindow(QMainWindow):
    def __init__(self, monitor):
        super().__init__()
        self._monitor = monitor
        self.setWindowTitle("CopyClip")
        self.setFixedSize(400, 500)
        self._init_ui()

    def _init_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)

        # Header
        header = QHBoxLayout()
        title = QLabel("CopyClip")
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        header.addWidget(title)
        header.addStretch()

        # Toggle button
        self._toggle_btn = QPushButton("ON")
        self._toggle_btn.setCheckable(True)
        self._toggle_btn.setChecked(True)
        self._toggle_btn.setFixedSize(60, 30)
        self._toggle_btn.setStyleSheet(self._toggle_style(True))
        self._toggle_btn.clicked.connect(self._on_toggle)
        header.addWidget(self._toggle_btn)
        layout.addLayout(header)

        # Status
        self._status = QLabel("Monitoring clipboard...")
        self._status.setStyleSheet("color: #4CAF50; font-size: 12px;")
        layout.addWidget(self._status)

        # Clip list
        self._list = QListWidget()
        self._list.setStyleSheet(
            "QListWidget { border: 1px solid #ddd; border-radius: 8px; }"
            "QListWidget::item { padding: 8px; border-bottom: 1px solid #eee; }"
            "QListWidget::item:hover { background: #f0f0f0; }"
        )
        self._list.itemClicked.connect(self._on_item_click)
        layout.addWidget(self._list)

        # Clear button
        clear_btn = QPushButton("Clear All")
        clear_btn.setStyleSheet(
            "QPushButton { background: #f44336; color: white; border: none; "
            "border-radius: 6px; padding: 8px; font-weight: bold; }"
            "QPushButton:hover { background: #d32f2f; }"
        )
        clear_btn.clicked.connect(self._on_clear)
        layout.addWidget(clear_btn)

    def _toggle_style(self, on: bool) -> str:
        bg = "#4CAF50" if on else "#ccc"
        return (
            f"QPushButton {{ background: {bg}; color: white; border: none; "
            f"border-radius: 15px; font-weight: bold; }}"
        )

    def _on_toggle(self):
        enabled = self._toggle_btn.isChecked()
        self._monitor.set_enabled(enabled)
        self._toggle_btn.setText("ON" if enabled else "OFF")
        self._toggle_btn.setStyleSheet(self._toggle_style(enabled))
        self._status.setText(
            "Monitoring clipboard..." if enabled else "Paused"
        )
        self._status.setStyleSheet(
            f"color: {'#4CAF50' if enabled else '#999'}; font-size: 12px;"
        )

    def _on_item_click(self, item: QListWidgetItem):
        text = item.data(Qt.ItemDataRole.UserRole)
        if text:
            self._monitor.set_enabled(False)
            QApplication.clipboard().setText(text)
            self._monitor.set_enabled(True)
            self._status.setText("Copied!")
            from PyQt6.QtCore import QTimer
            QTimer.singleShot(1500, lambda: self._status.setText("Monitoring clipboard..."))

    def _on_clear(self):
        database.clear_all()
        self.refresh_list()

    def refresh_list(self):
        self._list.clear()
        for _, text, timestamp in database.get_clips():
            display = text[:80] + "..." if len(text) > 80 else text
            display = display.replace("\n", " ")
            item = QListWidgetItem(display)
            item.setData(Qt.ItemDataRole.UserRole, text)
            item.setToolTip(text)
            self._list.addItem(item)

    def show_window(self):
        self.refresh_list()
        self.show()
        self.raise_()
        self.activateWindow()

    def closeEvent(self, event):
        event.ignore()
        self.hide()
