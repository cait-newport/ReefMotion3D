# Description: This script reads the offset.txt file in a folder and extracts the frame offset value.
# If one video is ahead of the other, it will return the start frame for each video, while ensuring the frame numbers are positive.
# The start frame values are appended to the run_file.txt file in the same folder.

# Usage: Call the function find_start_frame(folder_path) with the path to the folder containing the offset.txt file.
# Dependencies: None
# Notes: This script assumes the offset.txt file is in the expected format.


def find_start_frame(folder_path):
    import os
    
    # Path to the offset file
    offset_file_path = os.path.join(folder_path, 'offset.txt')
    run_file_path = os.path.join(folder_path, 'run_file.txt')
    
    try:
        with open(offset_file_path, 'r') as file:
            lines = file.readlines()
            # Extract the frame offset from the second line
            frame_offset_line = lines[1].strip()
            frame_offset = int(frame_offset_line.split(":")[1].strip())
    except FileNotFoundError:
        raise FileNotFoundError(f"The file offset.txt was not found in the folder path: {folder_path}")
    except (ValueError, IndexError):
        raise ValueError("The offset value in offset.txt is not in the expected format.")
    
    if frame_offset < 0:
        video1_start_frame = abs(frame_offset) + 1
        video2_start_frame = 1
    else:
        video1_start_frame = 1
        video2_start_frame = frame_offset + 1
    
    # Append results to run_file.txt
    with open(run_file_path, 'a') as run_file:
        run_file.write(f"Left start frame: {video1_start_frame}\n")
        run_file.write(f"Right start frame: {video2_start_frame}\n")
    
    return video1_start_frame, video2_start_frame

# Example usage
folder_path = "/Users/user/projects/ReefMotion3D/data/2024_02_14/Cait/"
video1_start, video2_start = find_start_frame(folder_path)
print(f"Video 1 start frame: {video1_start}, Video 2 start frame: {video2_start}")
