# src.controller/main_controller.py
from src.views.main_window import MainWindow

class MainController:
    def __init__(self, app, config) -> None:
        self.app = app
        self.config = config
        self.base_model = None
        self.main_window = MainWindow(self,self.config)



    def run(self) -> None:
        self.main_window.show()

