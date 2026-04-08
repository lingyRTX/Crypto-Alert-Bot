# CryptoAlertBot

Real-time cryptocurrency price monitoring with Telegram notifications.

## About

CryptoAlertBot is a lightweight Windows application that monitors cryptocurrency prices and sends Telegram notifications when prices reach your target levels. Monitor any of 40,000+ cryptocurrencies with customizable check intervals.

## Telegram Contacts

- Telegram Channel for new tools: https://t.me/toolsforcrypto
- Report bugs and feature requests: https://t.me/lingytm

## Features

- Monitor 40,000+ cryptocurrencies from CoinGecko API
- Set alerts for price thresholds (rises above or falls below)
- Receive Telegram notifications instantly
- Customizable check intervals (1-60 minutes)
- Professional Windows desktop application
- Light and dark themes available
- All data stored locally, no cloud sync
- Free and open source

## Quick Start

### Using Pre-built EXE

1. Download CryptoAlertBot.exe from the Releases page
2. Run the executable
3. Configure Telegram settings (see Setup section below)
4. Create your first price alert

### Building from Source

```bash
git clone https://github.com/lingytm/CryptoAlertBot.git
cd CryptoAlertBot
pip install -r requirements.txt
python main.py
```

To build your own EXE:
```bash
python build_exe.py
```

## Setup Guide

### Step 1: Create Telegram Bot

1. Open Telegram and search for @BotFather
2. Send /newbot command
3. Follow the instructions to create a bot
4. Copy the Bot Token

### Step 2: Get Your Chat ID

1. Search for @userinfobot in Telegram
2. Click Start
3. The bot will send you your numeric Chat ID

### Step 3: Configure the Application

1. Launch CryptoAlertBot
2. Go to Settings tab
3. Enter your Bot Token and Chat ID
4. Click "Test Connection" to verify
5. Save settings

### Step 4: Create an Alert

1. Go to Price Alerts tab
2. Select a cryptocurrency
3. Enter target price in USD
4. Choose condition (rises above or falls below)
5. Click "Add Alert"

## Usage

### Price Alerts Tab

Create and manage price alerts. View current prices and alert status.

- Cryptocurrency: Select from 40,000+ coins
- Target Price: Price in USD
- Condition: When to trigger the alert

### Settings Tab

Configure Telegram connection and check interval.

- Bot Token: Your Telegram bot authentication
- Chat ID: Your Telegram user ID for notifications
- Check Interval: How often to check prices (1-60 minutes)

### Activity Log Tab

View notification history and application events.

## System Requirements

- Windows 7 or newer (64-bit)
- Active internet connection
- Telegram account

## Technology Stack

- Python 3.8+
- PyQt5 for the desktop UI
- CoinGecko API for price data
- Telegram Bot API for notifications
- PyInstaller for building the executable

## Project Structure

```
CryptoAlertBot/
├── main.py                    Entry point
├── build_exe.py              Build script
├── requirements.txt          Python dependencies
├── frontend/                 UI layer (PyQt5)
│   ├── main_window.py
│   ├── light_styles.py
│   └── dark_styles.py
└── backend/                  Business logic
    ├── api/                  External API clients
    ├── telegram/            Telegram integration
    ├── checker/             Price monitoring
    ├── models/              Data structures
    ├── services/            Service layer
    ├── storage/             Configuration storage
    └── data/                Cryptocurrency database
```

## Security

- All configuration stored locally in config.json
- Telegram token stored only on your computer
- No cloud servers or data tracking
- Source code is open for review
- Licensed under MIT

## License

MIT License. See LICENSE file for details.

## FAQ

Q: Is this free?
A: Yes, completely free and open source.

Q: Will my Telegram be spammed?
A: No, the bot only sends alerts to your Chat ID.

Q: How accurate are prices?
A: Prices come from CoinGecko API. Updates are configurable (1-60 minutes).

Q: Can I use on Mac or Linux?
A: Currently Windows only.

Q: What if I lose my token?
A: Create a new bot with BotFather. There's no limit on bot creation.

Q: Can I set multiple alerts for one coin?
A: Yes, you can create multiple alerts with different price targets.

## Support

For bug reports and feature requests, contact @lingytm on Telegram.

Subscribe to https://t.me/toolsforcrypto for updates on new tools.

## Disclaimer

CryptoAlertBot is a price monitoring tool. It does not provide investment advice, make trading decisions, or manage crypto funds. Use at your own risk. Always do your own research before making investment decisions.

Cryptocurrency markets are volatile and prices can change rapidly.
