"""Main application window with complete UI redesign"""
import uuid
from datetime import datetime
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget,
    QLabel, QLineEdit, QPushButton, QComboBox, QSpinBox,
    QTableWidget, QTableWidgetItem, QGroupBox, QTextEdit,
    QMessageBox, QHeaderView, QFrame, QScrollArea, QMenu
)
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import Qt, QTimer, QSize, QUrl
from PyQt5.QtGui import QFont, QColor
from backend.services import AlertService
from backend.models import Alert
from backend.data.cryptocurrencies import get_crypto_names, get_crypto_id
from .light_styles import LIGHT_STYLESHEET


class CryptoAlertBotWindow(QMainWindow):
    """Professional cryptocurrency price alert application"""

    def __init__(self, service: AlertService):
        super().__init__()
        self.service = service
        self.init_ui()
        self.load_alerts()
        self.setup_timers()

    def init_ui(self) -> None:
        """Initialize redesigned UI"""
        self.setWindowTitle("CryptoAlertBot - Real-time Crypto Alerts")
        self.setGeometry(100, 100, 1500, 900)
        self.setMinimumSize(1300, 800)
        self.setStyleSheet(LIGHT_STYLESHEET)

        # Create menu bar
        self._create_menu_bar()

        # Main widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(24, 20, 24, 16)
        main_layout.setSpacing(0)

        # Header
        header_widget = self._create_header()
        main_layout.addWidget(header_widget)

        # Separator
        separator = QFrame()
        separator.setObjectName("separator")
        separator.setFixedHeight(1)
        main_layout.addWidget(separator)
        main_layout.addSpacing(16)

        # Tabs
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.North)
        main_layout.addWidget(self.tabs)

        self.tabs.addTab(self._create_alerts_tab(), "Price Alerts")
        self.tabs.addTab(self._create_settings_tab(), "Settings")
        self.tabs.addTab(self._create_logs_tab(), "Activity Log")

        # Status bar
        self.statusBar().showMessage("Ready")

    def _create_header(self) -> QWidget:
        """Create header with title"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 12)
        layout.setSpacing(4)

        title = QLabel("CryptoAlertBot")
        title.setObjectName("title")

        subtitle = QLabel("Real-time cryptocurrency price monitoring with Telegram notifications")
        subtitle.setObjectName("subtitle")

        layout.addWidget(title)
        layout.addWidget(subtitle)

        return widget

    def _create_menu_bar(self) -> None:
        """Create menu bar with Help and Contact options"""
        menubar = self.menuBar()

        # Help menu
        help_menu = menubar.addMenu("Help")

        # Contact action
        contact_action = help_menu.addAction("📞 Contact & Bug Reports")
        contact_action.triggered.connect(self.show_contact_dialog)

    def show_contact_dialog(self) -> None:
        """Show contact information dialog"""
        contact_text = """
        <html>
        <head>
            <style>
                body { font-family: Arial, sans-serif; }
                h2 { color: #2563eb; margin-top: 0; }
                p { line-height: 1.6; color: #333; }
                .highlight { color: #059669; font-weight: bold; font-size: 14px; }
                .telegram { color: #0088cc; }
            </style>
        </head>
        <body>
            <h2>📞 Contact Information</h2>

            <p><strong>Have questions or found a bug?</strong></p>

            <p>Reach out via Telegram:</p>
            <p class="highlight telegram">@lingytm</p>

            <h3>What to report:</h3>
            <ul>
                <li>🐛 <strong>Bugs</strong> - Application crashes or unexpected behavior</li>
                <li>💡 <strong>Feature Requests</strong> - New ideas for improvements</li>
                <li>❓ <strong>Questions</strong> - How to use the application</li>
            </ul>

            <h3>⚠️ Please Note:</h3>
            <p><strong>This Telegram is ONLY for bug reports and feature requests.</strong></p>
            <p>Do not send:</p>
            <ul>
                <li>Investment or trading advice requests</li>
                <li>Crypto price predictions</li>
                <li>General cryptocurrency questions</li>
            </ul>

            <p>The application is designed to monitor prices and send alerts.
            That's it. Use it responsibly! 🚀</p>
        </body>
        </html>
        """

        QMessageBox.information(self, "Contact & Bug Reports", contact_text)

    def _create_alerts_tab(self) -> QWidget:
        """Create alerts tab"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(16)

        form_group = self._create_alert_form()
        layout.addWidget(form_group)

        table_group = self._create_alerts_table()
        layout.addWidget(table_group, 1)

        return widget

    def _create_alert_form(self) -> QGroupBox:
        """Create alert form with proper layout"""
        group = QGroupBox("Create New Alert")
        layout = QVBoxLayout(group)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(16)

        # Three columns layout
        columns_layout = QHBoxLayout()
        columns_layout.setSpacing(24)

        # Column 1: Cryptocurrency
        col1 = QVBoxLayout()
        col1.setSpacing(8)
        label1 = QLabel("Cryptocurrency")
        label1.setObjectName("formLabel")
        col1.addWidget(label1)
        self.coin_combo = QComboBox()
        self.coin_combo.addItems(get_crypto_names())
        col1.addWidget(self.coin_combo)
        columns_layout.addLayout(col1)

        # Column 2: Price
        col2 = QVBoxLayout()
        col2.setSpacing(8)
        label2 = QLabel("Target Price (USD)")
        label2.setObjectName("formLabel")
        col2.addWidget(label2)
        self.price_input = QLineEdit()
        self.price_input.setPlaceholderText("e.g., 45000")
        col2.addWidget(self.price_input)
        columns_layout.addLayout(col2)

        # Column 3: Condition
        col3 = QVBoxLayout()
        col3.setSpacing(8)
        label3 = QLabel("Condition")
        label3.setObjectName("formLabel")
        col3.addWidget(label3)
        self.condition_combo = QComboBox()
        self.condition_combo.addItems(["Price falls below", "Price rises above"])
        col3.addWidget(self.condition_combo)
        columns_layout.addLayout(col3)

        # Button column
        btn_col = QVBoxLayout()
        btn_col.setSpacing(8)
        btn_label = QLabel(" ")
        btn_col.addWidget(btn_label)
        add_btn = QPushButton("+ Add Alert")
        add_btn.setMinimumWidth(150)
        add_btn.clicked.connect(self.add_alert)
        btn_col.addWidget(add_btn)
        columns_layout.addLayout(btn_col)

        layout.addLayout(columns_layout)
        return group

    def _create_alerts_table(self) -> QGroupBox:
        """Create alerts table"""
        group = QGroupBox("Active Alerts")
        layout = QVBoxLayout(group)
        layout.setContentsMargins(20, 20, 20, 20)

        self.alerts_table = QTableWidget()
        self.alerts_table.setColumnCount(6)
        self.alerts_table.setHorizontalHeaderLabels([
            "Cryptocurrency", "Target Price", "Condition", "Current Price", "Status", "Actions"
        ])

        header = self.alerts_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeToContents)

        self.alerts_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.alerts_table.setSelectionMode(QTableWidget.SingleSelection)
        self.alerts_table.setAlternatingRowColors(True)
        self.alerts_table.setShowGrid(False)
        self.alerts_table.setMinimumHeight(350)

        layout.addWidget(self.alerts_table)
        group.setLayout(layout)
        return group

    def _create_settings_tab(self) -> QWidget:
        """Create settings tab with 2-column layout"""
        widget = QWidget()
        main_layout = QHBoxLayout(widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(16)

        # Left column: forms
        left_layout = QVBoxLayout()
        left_layout.setSpacing(16)

        telegram_group = self._create_telegram_group()
        left_layout.addWidget(telegram_group)

        interval_group = self._create_interval_group()
        left_layout.addWidget(interval_group)

        left_layout.addStretch()

        # Right column: guide
        guide_group = self._create_guide_group()

        main_layout.addLayout(left_layout, 1)
        main_layout.addWidget(guide_group, 1)

        return widget

    def _create_telegram_group(self) -> QGroupBox:
        """Create Telegram settings"""
        group = QGroupBox("Telegram Configuration")
        layout = QVBoxLayout(group)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(14)

        # Token
        token_label = QLabel("Bot Token")
        token_label.setObjectName("formLabel")
        layout.addWidget(token_label)

        self.token_input = QLineEdit()
        self.token_input.setEchoMode(QLineEdit.Password)
        self.token_input.setPlaceholderText("Paste your Telegram bot token...")
        layout.addWidget(self.token_input)

        # User ID
        user_label = QLabel("Your Chat ID")
        user_label.setObjectName("formLabel")
        layout.addWidget(user_label)

        self.user_id_input = QLineEdit()
        self.user_id_input.setPlaceholderText("Your numeric Telegram user ID...")
        layout.addWidget(self.user_id_input)

        # Buttons
        btn_layout = QHBoxLayout()
        save_btn = QPushButton("Save Settings")
        save_btn.clicked.connect(self.save_telegram_config)
        test_btn = QPushButton("Test Connection")
        test_btn.setObjectName("testBtn")
        test_btn.clicked.connect(self.test_telegram)
        btn_layout.addWidget(save_btn)
        btn_layout.addWidget(test_btn)
        layout.addLayout(btn_layout)

        group.setLayout(layout)
        return group

    def _create_interval_group(self) -> QGroupBox:
        """Create interval settings"""
        group = QGroupBox("Price Check Interval")
        layout = QVBoxLayout(group)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(14)

        label = QLabel("Check Frequency")
        label.setObjectName("formLabel")
        layout.addWidget(label)

        interval_layout = QHBoxLayout()
        self.interval_spinbox = QSpinBox()
        self.interval_spinbox.setMinimum(1)
        self.interval_spinbox.setMaximum(60)
        self.interval_spinbox.setSuffix(" min")
        self.interval_spinbox.setMaximumWidth(100)
        interval_layout.addWidget(self.interval_spinbox)

        save_btn = QPushButton("Save")
        save_btn.setMaximumWidth(100)
        save_btn.clicked.connect(self.save_interval)
        interval_layout.addWidget(save_btn)
        interval_layout.addStretch()

        layout.addLayout(interval_layout)

        group.setLayout(layout)
        return group

    def _create_guide_group(self) -> QGroupBox:
        """Create detailed setup guide"""
        group = QGroupBox("Setup Guide")
        layout = QVBoxLayout(group)
        layout.setContentsMargins(20, 20, 20, 20)

        guide_text = QTextEdit()
        guide_text.setReadOnly(True)
        guide_text.setPlainText(
            "═══════════════════════════════════════\n"
            "COMPLETE SETUP GUIDE\n"
            "═══════════════════════════════════════\n\n"
            "STEP 1: CREATE TELEGRAM BOT\n"
            "─────────────────────────────────────\n"
            "1. Open Telegram app\n"
            "2. Search: @BotFather\n"
            "3. Click 'Start' or send /start\n"
            "4. Type: /newbot\n"
            "5. Choose bot name (e.g., MyPriceBot)\n"
            "6. Choose bot username (must end with 'bot')\n"
            "   Example: my_price_bot_123\n"
            "7. Copy the TOKEN shown\n"
            "   Format: 123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11\n"
            "8. Paste token in 'Bot Token' field above\n\n"

            "STEP 1.5: ACTIVATE YOUR BOT\n"
            "─────────────────────────────────────\n"
            "⚠️ IMPORTANT: After creating the bot:\n"
            "1. Search for your bot username\n"
            "   (the one you created in step 6)\n"
            "2. Click 'Start' button\n"
            "3. Or send any message (like /start)\n"
            "4. This activates the bot for you\n"
            "   (Bot won't work without this!)\n\n"

            "STEP 2: GET YOUR TELEGRAM ID\n"
            "─────────────────────────────────────\n"
            "1. Search: @userinfobot\n"
            "2. Click 'Start' or send any message\n"
            "3. Bot replies with your ID\n"
            "   Example: Your user id is 123456789\n"
            "4. Copy the NUMBER only\n"
            "5. Paste in 'Your Chat ID' field above\n\n"

            "STEP 3: VERIFY SETUP\n"
            "─────────────────────────────────────\n"
            "1. Paste Bot Token → click 'Save Settings'\n"
            "2. Paste Chat ID → click 'Save Settings'\n"
            "3. Click 'Test Connection'\n"
            "4. Check Telegram - should receive message\n"
            "5. If success: Ready to create alerts!\n\n"

            "STEP 4: CREATE FIRST ALERT\n"
            "─────────────────────────────────────\n"
            "1. Go to 'Price Alerts' tab\n"
            "2. Select cryptocurrency (e.g., Bitcoin)\n"
            "3. Enter target price (e.g., 45000)\n"
            "4. Choose condition: falls below/rises above\n"
            "5. Click '+ Add Alert'\n"
            "6. Alert is now monitoring 24/7\n\n"

            "MONITORING\n"
            "─────────────────────────────────────\n"
            "• Checks every 5 minutes (default)\n"
            "• Change interval in 'Settings' tab\n"
            "• Telegram notifies when price hits target\n"
            "• Multiple alerts supported\n"
            "• Keep app running or use Task Scheduler\n\n"

            "═══════════════════════════════════════"
        )
        guide_text.setFont(QFont("Consolas", 9))
        layout.addWidget(guide_text)

        group.setLayout(layout)
        return group

    def _create_logs_tab(self) -> QWidget:
        """Create activity logs tab"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(12)

        group = QGroupBox("Activity Log")
        group_layout = QVBoxLayout(group)
        group_layout.setContentsMargins(20, 20, 20, 20)

        self.logs_text = QTextEdit()
        self.logs_text.setReadOnly(True)
        group_layout.addWidget(self.logs_text)

        btn_layout = QHBoxLayout()
        clear_btn = QPushButton("Clear Logs")
        clear_btn.setObjectName("secondaryBtn")
        clear_btn.setMaximumWidth(120)
        clear_btn.clicked.connect(lambda: self.logs_text.clear())
        btn_layout.addStretch()
        btn_layout.addWidget(clear_btn)
        group_layout.addLayout(btn_layout)

        group.setLayout(group_layout)
        layout.addWidget(group)

        return widget

    def load_alerts(self) -> None:
        """Load alerts"""
        alerts = self.service.get_alerts()
        self.alerts_table.setRowCount(len(alerts))

        for row, alert in enumerate(alerts):
            # Cryptocurrency
            coin_item = QTableWidgetItem(alert.coin.upper())
            coin_item.setForeground(QColor("#2563eb"))
            coin_item.setFont(QFont("Segoe UI", 12, QFont.Bold))
            self.alerts_table.setItem(row, 0, coin_item)

            # Target Price
            price_item = QTableWidgetItem(f"${alert.price:,.2f}")
            self.alerts_table.setItem(row, 1, price_item)

            # Condition
            condition = "↓ Below" if alert.condition == "below" else "↑ Above"
            condition_item = QTableWidgetItem(condition)
            self.alerts_table.setItem(row, 2, condition_item)

            # Current Price
            current_price = self.service.get_current_price(alert.coin)
            price_item = QTableWidgetItem(f"${current_price:,.2f}")
            self.alerts_table.setItem(row, 3, price_item)

            # Status
            status_text = "● Active" if alert.active else "○ Inactive"
            status_color = QColor("#238636") if alert.active else QColor("#6e7681")
            status_item = QTableWidgetItem(status_text)
            status_item.setForeground(status_color)
            status_item.setFont(QFont("Segoe UI", 11, QFont.Bold))
            self.alerts_table.setItem(row, 4, status_item)

            # Delete button
            delete_btn = QPushButton("Remove")
            delete_btn.setObjectName("deleteBtn")
            delete_btn.clicked.connect(lambda checked, aid=alert.id: self.delete_alert(aid))
            self.alerts_table.setCellWidget(row, 5, delete_btn)

        self.log_event(f"Loaded {len(alerts)} alerts")

        token = self.service.config.get_telegram_token()
        user_id = self.service.config.get_telegram_user_id()
        interval = self.service.config.get_check_interval()

        if token:
            self.token_input.setText(token)
        if user_id:
            self.user_id_input.setText(str(user_id))
        self.interval_spinbox.setValue(interval)

    def add_alert(self) -> None:
        """Add new alert"""
        coin_name = self.coin_combo.currentText()
        coin = get_crypto_id(coin_name)
        price_text = self.price_input.text().strip()
        condition = "below" if "below" in self.condition_combo.currentText().lower() else "above"

        if not price_text:
            QMessageBox.warning(self, "Error", "Enter a target price")
            return

        try:
            price = float(price_text)
            if price <= 0:
                raise ValueError("Price must be positive")

            self.service.create_alert(coin, price, condition)
            self.price_input.clear()
            self.load_alerts()
            self.log_event(f"✓ Alert: {coin_name} @ ${price:,.2f}")
            QMessageBox.information(self, "Success", f"Alert created for {coin_name}")
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid price")

    def delete_alert(self, alert_id: str) -> None:
        """Delete alert"""
        self.service.delete_alert(alert_id)
        self.load_alerts()
        self.log_event("✗ Alert removed")

    def save_telegram_config(self) -> None:
        """Save Telegram config"""
        token = self.token_input.text().strip()
        user_id = self.user_id_input.text().strip()

        if not token or not user_id:
            QMessageBox.warning(self, "Error", "Fill all fields")
            return

        if self.service.set_telegram_token(token):
            self.service.set_telegram_user_id(user_id)
            self.log_event("✓ Telegram saved")
            QMessageBox.information(self, "Success", "Settings saved")
        else:
            self.log_event("✗ Invalid token")
            QMessageBox.warning(self, "Error", "Invalid token")

    def test_telegram(self) -> None:
        """Test Telegram"""
        if self.service.test_telegram():
            self.log_event("✓ Test sent")
            QMessageBox.information(self, "Success", "Test sent!")
        else:
            self.log_event("✗ Test failed")
            QMessageBox.warning(self, "Error", "Test failed")

    def save_interval(self) -> None:
        """Save interval"""
        interval = self.interval_spinbox.value()
        self.service.set_check_interval(interval)
        self.log_event(f"⏱ Interval: {interval}m")
        QMessageBox.information(self, "Success", f"Interval set to {interval}m")

    def setup_timers(self) -> None:
        """Setup timers"""
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update_prices)
        self.update_timer.start(60000)

    def update_prices(self) -> None:
        """Update prices"""
        alerts = self.service.get_alerts()
        for row, alert in enumerate(alerts):
            if row < self.alerts_table.rowCount():
                price = self.service.get_current_price(alert.coin)
                item = QTableWidgetItem(f"${price:,.2f}")
                self.alerts_table.setItem(row, 3, item)

    def log_event(self, message: str) -> None:
        """Log event"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.logs_text.insertPlainText(f"[{timestamp}] {message}\n")
        self.logs_text.verticalScrollBar().setValue(
            self.logs_text.verticalScrollBar().maximum()
        )

    def closeEvent(self, event) -> None:
        """Handle close"""
        self.service.stop()
        event.accept()
