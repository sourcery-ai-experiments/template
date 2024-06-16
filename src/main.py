import sys

from PySide6.QtWidgets import QApplication
from src.controllers.main_controller import MainController
from src.utils.config import Config
from src.utils.error_handling import handle_and_log_error
from src.utils.exceptions import MyCustomError
from src.utils.logger_setup import logger_main as logger


def main() -> None:
    logger.info("Starting main")

    app = QApplication(sys.argv)

    config = Config()

    main_controller = MainController(app, config)
    main_controller.run()

    sys.exit(app.exec())


if __name__ == "__main__":
    try:
        main()
    except MyCustomError as e:
        handle_and_log_error(
            "An error occurred while running the application",
            e,
            str(e),
            "An error occurred while running the application",
        )
    except Exception as e:
        logger.critical("An unexpected error occurred: %s", e)
        sys.exit(1)
