class MyCustomError(Exception):
    """Custom exception for specific error cases.

    This class is used to raise custom exceptions with a specific message.

    Attributes
    ----------
    message : str
        The error message associated with the exception.

    Methods
    -------
    __str__()
        Returns a string representation of the error.

    """

    def __init__(self, message: str) -> None:
        """Initialize the MyCustomError class.

        Args:
        ----
        message : str
            The error message associated with the exception.

        """
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        """Return a string representation of the error.

        Returns
        -------
        str
            A string representation of the error message.

        """
        return f"MyCustomError: {self.message}"


class InvalidParentError(MyCustomError):
    """Exception raised for invalid parent errors.

    This exception is used when an invalid parent is encountered for a new item.
    """

    def __init__(self, message: str = "Invalid parent for new item") -> None:
        """Initialize the InvalidParentError class.

        Args:
        ----
        message : str, optional
            The error message associated with the exception. Defaults to "Invalid parent for new item".

        """
        super().__init__(message)


class FileOperationError(MyCustomError):
    """Exception raised for file operation errors.

    This exception is used when an error occurs during a file operation.
    """

    def __init__(self, message: str = "An error occurred during file operation") -> None:
        """Initialize the FileOperationError class.

        Args:
        ----
        message : str, optional
            The error message associated with the exception. Defaults to "An error occurred during file operation".

        """
        super().__init__(message)
