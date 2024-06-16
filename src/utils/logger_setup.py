import logging
from logging.handlers import RotatingFileHandler



# Custom Formatters for colored and plain logging
class ColoredFormatter(logging.Formatter):
    RESET = "\033[0m"
    BOLD = "\033[1m"
    COLORS = {
        "DEBUG": "\033[36m",  # Cyan
        "INFO": "\033[32m",  # Green
        "WARNING": "\033[33m",  # Yellow
        "ERROR": "\033[31m",  # Red
        "CRITICAL": "\033[41m",  # Red background
    }

    def format(self, record):
        color = self.COLORS.get(record.levelname, self.RESET)
        record.levelname = f"{self.BOLD}{color}{record.levelname}{self.RESET}"
        record.msg = f"{self.BOLD}{color}{record.msg}{self.RESET}"
        return super().format(record)


class PlainFormatter(logging.Formatter):
    def format(self, record) -> str:
        return super().format(record)


# Logger class to handle logger setup
class Logger:
    def __init__(self, name: str = "", delete: bool = False) -> None:
        self.logger = logging.getLogger(name)
        self._setup(delete)

    def _setup(self, delete: bool) -> None:
        if delete:
            open("app.log", "w", encoding="utf-8").close()

        if not self.logger.hasHandlers():
            self.logger.setLevel(logging.DEBUG)
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            colored_formatter = ColoredFormatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            plain_formatter = PlainFormatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )

            file_handler = RotatingFileHandler(
                "app.log", maxBytes=5 * 1024 * 1024, backupCount=5
            )
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            console_handler.setFormatter(colored_formatter)
            self.logger.addHandler(console_handler)

            # smtp_handler = SMTPHandler(
            #     mailhost=("smtp.example.com", 587),
            #     fromaddr=formataddr(("Error Logger", "error@example.com")),
            #     toaddrs=["admin@example.com"],
            #     subject="Critical Error Logged",
            #     credentials=("user", "password"),
            #     secure=(),
            # )
            # smtp_handler.setLevel(logging.CRITICAL)
            # smtp_handler.setFormatter(plain_formatter)
            # self.logger.addHandler(smtp_handler)

    def get_logger(self) -> logging.Logger:
        return self.logger


# Logger instances
logger_main_window = Logger("MW").get_logger()
logger_main_controller = Logger("MC").get_logger()
logger_base_model = Logger("BM").get_logger()
logger_eh = Logger("EH").get_logger()
logger_config = Logger("CONFIG").get_logger()
logger_utils = Logger("UTILS").get_logger()
logger_main = Logger("MAIN", delete=True).get_logger()
