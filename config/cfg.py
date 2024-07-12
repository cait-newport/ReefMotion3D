"""
Data to be shared across files.
"""

import logging
from pathlib import Path

# Config location
CONFIG_DIR = Path(__file__).resolve().parent
PREPROCESS_CONFIG = CONFIG_DIR / "preprocess_config.yaml"

# Preprocessing configuration
ROOT_FILENAME = "ReefMotion3D"
ROOT_FILEPATH = CONFIG_DIR.parent

# Logging format
LOG_FILENAME = "reefmotion3d.log"
LOGGING_FMT = "%(asctime)s - %(levelname)s - %(message)s"
LOGGING_DATE_FMT = "%d-%b-%y %H:%M:%S"

def setup_logging():
    logging.basicConfig(format=LOGGING_FMT, datefmt=LOGGING_DATE_FMT)
    logging.getLogger().setLevel(logging.INFO)
    formatter = logging.Formatter(LOGGING_FMT, datefmt=LOGGING_DATE_FMT)
    file_handler = logging.FileHandler(str(ROOT_FILEPATH / LOG_FILENAME))
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logging.getLogger().addHandler(file_handler)
