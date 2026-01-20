import os
import zipfile

# Specify the directory containing the ZIP files
zip_dir = './'
# Specify the directory where you want to extract the files
extract_dir = './22e/'

# Create the extraction directory if it doesn't exist
os.makedirs(extract_dir, exist_ok=True)

# Loop through all files in the specified directory
for filename in os.listdir(zip_dir):
    if filename.endswith('.zip'):
        zip_path = os.path.join(zip_dir, filename)
        # Create a folder for each ZIP file
        folder_name = os.path.splitext(filename)[0]
        folder_path = os.path.join(extract_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        # Extract the ZIP file
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(folder_path)
            print(f'Extracted {filename} to {folder_path}')

print('All ZIP files have been extracted.')
