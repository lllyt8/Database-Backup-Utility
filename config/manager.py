import os
import yaml

class ConfigManager:
    def __init__(self, config_file=None):
        self.config_file = config_path or os.path.expanduser("~/.dbbackup/config.yaml")

    def load(self):
        """Load configuration from the specified file."""
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Configuration file not found: {self.config_file}")
