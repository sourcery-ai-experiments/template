# src/views/main_window.py

from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from src.utils.logger_setup import logger_main_window as logger

class MainWindow(QMainWindow):
    def __init__(self, main_controller, config) -> None:
        super().__init__()
        self.main_controller = main_controller
        self.config = config

        self.init_ui()

    def init_ui(self) -> None:
        # Set up the main window
        self.setWindowTitle("Template Application")
        self.setGeometry(0, 0, 800, 600)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout(self.centralWidget)