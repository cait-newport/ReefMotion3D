from audio_offset_finder.audio_offset_finder import find_offset_between_files
import os
import sys
import subprocess

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
    try:
        subprocess.run(["ffmpeg", "-version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("ffmpeg is installed and available.")
    except FileNotFoundError:
        print("Error: ffmpeg is not installed or not found in the system PATH.")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print("Error while checking ffmpeg installation:", e)
        sys.exit(1)

def check_files_exist(filepath1, filepath2):
    if not os.path.exists(filepath1):
        print(f"Error: The file '{filepath1}' does not exist.")
        sys.exit(1)
    if not os.path.exists(filepath2):
        print(f"Error: The file '{filepath2}' does not exist.")
        sys.exit(1)


def sync_by_audio(filepath1, filepath2, trim_input, offset_output):
    # Only use the first n seconds of each audio file
    results = find_offset_between_files(filepath1, filepath2, trim=trim_input)
    # check script is working
    print("sync_by_audio is working")
    # TODO: warning for very poor sync
    # Print the offset between the two videos
    print("Offset between videos: %s (seconds)" % str(results["time_offset"]))
    print("Frame offset: %s" % str(results["frame_offset"]))
    print("Standard score: %s" % str(results["standard_score"]))
    # Add a warning if the standard score is very low
    if results["standard_score"] < 10:
        print("Warning: The standard score is very low, indicating poor synchronization")
    
    # Save the offset to a text file
    try:
        # Attempt to open and write to the file
        with open(offset_output, "w") as file:
            file.write(f"Time Offset: {str(results['time_offset'])}\n")
            file.write(f"Frame Offset: {str(results['frame_offset'])}\n")
            file.write(f"Standard Score: {str(results['standard_score'])}\n")
        print(f"Successfully wrote to {offset_output}")
    except Exception as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    check_ffmpeg()
    
    if len(sys.argv) != 5:
        print("Usage: python audio-stereo-video-sync.py <file1> <file2> <trim_input> <offset_output>")
    else:
        filepath1 = sys.argv[1]
        filepath2 = sys.argv[2]
        trim_input = float(sys.argv[3])
        offset_output = sys.argv[4]
        check_files_exist(filepath1, filepath2)
        sync_by_audio(filepath1, filepath2, trim_input, offset_output)
