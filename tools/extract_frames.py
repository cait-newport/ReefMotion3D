import os
import ffmpeg

# Example usage
#extract_frames_from_video('path/to/your/textfile.txt', 'path/to/output/folder')

#Example text file format
#path/to/video1.mp4 0 100
#path/to/video2.mp4 50 150

# TODO: Add error handling for invalid input
# TODO: make a list of videos to group together. Make it so frame numbers add on for each video in the group. 
# TODO: split this into two functions, one to read the text file and one to extract the frames



def extract_frames_from_video(text_file_path, output_folder):
    # Read the text file
    with open(text_file_path, 'r') as file:
        lines = file.readlines()

    # Process each line in the text file
    for line in lines:
        parts = line.strip().split()
        if len(parts) != 3:
            print(f"Invalid line format: {line}")
            continue

        video_path, start_frame, end_frame = parts
        start_frame = int(start_frame)
        end_frame = int(end_frame)

        # Ensure the output folder exists
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Extract the frames using ffmpeg
        output_pattern = os.path.join(output_folder, f"{os.path.basename(video_path)}_%04d.png")
        (
            ffmpeg
            .input(video_path, ss=start_frame, to=end_frame)
            .output(output_pattern, start_number=start_frame, vframes=end_frame - start_frame + 1)
            .run()
        )

        print(f"Extracted frames {start_frame} to {end_frame} from {video_path} to {output_pattern}")

if __name__ == "__main__":
    extract_frames_from_video("frames.txt", "frames")
