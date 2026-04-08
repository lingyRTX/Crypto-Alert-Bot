"""Professional dark theme stylesheet - Complete Redesign"""

DARK_STYLESHEET = """
    * {
        margin: 0;
        padding: 0;
    }

    QMainWindow {
        background-color: #0d1117;
        border: 1px solid #21262d;
    }

    QWidget {
        background-color: #0d1117;
        color: #e0e0e0;
    }

    QMainWindow::separator {
        background-color: #21262d;
        width: 1px;
        height: 1px;
    }

    /* Tabs - Polished */
    QTabWidget::pane {
        border: none;
        background-color: #0d1117;
    }

    QTabBar {
        background-color: #0d1117;
        border-bottom: 2px solid #30363d;
    }

    QTabBar::tab {
        background-color: #0d1117;
        color: #8b949e;
        padding: 14px 32px;
        margin-right: 2px;
        border: none;
        font-weight: 600;
        font-size: 13px;
        letter-spacing: 0.3px;
        min-width: 130px;
    }

    QTabBar::tab:selected {
        background-color: #2563eb;
        color: #ffffff;
        border-bottom: none;
        padding: 14px 32px;
    }

    QTabBar::tab:hover:!selected {
        color: #c9d1d9;
        background-color: #161b22;
    }

    /* GroupBox - Clean */
    QGroupBox {
        color: #c9d1d9;
        border: 1px solid #30363d;
        border-radius: 10px;
        margin-top: 10px;
        padding: 0px;
        font-weight: 600;
        font-size: 13px;
        background-color: #0f1419;
    }

    QGroupBox::title {
        subcontrol-origin: margin;
        left: 16px;
        padding: 8px 8px 8px 8px;
        color: #c9d1d9;
        font-weight: 700;
        font-size: 13px;
    }

    /* Labels */
    QLabel {
        color: #8b949e;
        font-size: 11px;
        font-weight: 500;
    }

    QLabel#title {
        color: #ffffff;
        font-size: 20px;
        font-weight: 700;
    }

    QLabel#subtitle {
        color: #6e7681;
        font-size: 12px;
        font-weight: 400;
    }

    QLabel#formLabel {
        color: #c9d1d9;
        font-size: 12px;
        font-weight: 600;
    }

    /* Input Fields - Enhanced */
    QLineEdit, QSpinBox, QDoubleSpinBox {
        border: 1px solid #30363d;
        border-radius: 6px;
        padding: 11px 13px;
        background-color: #0f1419;
        color: #e0e0e0;
        font-size: 12px;
        selection-background-color: #2563eb;
        font-weight: 400;
        min-height: 38px;
    }

    QLineEdit:focus, QSpinBox:focus, QDoubleSpinBox:focus {
        border: 2px solid #2563eb;
        background-color: #161b22;
    }

    QLineEdit::placeholder {
        color: #484f58;
    }

    /* ComboBox - Enhanced Professional Style */
    QComboBox {
        border: 2px solid #30363d;
        border-radius: 6px;
        padding: 10px 12px;
        padding-right: 32px;
        background-color: #0f1419;
        color: #e0e0e0;
        font-size: 12px;
        font-weight: 400;
        min-height: 38px;
        selection-background-color: #2563eb;
    }

    QComboBox:hover {
        border: 2px solid #484f58;
        background-color: #161b22;
    }

    QComboBox:focus {
        border: 2px solid #2563eb;
        background-color: #161b22;
        outline: none;
    }

    QComboBox::drop-down {
        subcontrol-origin: padding;
        subcontrol-position: right center;
        width: 28px;
        border: none;
        background-color: transparent;
        margin-right: 4px;
    }

    QComboBox::down-arrow {
        image: none;
        width: 16px;
        height: 16px;
        background-image: url(data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%238b949e'%3E%3Cpath d='M7 10l5 5 5-5H7z'/%3E%3C/svg%3E);
        background-repeat: no-repeat;
        background-position: center;
    }

    QComboBox::down-arrow:on {
        background-image: url(data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%232563eb'%3E%3Cpath d='M17 14l-5-5-5 5h10z'/%3E%3C/svg%3E);
    }

    QComboBox QAbstractItemView {
        background-color: #0f1419;
        color: #c9d1d9;
        selection-background-color: #2563eb;
        selection-color: #ffffff;
        border: 2px solid #30363d;
        border-radius: 6px;
        outline: none;
        padding: 6px 0px;
        margin-top: 4px;
    }

    QComboBox QAbstractItemView::item {
        padding: 10px 14px;
        height: 36px;
        font-size: 12px;
        color: #c9d1d9;
    }

    QComboBox QAbstractItemView::item:selected {
        background-color: #2563eb;
        color: #ffffff;
        font-weight: 500;
    }

    QComboBox QAbstractItemView::item:hover {
        background-color: #1f6feb;
        color: #ffffff;
    }

    /* Buttons - Enhanced */
    QPushButton {
        background-color: #2563eb;
        color: #ffffff;
        border: none;
        border-radius: 6px;
        padding: 10px 18px;
        font-weight: 600;
        font-size: 12px;
        min-height: 38px;
        min-width: 100px;
        letter-spacing: 0.3px;
    }

    QPushButton:hover {
        background-color: #1d4ed8;
    }

    QPushButton:pressed {
        background-color: #1e40af;
    }

    QPushButton:disabled {
        background-color: #21262d;
        color: #6e7681;
    }

    /* Delete Button */
    QPushButton#deleteBtn {
        background-color: #c0392b;
        padding: 8px 14px;
        font-size: 11px;
        min-height: 34px;
        min-width: 80px;
    }

    QPushButton#deleteBtn:hover {
        background-color: #a93226;
    }

    QPushButton#deleteBtn:pressed {
        background-color: #922b21;
    }

    /* Test Button */
    QPushButton#testBtn {
        background-color: #238636;
    }

    QPushButton#testBtn:hover {
        background-color: #2ea043;
    }

    QPushButton#testBtn:pressed {
        background-color: #1a7f37;
    }

    /* Secondary Button */
    QPushButton#secondaryBtn {
        background-color: #2d333b;
        color: #c9d1d9;
        border: 1px solid #444c56;
    }

    QPushButton#secondaryBtn:hover {
        background-color: #30363d;
        border: 1px solid #484f58;
    }

    /* Table - Professional */
    QTableWidget {
        border: 1px solid #30363d;
        border-radius: 8px;
        background-color: #0f1419;
        alternate-background-color: #0d1117;
        gridline-color: #21262d;
        outline: none;
    }

    QTableWidget::item {
        padding: 12px 14px;
        color: #c9d1d9;
        border: none;
        font-size: 12px;
        height: 40px;
    }

    QTableWidget::item:selected {
        background-color: #1f6feb;
        color: #ffffff;
    }

    QTableWidget::item:alternate {
        background-color: #0d1117;
    }

    QHeaderView::section {
        background-color: #0d1117;
        color: #8b949e;
        padding: 12px 14px;
        border: none;
        border-bottom: 2px solid #30363d;
        font-weight: 700;
        font-size: 12px;
        text-align: left;
    }

    /* TextEdit */
    QTextEdit {
        border: 1px solid #30363d;
        border-radius: 6px;
        background-color: #0f1419;
        color: #c9d1d9;
        font-size: 11px;
        font-family: 'Consolas', 'Monaco', monospace;
        padding: 12px;
    }

    QTextEdit:focus {
        border: 2px solid #2563eb;
    }

    /* Scrollbar */
    QScrollBar:vertical {
        background-color: #0d1117;
        width: 10px;
        border: none;
    }

    QScrollBar::handle:vertical {
        background-color: #30363d;
        border-radius: 5px;
        min-height: 20px;
        margin: 2px 2px 2px 2px;
    }

    QScrollBar::handle:vertical:hover {
        background-color: #484f58;
    }

    QScrollBar::sub-line:vertical, QScrollBar::add-line:vertical {
        border: none;
        background: none;
    }

    QScrollBar:horizontal {
        background-color: #0d1117;
        height: 10px;
        border: none;
    }

    QScrollBar::handle:horizontal {
        background-color: #30363d;
        border-radius: 5px;
        min-width: 20px;
        margin: 2px 2px 2px 2px;
    }

    QScrollBar::handle:horizontal:hover {
        background-color: #484f58;
    }

    /* Separator */
    QFrame#separator {
        background-color: #30363d;
        height: 1px;
    }

    /* StatusBar */
    QStatusBar {
        background-color: #0f1419;
        color: #8b949e;
        border-top: 1px solid #30363d;
        font-size: 11px;
    }
"""
