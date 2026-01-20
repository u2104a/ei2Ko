import os
import sys
import re
import shutil

def contains_chinese_characters(text):
    # Regular expression to match Chinese characters
    return re.search(r'[\u4e00-\u9fff]', text) is not None

def find_txt_files_with_chinese_characters(folder_path):
    # List to store files with Chinese characters
    files_with_chinese = []

    # Walk through the directory
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if contains_chinese_characters(content):
                            files_with_chinese.append(file_path)
                except (UnicodeDecodeError, FileNotFoundError) as e:
                    print(f"Error reading {file_path}: {e}")

    return files_with_chinese

def move_files(files, destination_folder):
    # Create the destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)
    
    for file in files:
        try:
            shutil.move(file, destination_folder)
            print(f"Moved: {file} to {destination_folder}")
        except Exception as e:
            print(f"Error moving {file}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python find_chinese_txt.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    result = find_txt_files_with_chinese_characters(folder_path)
    result.sort()
    
    if result:
        print("Files containing Chinese characters:")
        for file in result:
            print(file)
        
        move_option = input("Do you want to move these files to a new folder? (yes/no): ").strip().lower()
        if move_option in ['yes','y']:
            new_folder_name = input("Enter the name of the new folder: ").strip()
            destination_folder = os.path.join(folder_path, new_folder_name)
            move_files(result, destination_folder)
    else:
        print("No files containing Chinese characters found.")
