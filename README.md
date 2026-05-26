![CopyClip Banner](resources/banner.png)

# CopyClip

A lightweight clipboard history manager for Linux. Lives in your system tray — click to access your last 20 copied texts instantly.

Built for developers and coders who copy-paste frequently.

## Features

- 🔄 Monitors clipboard in real-time (polls every 500ms)
- 📋 Stores last 20 copied texts
- 🖱️ System tray icon — click to see history & re-copy
- 🖥️ Full app window with ON/OFF toggle
- 🗑️ Clear history with one click
- 💾 Persists across restarts (SQLite)
- 🐧 GNOME compatible (uses xclip for reliable clipboard access)
- 🚀 Starts automatically on login

## Screenshots

### Tray Dropdown
![tray](screenshots/tray-dropdown.png)

### App Window
![window](screenshots/app-window.png)

### Full Screen
![fullscreen](screenshots/app-fullscreen.png)

## Installation

### Option 1: .deb package (recommended)

```bash
wget https://github.com/ujjawal200/copyclip/raw/main/copyclip_1.0_all.deb
sudo dpkg -i copyclip_1.0_all.deb
sudo apt install -f
```

### Option 2: Install script

```bash
git clone https://github.com/ujjawal200/copyclip.git
cd copyclip
bash install.sh
```

### Option 3: Run manually

```bash
git clone https://github.com/ujjawal200/copyclip.git
cd copyclip
pip install -r requirements.txt
python main.py
```

## Usage

1. After install, CopyClip starts automatically on login
2. Copy text anywhere — CopyClip saves it automatically
3. Click the tray icon — see your last 20 clips, click any to re-copy
4. Right-click tray → "Open CopyClip" for the full app window
5. Toggle ON/OFF to pause/resume monitoring

## Uninstall

```bash
# If installed via .deb:
sudo apt remove copyclip

# If installed via install.sh:
bash ~/.local/share/copyclip/uninstall.sh
```

## Tech Stack

- **Language**: Python 3
- **UI**: PyQt6 (system tray + window)
- **Clipboard**: xclip (reliable on GNOME/KDE/XFCE)
- **Storage**: SQLite (~/.copyclip/history.db)

## Requirements

- Linux (Ubuntu, Fedora, Arch, etc.)
- Python 3.10+
- xclip
- System tray support

## Project Structure

```
copyclip/
├── main.py              # Entry point
├── clipboard_monitor.py # Polls clipboard via xclip
├── database.py          # SQLite storage (20 item limit)
├── tray.py              # System tray icon + dropdown menu
├── window.py            # Full app window (toggle, list, clear)
├── resources/icon.png   # Tray icon
├── install.sh           # One-command installer
├── uninstall.sh         # Clean removal
└── copyclip_1.0_all.deb # Debian package
```

## License

MIT
