#!/bin/bash
echo "Removing CopyClip..."
rm -rf "$HOME/.local/share/copyclip"
rm -f "$HOME/.local/bin/copyclip"
rm -f "$HOME/.local/share/icons/copyclip.png"
rm -f "$HOME/.local/share/applications/copyclip.desktop"
rm -f "$HOME/.config/autostart/copyclip.desktop"
echo "✅ CopyClip uninstalled."
