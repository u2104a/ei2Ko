import os
import tarfile
import argparse

# Set up argument parsing
parser = argparse.ArgumentParser(description='Create tar.gz files.')
parser.add_argument('start', type=int, help='Start value')
parser.add_argument('end', type=int, help='End value')
parser.add_argument('difference', type=int, help='Difference value')
parser.add_argument('outdir', type=str, help='Output Directory')
parser.add_argument('indir', type=str, help='Input Directory')

# Parse the arguments
args = parser.parse_args()

# Assign the arguments to variables
start = args.start
end = args.end
difference = args.difference
outdir = args.outdir
indir = args.indir

# Create output directory if it doesn't exist
os.makedirs(outdir, exist_ok=True)

# Define the command components
file_extension = '.mp3'

def create_tar_gz(tar_gz_filename, files_to_archive):
    # Create a new tar.gz file
    with tarfile.open(tar_gz_filename, 'w:gz') as tar:
        for file in files_to_archive:
            # Check if the file exists
            if os.path.exists(file):
                # Add file to the tar.gz file
                tar.add(file, arcname=os.path.basename(file))
            else:
                print(f"File {file} does not exist and will be skipped.")

    print(f"Created tar.gz file: {tar_gz_filename}")

for mid in range(start, end + 1, difference):  # Adjusted to include end
    # Create a list to hold valid file names
    valid_files = []
    
    for sub in range(mid, mid + difference):
        if sub <= end:  # Check if the file number is within the valid range
            valid_files.append(os.path.join(indir, f'{sub:04}{file_extension}'))

    if valid_files:  # Only proceed if there are valid files
        tar_gz_filename = os.path.join(outdir, f'{mid:04}-{min(mid + difference - 1, end):04}.tar.gz')
        create_tar_gz(tar_gz_filename, valid_files)
