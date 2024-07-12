"""
A script to perform preprocessing on the video data.
"""

import logging

import yaml
from config import cfg
from tools.preprocess import audio_stereo_video_sync

# Set up logging
cfg.setup_logging()


def preprocess():
    logging.debug("Checking the ffmpeg installation")
    audio_stereo_video_sync.check_ffmpeg()

    # Read the configuration file
    logging.debug("Reading the configuration file")
    with open(cfg.PREPROCESS_CONFIG) as file:
        config = yaml.safe_load(file)

    # Extract the necessary information
    left_video_path = config['left_video']
    right_video_path = config['right_video']
    trim_input = config['trim_input']
    offset_file = config['offset_file']

    # Call the sync_by_audio function with the extracted information
    logging.debug("Calculating offset between videos using audio")
    audio_stereo_video_sync.sync_by_audio(
        left_video_path,
        right_video_path,
        trim_input,
        offset_file
    )


if __name__ == "__main__":
    preprocess()
    logging.info("Preprocessing complete.")
