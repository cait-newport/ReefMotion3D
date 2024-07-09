# Description: This script sets the root directory of the project and checks that folders are in place. 
# If folders are missing, they are created.

import os

def check_and_create_folders():
    # Get the current working directory
    current_directory = os.getcwd()
    
    # Define the parent folder name
    parent_folder_name = 'ReefMotion3D'
    
    # Define the full path for the parent folder
    parent_folder_path = os.path.join(current_directory, parent_folder_name)
    
    # Create the parent folder if it doesn't exist
    if not os.path.exists(parent_folder_path):
        os.makedirs(parent_folder_path)
        print(f"Created parent folder: {parent_folder_path}")
    else:
        print(f"Parent folder already exists: {parent_folder_path}")
    
    # Define the folders to check within the parent folder
    folders = ['tools', 'data', 'results']
    
    for folder in folders:
        folder_path = os.path.join(parent_folder_path, folder)
        
        # Check if the folder exists, if not, create it
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")
        else:
            print(f"Folder already exists: {folder_path}")

if __name__ == "__main__":
    check_and_create_folders()

