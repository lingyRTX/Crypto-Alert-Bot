"""Professional light theme stylesheet"""

LIGHT_STYLESHEET = """
    * {
        margin: 0;
        padding: 0;
    }

    QMainWindow {
        background-color: #ffffff;
    }

    QWidget {
        background-color: #ffffff;
        color: #1a1a1a;
    }

    /* Tabs */
    QTabWidget::pane {
        border: 1px solid #e0e0e0;
        background-color: #ffffff;
    }

    QTabBar {
        background-color: #f5f5f5;
        border-bottom: 2px solid #e0e0e0;
    }

    QTabBar::tab {
        background-color: #f5f5f5;
        color: #666666;
        padding: 10px 24px;
        margin-right: 2px;
        border: none;
        font-weight: 600;
        font-size: 12px;
        min-width: 140px;
        max-width: 200px;
    }

    QTabBar::tab:selected {
        background-color: #ffffff;
        color: #2563eb;
        border-bottom: 2px solid #2563eb;
        padding: 10px 24px;
    }

    QTabBar::tab:hover:!selected {
        background-color: #eeeeee;
        color: #333333;
    }

    /* GroupBox */
    QGroupBox {
        color: #1a1a1a;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        margin-top: 10px;
        padding: 0px;
        font-weight: 600;
        font-size: 12px;
        background-color: #fafafa;
    }

    QGroupBox::title {
        subcontrol-origin: margin;
        left: 16px;
        padding: 8px 8px 8px 8px;
        color: #1a1a1a;
        font-weight: 700;
        font-size: 13px;
    }

    /* Labels */
    QLabel {
        color: #666666;
        font-size: 11px;
        font-weight: 500;
    }

    QLabel#title {
        color: #000000;
        font-size: 24px;
        font-weight: 700;
    }

    QLabel#subtitle {
        color: #999999;
        font-size: 12px;
        font-weight: 400;
    }

    QLabel#formLabel {
        color: #1a1a1a;
        font-size: 12px;
        font-weight: 600;
    }

    /* Input Fields */
    QLineEdit, QSpinBox, QDoubleSpinBox {
        border: 1px solid #d0d0d0;
        border-radius: 6px;
        padding: 10px 12px;
        background-color: #ffffff;
        color: #1a1a1a;
        font-size: 12px;
        selection-background-color: #2563eb;
        selection-color: #ffffff;
        font-weight: 400;
        min-height: 36px;
    }

    QLineEdit:focus, QSpinBox:focus, QDoubleSpinBox:focus {
        border: 2px solid #2563eb;
        background-color: #ffffff;
    }

    QLineEdit::placeholder {
        color: #cccccc;
    }

    /* ComboBox */
    QComboBox {
        border: 1px solid #d0d0d0;
        border-radius: 6px;
        padding: 10px 12px;
        background-color: #ffffff;
        color: #1a1a1a;
        font-size: 12px;
        selection-background-color: #2563eb;
        font-weight: 400;
        min-height: 36px;
    }

    QComboBox:focus {
        border: 2px solid #2563eb;
        background-color: #ffffff;
    }

    QComboBox::drop-down {
        subcontrol-origin: content;
        subcontrol-position: right;
        width: 28px;
        border: none;
        background-color: transparent;
        margin-right: 4px;
    }

    QComboBox::down-arrow {
        image: none;
    }

    QComboBox QAbstractItemView {
        background-color: #ffffff;
        color: #1a1a1a;
        selection-background-color: #2563eb;
        selection-color: #ffffff;
        border: 1px solid #d0d0d0;
        border-radius: 6px;
        outline: none;
        padding: 4px 0px;
    }

    QComboBox QAbstractItemView::item {
        padding: 8px 12px;
        height: 36px;
        font-size: 12px;
    }

    QComboBox QAbstractItemView::item:selected {
        background-color: #2563eb;
    }

    QComboBox QAbstractItemView::item:hover {
        background-color: #e8f0fe;
    }

    /* Buttons */
    QPushButton {
        background-color: #2563eb;
        color: #ffffff;
        border: none;
        border-radius: 6px;
        padding: 9px 16px;
        font-weight: 600;
        font-size: 12px;
        min-height: 36px;
        min-width: 100px;
    }

    QPushButton:hover {
        background-color: #1d4ed8;
    }

    QPushButton:pressed {
        background-color: #1e40af;
    }

    QPushButton:disabled {
        background-color: #e0e0e0;
        color: #999999;
    }

    /* Delete Button */
    QPushButton#deleteBtn {
        background-color: #dc2626;
        color: #ffffff;
        padding: 8px 12px;
        font-size: 11px;
        min-height: 32px;
        min-width: 75px;
    }

    QPushButton#deleteBtn:hover {
        background-color: #b91c1c;
    }

    /* Test Button */
    QPushButton#testBtn {
        background-color: #059669;
    }

    QPushButton#testBtn:hover {
        background-color: #047857;
    }

    /* Secondary Button */
    QPushButton#secondaryBtn {
        background-color: #f3f4f6;
        color: #1a1a1a;
        border: 1px solid #d0d0d0;
    }

    QPushButton#secondaryBtn:hover {
        background-color: #e5e7eb;
        border: 1px solid #b0b0b0;
    }

    /* Table */
    QTableWidget {
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        background-color: #ffffff;
        alternate-background-color: #f9f9f9;
        gridline-color: #f0f0f0;
        outline: none;
    }

    QTableWidget::item {
        padding: 11px 12px;
        color: #1a1a1a;
        border: none;
        font-size: 12px;
        height: 38px;
    }

    QTableWidget::item:selected {
        background-color: #e8f0fe;
        color: #1a1a1a;
    }

    QTableWidget::item:alternate {
        background-color: #f9f9f9;
    }

    QHeaderView::section {
        background-color: #f5f5f5;
        color: #666666;
        padding: 10px 12px;
        border: none;
        border-bottom: 1px solid #e0e0e0;
        font-weight: 700;
        font-size: 11px;
        text-align: left;
    }

    /* TextEdit */
    QTextEdit {
        border: 1px solid #d0d0d0;
        border-radius: 6px;
        background-color: #ffffff;
        color: #1a1a1a;
        font-size: 11px;
        font-family: 'Consolas', 'Monaco', monospace;
        padding: 10px;
    }

    QTextEdit:focus {
        border: 2px solid #2563eb;
    }

    /* Scrollbar */
    QScrollBar:vertical {
        background-color: #f5f5f5;
        width: 10px;
        border: none;
    }

    QScrollBar::handle:vertical {
        background-color: #c0c0c0;
        border-radius: 5px;
        min-height: 20px;
        margin: 2px 2px 2px 2px;
    }

    QScrollBar::handle:vertical:hover {
        background-color: #a0a0a0;
    }

    QScrollBar::sub-line:vertical, QScrollBar::add-line:vertical {
        border: none;
        background: none;
    }

    QScrollBar:horizontal {
        background-color: #f5f5f5;
        height: 10px;
        border: none;
    }

    QScrollBar::handle:horizontal {
        background-color: #c0c0c0;
        border-radius: 5px;
        min-width: 20px;
        margin: 2px 2px 2px 2px;
    }

    QScrollBar::handle:horizontal:hover {
        background-color: #a0a0a0;
    }

    /* Separator */
    QFrame#separator {
        background-color: #e0e0e0;
        height: 1px;
    }

    /* StatusBar */
    QStatusBar {
        background-color: #f5f5f5;
        color: #666666;
        border-top: 1px solid #e0e0e0;
        font-size: 11px;
    }
"""
