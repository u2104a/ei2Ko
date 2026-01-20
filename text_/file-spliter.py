import os
import sys
import glob
import shutil

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 3:
    print('Usage: python script.py input_directory "<number of splits>"')
    sys.exit(1)

# Assign the arguments to variables
input_directory = str(sys.argv[1])

condition = int(sys.argv[2])

# Use glob to find all .txt files in the input directory
text_files = sorted(glob.glob(os.path.join(input_directory, '*.txt')))

# Check if there are any text files to process
if not text_files:
    print(f"No text files found in the input directory: {input_directory}")
    sys.exit(0)

# If there are text files, process and move them
print(f"Found {len(text_files)} text files to process.")

bit = 0

for text_file in text_files:
    bit += 1

    # Create a subdirectory based on the bit counter
    destination_directory = os.path.join(input_directory, str(bit))
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Create output file path
    filename = os.path.basename(text_file)
    output_file_path = os.path.join(destination_directory, filename)

    # Move the file to the destination directory
    shutil.move(text_file, output_file_path)
#    print(f"Moved {text_file} to {output_file_path}"/end="\r")
    print(f"Moved {text_file} to {output_file_path}", end="\r", flush=True)
    # Reset the counter after every 4 files
    if bit == condition:
        bit = 0

