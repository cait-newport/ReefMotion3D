import logging
import subprocess
import sys

import click
from audio_offset_finder.audio_offset_finder import find_offset_between_files
import yaml

# Description: This script is used to find the offset between two audio files.
# 
# Usage:
# 1. Save this script to a file, e.g., audio-stereo-video-sync.py.
# 2. Run the script in the terminal: python audio-stereo-video-sync.py file1 file2 trim_input offset_output
#    Alternatively you can call the function directly in another script.
# 3. Must be in the 'tools' directory
# 
# Example: python audio-stereo-video-sync.py /Users/user/projects/ReefMotion3D/data/2024_02_14/Cait/Left/GX020703.MP4 /Users/user/projects/ReefMotion3D/data/2024_02_14/Cait/Right/GX020029.MP4 40 /Users/user/projects/ReefMotion3D/data/2024_02_14/Cait/offset.txt
#
# Dependencies: 
# - audio_offset_finder
# - ffmpeg
#
# Notes:
# - This script is intended to be run from the command line or imported into another script.
# - The audio_offset_finder package must be installed to use this script.
# - trim_input is the number of seconds to use from the beginning of each audio file. A shorter value can speed up the process.
# Load the function from the audio_offset_finder package

def check_ffmpeg():
    """Check if ffmpeg is installed and available."""

    try:
        subprocess.run(["ffmpeg", "-version"], check=True, capture_output=True)
        logging.info("ffmpeg is installed and available.")
    except FileNotFoundError:
        logging.error("Error: ffmpeg is not installed or not found in the system PATH.")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error while checking ffmpeg installation: {e}")
        sys.exit(1)

def sync_by_audio(filepath1, filepath2, trim_input, offset_output):
    """Find the offset between two audio files.
    Args:
        filepath1 (str): The path to the first audio file.
        filepath2 (str): The path to the second audio file.
        trim_input (float): The number of seconds to use from the beginning of each audio file.
        offset_output (str): The path to save the offset information."""

    # Only use the first n seconds of each audio file
    results = find_offset_between_files(filepath1, filepath2, trim=trim_input)
    # check script is working
    logging.info("sync_by_audio is working")
    # TODO: warning for very poor sync
    # Print the offset between the two videos
    logging.info("Offset between videos: {} (seconds)".format(str(results["time_offset"])))
    logging.info("Frame offset: %s" % str(results["frame_offset"]))
    logging.info("Standard score: %s" % str(results["standard_score"]))
    # Add a warning if the standard score is very low
    if results["standard_score"] < 10:
        logging.info("Warning: The standard score is very low, indicating poor synchronization")

    # Save the offset to a YAML file
    try:
        # Attempt to open and write to the file
        with open(offset_output, "w") as file:
            yaml.dump({
                "Time Offset": float(results["time_offset"]),
                "Frame Offset": int(results["frame_offset"]),
                "Standard Score": float(results["standard_score"]),
            }, file)
        logging.info(f"Successfully wrote to {offset_output}")
    except Exception as e:
        logging.error(f"Error writing to file: {e}")

@click.command()
@click.argument('file1', type=click.Path(exists=True))
@click.argument('file2', type=click.Path(exists=True))
@click.argument('trim_input', type=float)
@click.argument('offset_output', type=click.Path())

def main(file1, file2, trim_input, offset_output):
    """Script to find the offset between two audio files."""
    check_ffmpeg()
    sync_by_audio(file1, file2, trim_input, offset_output)

if __name__ == "__main__":
    main()
