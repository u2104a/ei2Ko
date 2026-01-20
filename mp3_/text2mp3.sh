#!/bin/bash

# Check if the correct number of command-line arguments is provided
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 input_directory output_directory move_directory"
    exit 1
fi

input_directory="$1"
output_directory="$2"
move_directory="$3"

# Check if input directory exists
if [ ! -d "$input_directory" ]; then
    echo "Error: Input directory does not exist: $input_directory"
    exit 1
fi

# Create output directory if it doesn't exist
mkdir -p "$output_directory"

# Create move directory if it doesn't exist
mkdir -p "$move_directory"

voice_1='en-HK-YanNeural' # Ensure this is the correct voice name

# Check if there are any text files to process
shopt -s nullglob
text_files=("$input_directory"/*.txt)
if [ ${#text_files[@]} -eq 0 ]; then
    echo "No text files found in the input directory: $input_directory"
    exit 0
fi

# Process each text file in the input directory
for text_file in "${text_files[@]}"; do
    if [ -f "$text_file" ]; then
        # Extract filename without extension
        file_name=$(basename -- "$text_file")
        file_name_no_ext="${file_name%.*}"

        # Define the output MP3 file path
        mp3_file="$output_directory/$file_name_no_ext.mp3"

        # Use edge-tts to convert text file to MP3
        if time edge-tts -v "$voice_1" -f "$text_file" --write-media "$mp3_file" >/dev/null 2>&1; then
            printf "Conversion successful. MP3 saved in %s as %s.\n" "$output_directory" "$file_name_no_ext.mp3"

            # Move the processed text file to the specified move_directory
            mv "$text_file" "$move_directory"
            bash send_message.sh -1002136069032 "<pill sovereign martial emperor> $file_name_no_ext mp3 COMPLETED converted by @a1b_d1"
            date

        else
            printf "Error during conversion for file: %s. Please check your input file.\n" "$text_file"
        fi
    else
        printf "Error: Text file does not exist: %s\n" "$text_file"
    fi
done
