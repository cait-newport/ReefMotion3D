# ReefMotion3D
ReefMotion3D leverages Structure from Motion (SfM) to create high-resolution 3D models of coral reefs and fish movements. Our goal is to advance marine research by providing accurate and high-resolution visual data that can aid in the study of coral reef ecosystems, fish behavior, and habitat health.

**Key Features:**

- High-resolution 3D reconstruction of coral reefs
- Detailed modelling of fish species and their movements
- Tools and scripts for SfM processing and analysis
- Data visualization and export options for research purposes
- Comprehensive documentation and tutorials for easy replication and extension

## Tutorial: Getting Started with ReefMotion3D
Learn how to use ReefMotion3D to create high-resolution 3D models of coral reefs and analyze fish movements. This tutorial provides step-by-step instructions and examples to help you get started with the software. Whether you're a marine researcher or an enthusiast, this tutorial will guide you through the process of leveraging Structure from Motion (SfM) technology for studying coral reef ecosystems and fish behavior.

### Step 1: Load requirements file
In the terminal, navigate to your repository folder using cd.
once in the correct folder, create and activate a virtual environment.

```
# In the terminal
cd path/to/ReefMotion3D/
python3 -m venv venv
pip install -r requirements.txt
```

### Step 2: Check folder structure
 This script will check you are in the ReefMotion3D folder. It will also check that a 'tools', 'data', and 'results' folder exist. If it doesnt' they will be automatically made.
 
 ```
 # In the terminal
 python check_folder.py
 ```

### Step 3: Put videos into the 'data' folder following described folder structure
Currently this is in a local folder but would like to make this so it is remote (e.g. RFS, or a different drive).

### Step 3: Sync two videos
#### Find offset between two videos
This is based on audio data within the video. Requires input such as 'trim' which is how much of the video you want to compare. A shorter trim value runs faster but may be less accurate. 

```
cd ReefMotion3D/tools

python audio-stereo-video-sync.py /Users/user/projects/ReefMotion3D/data/2024_02_14/Cait/Left/GX020703.MP4 /Users/user/projects/ReefMotion3D/data/2024_02_14/Cait/Right/GX020029.MP4 40 /Users/user/projects/ReefMotion3D/data/2024_02_14/Cait/offset.txt
```

#### Determines a starting frame for each video
Input should either be manual, or calculated using the find_start_frame.py script. This script is needed to ensure the start frame is always a positive integer.
- Currently inputs are within the script.


#### Extracts frames
- Not tested yet

Videos have been divided into smaller video sections by GoPro. In some cases Rather than  This script allows you to identify multiple videos that 
Example usage: 
main('path/to/your/textfile.txt', 'path/to/output/folder')

### Folder structure

ReefMotion3D/
    tools/
    bs/
        colmap/
        help files/
            .ipynb_checkpoints/
        scripts/
        jupyter/
            GPO/
                examples/
                    .ipynb_checkpoints/
                .ipynb_checkpoints/
            .ipynb_checkpoints/
            tiled_imgs/
            src/
                python-graphslam/
                    images/
                    tests/
                    docs/
                        source/
                            images/
                    scripts/
                    .github/
                        workflows/
                    .git/
                        objects/
                            pack/
                            info/
                        info/
                        logs/
                            refs/
                                heads/
                                remotes/
                                    origin/
                        hooks/
                        refs/
                            heads/
                            tags/
                            remotes/
                                origin/
                    data/
                    graphslam/
                        edge/
                        pose/
                graphslam/
                    images/
                    tests/
                    graphslam.egg-info/
                    docs/
                        source/
                            images/
                    scripts/
                    .github/
                        workflows/
                    .git/
                        objects/
                            pack/
                            info/
                        info/
                        logs/
                            refs/
                                heads/
                                remotes/
                                    origin/
                        hooks/
                        refs/
                            heads/
                            tags/
                            remotes/
                                origin/
                    data/
                    graphslam/
                        __pycache__/
                        edge/
                            __pycache__/
                        pose/
                            __pycache__/
                        .ipynb_checkpoints/
    .git/
        objects/
            66/
            5a/
            ac/
            be/
            e4/
            pack/
            info/
            b8/
            13/
        info/
        logs/
            refs/
                heads/
                remotes/
                    origin/
        hooks/
        refs/
            heads/
            tags/
            remotes/
                origin/