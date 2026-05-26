# Contributing to CopyClip

  Thanks for your interest in contributing! Contributions of all sizes are welcome.

  ## Getting Started

  1. Fork and clone:
     ```bash
     git clone https://github.com/<your-username>/copyclip.git
     cd copyclip

  2. Install dependencies:

     sudo apt install xclip
     pip install -r requirements.txt

  3. Run:

     python main.py

  How to Contribute

  Reporting Bugs

  - Open an issue with your Linux distro, desktop environment, and Python version
  - Include steps to reproduce

  Suggesting Features

  - Open an issue with the enhancement label

  Submitting Code

  1. Create a branch: git checkout -b feat/your-feature
  2. Make focused, atomic commits
  3. Test manually — tray, window, clipboard monitoring
  4. Open a Pull Request

  Code Style

  - Python 3.10+
  - Follow existing patterns
  - One module per responsibility

  Project Structure

  ┌──────────────────────┬──────────────────────────────┐
  │ File                 │ Purpose                      │
  ├──────────────────────┼──────────────────────────────┤
  │ main.py              │ Entry point                  │
  ├──────────────────────┼──────────────────────────────┤
  │ clipboard_monitor.py │ Polls xclip for changes      │
  ├──────────────────────┼──────────────────────────────┤
  │ database.py          │ SQLite storage (20 item cap) │
  ├──────────────────────┼──────────────────────────────┤
  │ tray.py              │ System tray + dropdown       │
  ├──────────────────────┼──────────────────────────────┤
  │ window.py            │ App window UI                │
  └──────────────────────┴──────────────────────────────┘

  Ideas for Contributions

  - Search/filter in history
  - Global keyboard shortcut
  - Pin favorite clips
  - Wayland support (wl-clipboard)
  - Image clipboard support
  - Unit tests

  License

  By contributing, you agree your work is licensed under the MIT License.
