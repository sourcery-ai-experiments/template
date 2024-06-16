from pathlib import Path
from typing import Any, Optional

import yaml

from src.utils.logger_setup import logger_config as logger


from src.utils.logger_setup import logger_config as logger


class Config:
    """Manages the application's configuration file.

    This class provides methods to create, read, and update a YAML configuration file.

    Attributes
    ----------
    config_path : Path
        The path to the configuration file.
    config : dict
        The loaded configuration data.
    """

    def __init__(self, config_file: str = "config.yaml") -> None:
        """Initialize the Config class.

        Args:
            config_file (str, optional): The name of the configuration file. Defaults to "config.yaml".
        """

        logger.info("Initializing Config")

        self.config_path = Path(config_file)

        if not self.config_path.is_absolute():
            self.config_path = Path(__file__).resolve().parent / config_file

        self.load_config()

    def load_config(self) -> None:
        """Load the configuration data from the YAML file."""

        logger.info("Loading configuration")

        if not self.config_path.exists():
            self.create_default_config()
        else:
            with open(self.config_path, "r", encoding="utf-8") as file:
                self.config = yaml.safe_load(file)

    def create_default_config(self) -> None:
        """Create a default configuration file if it doesn't exist."""

        logger.info("Creating default configuration")

        default_config = {"Settings": {}, "Shortcuts": {}}

        with open(self.config_path, "w", encoding="utf-8") as file:
            yaml.safe_dump(default_config, file)
        self.config = default_config

    def get_value(self, section: str, setting: str) -> Optional[Any]:
        """Retrieve the value of a specific setting from the configuration.

        Args:
            section (str): The section name in the configuration.
            setting (str): The setting name within the specified section.

        Returns:
            Optional[Any]: The value of the requested setting, or None if the section or setting is not found.
        """

        logger.info("Getting value for %s/%s", section, setting)

        section_config = self.config.get(section, {})
        logger.debug("Getting value for %s/%s: %s", section, setting, section_config.get(setting))
        return section_config.get(setting)

    def set_value(self, section: str, setting: str, value: Any) -> None:
        """Set the value of a specific setting in the configuration.

        Args:
            section (str): The section name in the configuration.
            setting (str): The setting name within the specified section.
            value (Any): The value to set for the specified setting.
        """
        self.config.setdefault(section, {})[setting] = value
        self.save_config()

    def save_config(self) -> None:
        """Save the configuration data to the YAML file."""
        with open(self.config_path, "w", encoding="utf-8") as file:
            yaml.safe_dump(self.config, file, default_flow_style=False)
