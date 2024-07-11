"""
Description: This script checks that it is being run from the correct location and then
checks that folders are in place.
If folders are missing, they are created.
"""

import logging
import sys
from pathlib import Path

from config import cfg

# Define the folders to check within the parent folder
FOLDERS = ["data", "results"]
CWD = Path.cwd()

def check_and_create_folders(parent_folder_path=cfg.ROOT_FILEPATH):

    # Check if the current working directory is the parent folder
    if parent_folder_path != CWD:
        msg = (f"Please run this script from the parent folder: {parent_folder_path}. "
               f"Current working directory: {CWD}")
        logging.error(msg)
        sys.exit(1)

    for folder in FOLDERS:
        folder_path = parent_folder_path / folder

        # Check if the folder exists, if not, create it
        if not folder_path.exists():
            folder_path.mkdir(parents=True)
            logging.info(f"Folder created: {folder_path}")
        else:
            logging.info(f"Folder found: {folder_path}")


if __name__ == "__main__":
    check_and_create_folders()
