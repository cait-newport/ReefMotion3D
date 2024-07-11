import os
import ffmpeg

# Description: This script reads a text file containing video file paths and frame ranges, and extracts the frames from the videos.
# The frame ranges are continuous, and the extracted frames are saved as PNG images in the specified output folder.
# Usage: Call the main function with the path to the text file and the output folder.
# Dependencies: ffmpeg-python
# Notes: This script assumes the text file is in the expected format.

# Example text file format:
# video1.mp4 video2.mp4 0 100
# video3.mp4 50 150

def read_video_parts(text_file_path):
    try:
        with open(text_file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file {text_file_path} was not found.")
        return None
    except Exception as e:
        print(f"Error reading file {text_file_path}: {e}")
        return None

    video_parts_info = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) < 4:
            print(f"Invalid line format: {line}")
            continue

        video_parts = parts[:-2]
        start_frame = parts[-2]
        end_frame = parts[-1]

        try:
            start_frame = int(start_frame)
            end_frame = int(end_frame)
            if start_frame < 0 or end_frame < 0 or end_frame < start_frame:
                print(f"Invalid frame range: {line}")
                continue
        except ValueError:
            print(f"Invalid frame numbers: {line}")
            continue

        for video_path in video_parts:
            if not os.path.exists(video_path):
                print(f"Error: The video file {video_path} does not exist.")
                continue

        video_parts_info.append((video_parts, start_frame, end_frame))

    return video_parts_info

def extract_continuous_frames(video_parts, start_frame, end_frame, output_folder):
    if not os.path.exists(output_folder):
        try:
            os.makedirs(output_folder)
        except Exception as e:
            print(f"Error creating output folder {output_folder}: {e}")
            return

    current_frame = start_frame
    for video_path in video_parts:
        input_args = {
            'ss': 0,
            'to': end_frame - start_frame + 1
        }
        output_pattern = os.path.join(output_folder, f"{os.path.basename(video_path)}_%04d.png")
        try:
            (
                ffmpeg
                .input(video_path, **input_args)
                .output(output_pattern, start_number=current_frame, vframes=end_frame - start_frame + 1)
                .run()
            )
            print(f"Extracted frames from {video_path} to {output_pattern}")
        except ffmpeg.Error as e:
            print(f"ffmpeg error for video {video_path}: {e}")
        except Exception as e:
            print(f"Error processing video {video_path}: {e}")

        # Update the current frame for the next part
        current_frame += end_frame - start_frame + 1

def main(text_file_path, output_folder):
    video_parts_info = read_video_parts(text_file_path)
    if video_parts_info is None:
        return

    for video_parts, start_frame, end_frame in video_parts_info:
        extract_continuous_frames(video_parts, start_frame, end_frame, output_folder)

# Example usage
main('path/to/your/textfile.txt', 'path/to/output/folder')
