"""CryptoAlertBot - Cryptocurrency Price Alert Application"""
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from backend.storage import ConfigManager
from backend.services import AlertService
from frontend.main_window import CryptoAlertBotWindow


def main():
    """Launch the application"""
    # Initialize configuration
    config_manager = ConfigManager("config.json")

    # Initialize service
    service = AlertService(config_manager)
    service.initialize()

    # Create Qt application
    app = QApplication(sys.argv)
    app.setApplicationName("CryptoAlertBot")
    app.setApplicationVersion("2.0.0")
    app.setStyle("Fusion")

    # High DPI support
    app.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    app.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    # Create main window
    window = CryptoAlertBotWindow(service)
    window.show()

    # Run
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
