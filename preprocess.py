"""
A script to perform preprocessing on the video data.
"""

import logging

from config import cfg
from tools import check_folders

# Set up logging
cfg.setup_logging()


def preprocess():
    # Check the working directory and create the necessary folders
    check_folders.check_and_create_folders()


if __name__ == "__main__":
    preprocess()
    logging.info("Preprocessing complete.")
