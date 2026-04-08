# CryptoAlertBot

**Real-time cryptocurrency price monitoring with Telegram notifications**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-green.svg)](https://www.python.org)
[![Platform: Windows](https://img.shields.io/badge/Platform-Windows-blue.svg)](https://www.microsoft.com/windows)
[![GitHub Release](https://img.shields.io/badge/Release-v1.0.0-blue.svg)](https://github.com/lingyRTX/Crypto-Alert-Bot/releases)

---

## Quick Links

| Link | Description |
|------|-------------|
| [Download EXE](https://github.com/lingyRTX/Crypto-Alert-Bot/releases) | Download latest release |
| [Telegram Channel](https://t.me/toolsforcrypto) | New tools and updates |
| [Report Bug](https://t.me/lingytm) | Contact for bug reports |
| [Installation Guide](INSTALL.md) | Step-by-step setup |
| [License](LICENSE) | MIT License |

---

## Table of Contents

- [Features](#features)
- [Quick Start](#quick-start)
- [Setup Guide](#setup-guide)
- [System Requirements](#system-requirements)
- [Technology Stack](#technology-stack)
- [Security](#security)
- [FAQ](#faq)
- [Support](#support)

---

## Features

► Monitor 40,000+ cryptocurrencies from CoinGecko API  
► Set price alerts for any cryptocurrency  
► Receive instant Telegram notifications  
► Customizable check intervals (1-60 minutes)  
► Light and dark themes  
► Professional Windows application  
► Local storage - no cloud sync  
► Free and open source  

---

## Quick Start

### Option 1: Download EXE (Easiest)

1. [Download from Releases](https://github.com/lingyRTX/Crypto-Alert-Bot/releases)
2. Run CryptoAlertBot.exe
3. Configure Telegram (see Setup Guide below)
4. Create your first alert

### Option 2: Build from Source

```bash
git clone https://github.com/lingyRTX/Crypto-Alert-Bot.git
cd CryptoAlertBot
pip install -r requirements.txt
python main.py
```

Build your own EXE:
```bash
python build_exe.py
```

---

## Setup Guide

### Step 1: Create Telegram Bot

1. Search for [@BotFather](https://t.me/BotFather) in Telegram
2. Send `/newbot` command
3. Follow instructions to create bot
4. **Copy your Bot Token**

### Step 2: Get Your Chat ID

1. Search for [@userinfobot](https://t.me/userinfobot) in Telegram
2. Click Start
3. **Copy your numeric Chat ID**

### Step 3: Configure Application

1. Launch CryptoAlertBot
2. Go to **Settings** tab
3. Paste Bot Token and Chat ID
4. Click **Test Connection**
5. Verify test message received

### Step 4: Create First Alert

1. Go to **Price Alerts** tab
2. Select cryptocurrency (e.g., Bitcoin)
3. Enter target price (e.g., 45000)
4. Choose condition: **rises above** or **falls below**
5. Click **Add Alert**

---

## Usage

### Price Alerts Tab

■ **Cryptocurrency** - Choose from 40,000+ coins  
■ **Target Price** - Price in USD  
■ **Condition** - When to send notification  
■ **Current Price** - Real-time price display  
■ **Status** - Active or triggered status  

### Settings Tab

■ **Bot Token** - Telegram bot authentication  
■ **Chat ID** - Your Telegram user ID  
■ **Check Interval** - Frequency in minutes (1-60)  

### Activity Log Tab

View all notifications and application events.

---

## System Requirements

▸ **OS:** Windows 7 or newer (64-bit)  
▸ **Internet:** Active connection required  
▸ **Telegram:** Account needed for notifications  
▸ **Disk Space:** ~50 MB for application  

No additional software installation needed.

---

## Technology Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.8+ |
| UI Framework | PyQt5 |
| Price Data | CoinGecko API |
| Notifications | Telegram Bot API |
| Packaging | PyInstaller |
| Version Control | Git |

---

## Project Structure

```
CryptoAlertBot/
├── main.py                      Application entry point
├── build_exe.py                 EXE build script
├── requirements.txt             Dependencies
├── config.json                  Configuration template
├── frontend/                    UI Layer
│   ├── main_window.py          Main application window
│   ├── light_styles.py         Light theme stylesheet
│   └── dark_styles.py          Dark theme stylesheet
└── backend/                     Business Logic
    ├── api/                    External APIs
    │   └── coingecko.py        Price data client
    ├── telegram/               Notifications
    │   └── bot.py             Telegram integration
    ├── checker/                Monitoring service
    │   └── price_checker.py   Price monitoring loop
    ├── models/                 Data structures
    ├── services/               Service orchestration
    ├── storage/                Configuration storage
    └── data/                   Cryptocurrency database
```

---

## Security

**Local Storage Only**  
All configuration stored in config.json on your computer. No cloud servers, no data tracking.

**Open Source**  
Full source code visible for transparency. No hidden processes. Licensed under MIT.

**No Permissions Needed**  
Only reads public price data from CoinGecko. Only sends messages to your Telegram.

---

## Building Your Own EXE

```bash
python build_exe.py
```

Output: `dist/CryptoAlertBot.exe` (approximately 45 MB)

---

## FAQ

**Q: Is CryptoAlertBot free?**  
A: Yes, completely free and open source. No ads or premium features.

**Q: Will my Telegram receive spam?**  
A: No. The bot only sends alerts to your Chat ID that you configured.

**Q: How accurate are the prices?**  
A: Prices come from CoinGecko API. Updates every 1-60 minutes as configured.

**Q: Can I use on Mac or Linux?**  
A: Currently Windows only. Mac/Linux support in future versions.

**Q: What if I lose my token?**  
A: Create a new bot with @BotFather. There's no limit on bot creation.

**Q: Can I set multiple alerts for one coin?**  
A: Yes. You can create multiple alerts with different price targets.

**Q: How often does it check prices?**  
A: Configurable from 1 to 60 minutes. Default is 5 minutes.

---

## Support

**Report Bugs:** [Contact @lingytm on Telegram](https://t.me/lingytm)

**Follow for Updates:** [Subscribe to Tools for Crypto](https://t.me/toolsforcrypto)

**GitHub Issues:** [Create an issue](https://github.com/lingyRTX/Crypto-Alert-Bot/issues)

---

## Contributing

Found a bug? Have a feature request?

1. [Read Contributing Guide](CONTRIBUTING.md)
2. [Contact @lingytm](https://t.me/lingytm)
3. Fork the repository
4. Create a feature branch
5. Submit a pull request

---

## License

This project is licensed under the MIT License.  
See [LICENSE](LICENSE) file for full details.

---

## Disclaimer

CryptoAlertBot is a price monitoring tool only. It does not:
- Provide investment advice
- Make trading decisions  
- Manage cryptocurrency funds
- Guarantee price accuracy

**Use at your own risk.** Always conduct your own research before making financial decisions.

Cryptocurrency markets are highly volatile. Prices can change rapidly and without warning.

---

## Changelog

**v1.0.0** (Initial Release)
- Real-time price monitoring for 40,000+ cryptocurrencies
- Telegram notifications
- Professional Windows desktop application
- Light and dark themes
- Local configuration storage

---

*Created by [lingytm](https://t.me/lingytm)*

Last Updated: April 2025
