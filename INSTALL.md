# Installation Guide

## Option 1: Download EXE (Recommended)

1. Go to Releases page
2. Download the latest CryptoAlertBot.exe
3. Run the executable
4. No installation required

## Option 2: Build from Source

### Requirements

- Python 3.8 or newer
- Windows 7 or newer

### Steps

1. Clone the repository:
```bash
git clone https://github.com/lingytm/CryptoAlertBot.git
cd CryptoAlertBot
```

2. Create virtual environment (optional):
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python main.py
```

5. Build your own EXE (optional):
```bash
python build_exe.py
```

The EXE will be created in the dist/ folder.

## Troubleshooting

**Issue: "No module named PyQt5"**
- Run: pip install -r requirements.txt

**Issue: EXE won't start**
- Make sure you have Python 3.8+ installed
- Try running from source first with: python main.py

**Issue: Can't find Telegram settings**
- Check Settings tab in the application
- Follow Setup Guide in README.md
