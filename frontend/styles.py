"""Стили для интерфейса"""

STYLESHEET = """
    QMainWindow {
        background-color: #f5f5f5;
    }

    QWidget {
        background-color: #f5f5f5;
    }

    QTabWidget::pane {
        border: none;
    }

    QTabBar::tab {
        background-color: #e0e0e0;
        color: #333333;
        padding: 8px 20px;
        margin-right: 2px;
        border: none;
        border-radius: 4px 4px 0 0;
    }

    QTabBar::tab:selected {
        background-color: #2196F3;
        color: white;
    }

    QTabBar::tab:hover {
        background-color: #1976D2;
    }

    QGroupBox {
        color: #333333;
        border: 2px solid #ddd;
        border-radius: 6px;
        margin-top: 10px;
        padding-top: 10px;
    }

    QGroupBox::title {
        subcontrol-origin: margin;
        left: 10px;
        padding: 0 3px 0 3px;
    }

    QLabel {
        color: #333333;
    }

    QLineEdit, QSpinBox {
        border: 1px solid #ccc;
        border-radius: 4px;
        padding: 6px;
        background-color: white;
        color: #333333;
    }

    QLineEdit:focus, QSpinBox:focus {
        border: 2px solid #2196F3;
    }

    QPushButton {
        background-color: #2196F3;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 8px 16px;
        font-weight: bold;
    }

    QPushButton:hover {
        background-color: #1976D2;
    }

    QPushButton:pressed {
        background-color: #1565C0;
    }

    QPushButton#deleteBtn {
        background-color: #f44336;
    }

    QPushButton#deleteBtn:hover {
        background-color: #d32f2f;
    }

    QPushButton#testBtn {
        background-color: #4CAF50;
    }

    QPushButton#testBtn:hover {
        background-color: #388E3C;
    }

    QComboBox {
        border: 1px solid #ccc;
        border-radius: 4px;
        padding: 6px;
        background-color: white;
        color: #333333;
    }

    QComboBox:focus {
        border: 2px solid #2196F3;
    }

    QListWidget {
        border: 1px solid #ddd;
        border-radius: 4px;
        background-color: white;
    }

    QListWidget::item {
        padding: 10px;
        border-bottom: 1px solid #eee;
    }

    QListWidget::item:selected {
        background-color: #2196F3;
        color: white;
    }

    QListWidget::item:hover {
        background-color: #e3f2fd;
    }

    QTextEdit {
        border: 1px solid #ddd;
        border-radius: 4px;
        background-color: white;
        color: #333333;
    }

    QCheckBox {
        color: #333333;
        spacing: 5px;
    }

    QCheckBox::indicator {
        width: 18px;
        height: 18px;
    }

    QCheckBox::indicator:unchecked {
        background-color: white;
        border: 1px solid #ccc;
        border-radius: 3px;
    }

    QCheckBox::indicator:checked {
        background-color: #2196F3;
        border: 1px solid #2196F3;
        border-radius: 3px;
        image: url();
    }
"""
