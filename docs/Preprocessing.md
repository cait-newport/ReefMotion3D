# Preprocessing

## Step 1: Load requirements file
In the terminal, navigate to your repository folder using cd.
once in the correct folder, create and activate a virtual environment.

```
# In the terminal
cd path/to/ReefMotion3D/
python3 -m venv venv
pip install -r requirements.txt
```

## Step 2: Check folder structure
 This script will check you are in the ReefMotion3D folder. It will also check that a 'tools', 'data', and 'results' folder exist. If it doesnt' they will be automatically made.
 
 ```
 # In the terminal
 python check_folder.py
 ```

## Step 3: Put videos into the 'data' folder following described folder structure
Currently this is in a local folder but would like to make this so it is remote (e.g. RFS, or a different drive).

## Step 4: Sync two videos
### 4a: Find offset between two videos
This is based on audio data within the video. Requires input such as 'trim' which is how much of the video you want to compare. A shorter trim value runs faster but may be less accurate. 

```
cd ReefMotion3D/tools

python audio-stereo-video-sync.py /Users/user/projects/ReefMotion3D/data/2024_02_14/Cait/Left/GX020703.MP4 /Users/user/projects/ReefMotion3D/data/2024_02_14/Cait/Right/GX020029.MP4 40 /Users/user/projects/ReefMotion3D/data/2024_02_14/Cait/offset.txt
```

### 4b: Determines a starting frame for each video
Input should either be manual, or calculated using the find_start_frame.py script. This script is needed to ensure the start frame is always a positive integer.
- Currently inputs are within the script.


### 4c: Extracts frames
- Not tested yet

Videos have been divided into smaller video sections by GoPro. In some cases Rather than  This script allows you to identify multiple videos that 
Example usage: 
main('path/to/your/textfile.txt', 'path/to/output/folder')
