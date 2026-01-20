import os
import shutil

def move_files_to_current_directory():
    # Get the current working directory
    current_directory = os.getcwd()

    # Walk through all subdirectories and files
    for root, dirs, files in os.walk(current_directory):
        for file in files:
            # Construct full file path
            file_path = os.path.join(root, file)

            # Skip if the file is already in the current directory
            if root != current_directory:
                # Move the file to the current directory
                shutil.move(file_path, current_directory)
                print(f'Moved: {file_path} to {current_directory}')

if __name__ == "__main__":
    move_files_to_current_directory()
