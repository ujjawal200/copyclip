# CopyClip

A lightweight clipboard history manager for Linux. Lives in your system tray — click to access your last 20 copied texts instantly.

Built for developers and coders who copy-paste frequently.

## Features

- 🔄 Monitors clipboard in real-time
- 📋 Stores last 20 copied texts
- 🖱️ System tray icon — click to see history
- 📌 Click any item to re-copy it
- ⏸️ Toggle ON/OFF from the app window
- 🗑️ Clear history with one click
- 💾 Persists across restarts (SQLite)

## Installation

```bash
# Clone
git clone https://github.com/ujjawal200/copyclip.git
cd copyclip

# Install dependencies
pip install -r requirements.txt

# Run
python main.py
```

## Usage

1. Run `python main.py` — a clipboard icon appears in your system tray
2. Copy text anywhere — CopyClip saves it automatically
3. Click the tray icon — see your last 20 clips
4. Click any clip — it's copied back to your clipboard
5. Right-click tray → "Open CopyClip" for the full window

## Tech Stack

- Python 3
- PyQt6 (UI + clipboard monitoring)
- SQLite (local storage)

## Requirements

- Linux (GNOME, KDE, XFCE, etc.)
- Python 3.10+
- System tray support

## License

MIT
