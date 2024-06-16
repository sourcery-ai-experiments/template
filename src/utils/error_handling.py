from src.utils.logger_setup import logger_eh
from PySide6.QtWidgets import QMessageBox, QApplication


def handle_and_log_error(
    status_message: str, parent: object, error: str, log_message: str
) -> None:
    """Handle and log an error by showing a message box and logging the error.

    This function logs the provided error message and log message, and displays
    an error message box with the status message and error.

    Args:
    ----
    status_message : str
        The status message to be displayed.
    parent : object
        The parent widget (can be None if not used).
    error : str
        The error message to be displayed and logged.
    log_message : str
        The log message to be logged.

    Returns:
    -------
    None
    """
    # Fehlerprotokollierung
    logger_eh.error("%s: %s", log_message, error)

    # Aktives Fenster als Eltern-Widget verwenden, falls kein Eltern-Widget angegeben ist
    if parent is None:
        parent = QApplication.activeWindow()

    # Fehlermeldung anzeigen
    QMessageBox.critical(parent, "Fehler", f"{status_message}: {error}")

    # Zusätzliche Fehlerprotokollierung mit Ausnahmeinformationen
    logger_eh.error("Exception occurred", exc_info=True)
