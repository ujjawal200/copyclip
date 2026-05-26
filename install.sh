#!/bin/bash
set -e

INSTALL_DIR="$HOME/.local/share/copyclip"
BIN_DIR="$HOME/.local/bin"
ICON_DIR="$HOME/.local/share/icons"
DESKTOP_DIR="$HOME/.local/share/applications"
AUTOSTART_DIR="$HOME/.config/autostart"

echo "📋 Installing CopyClip..."

# Install system dependency
if ! command -v xclip &> /dev/null; then
    echo "Installing xclip..."
    sudo apt install -y xclip
fi

# Install Python dependency
pip install PyQt6 --index-url https://pypi.org/simple/ --user -q 2>/dev/null || pip install PyQt6 --user -q

# Create directories
mkdir -p "$INSTALL_DIR" "$BIN_DIR" "$ICON_DIR" "$DESKTOP_DIR" "$AUTOSTART_DIR"

# Copy app files
cp main.py clipboard_monitor.py database.py tray.py window.py "$INSTALL_DIR/"
cp -r resources "$INSTALL_DIR/"

# Create launcher script
cat > "$BIN_DIR/copyclip" << 'EOF'
#!/bin/bash
cd "$HOME/.local/share/copyclip"
exec python3 main.py
EOF
chmod +x "$BIN_DIR/copyclip"

# Install icon
cp resources/icon-512.png "$ICON_DIR/copyclip.png"

# Install desktop entry (app launcher)
sed "s|Icon=copyclip|Icon=$ICON_DIR/copyclip.png|" copyclip.desktop > "$DESKTOP_DIR/copyclip.desktop"

# Install autostart entry (run on login)
sed "s|Icon=copyclip|Icon=$ICON_DIR/copyclip.png|" copyclip.desktop > "$AUTOSTART_DIR/copyclip.desktop"

# Ensure ~/.local/bin is in PATH
if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.bashrc"
    echo "Added ~/.local/bin to PATH (restart terminal or run: source ~/.bashrc)"
fi

echo ""
echo "✅ CopyClip installed!"
echo ""
echo "  • Launch from app menu or run: copyclip"
echo "  • Starts automatically on login"
echo "  • To uninstall: ~/.local/share/copyclip/uninstall.sh"
