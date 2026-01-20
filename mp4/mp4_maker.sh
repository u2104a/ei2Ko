#!/bin/bash

# Check if the correct number of command-line arguments is provided
if [ "$#" -ne 5 ]; then
    echo "Usage: $0 input_directory output_directory pptx_file_path move_directory dump_directory"
    exit 1
fi

input_directory="$1"
output_directory="$2"
pptx_file_path="$3"
move_directory="$4"
dump_directory="$5"

# Create output, move, and dump directories if they don't exist
mkdir -p "$output_directory" "$move_directory" "$dump_directory"

# Process each MP3 file in the input directory
for mp3_file in "$input_directory"/*.mp3; do
    if [ -f "$mp3_file" ]; then
        # Extract filename without extension
        file_name=$(basename -- "$mp3_file")
        file_name_no_ext="${file_name%.*}"

        # Extract information from the MP3 filename
        IFS='-' read -r -a ad <<< "$file_name_no_ext"
        text_replacer="${ad[0]} to ${ad[1]}"

        # Define the output MP4 file path and dump PPTX file path
        mp4_file="$output_directory/$file_name_no_ext.mp4"
        
        pptx_filename=$(basename -- "$pptx_file_path")
        pptx_file_name_no_ext="${pptx_filename%.*}"
        dump_ppt_file="$dump_directory/$pptx_file_name_no_ext.pptx"

        # PPTX Correction
        if python3 -m python_pptx_text_replacer.TextReplacer -m 'XXXXxXXXX' -r "$text_replacer" -i "$pptx_file_path" -o "$dump_ppt_file" >/dev/null 2>&1; then
            echo ">> PPTX Correction DONE <<"

            # PPTX to JPEG Conversion
            if libreoffice --convert-to jpg "$dump_ppt_file" --outdir "$dump_directory" >/dev/null 2>&1; then
                echo ">> PPTX to JPEG Conversion [ DONE ] <<"

                # Define paths for MP4 creation
                image_path="$dump_directory/$pptx_file_name_no_ext.jpg"
                audio_path="$mp3_file"
                output_mp4_path="$mp4_file"

                # MP4 Creation
                if time python3 revise_mp4_maker.py "$image_path" "$audio_path" "$output_mp4_path" "1" >/dev/null 2>&1; then
                    echo ">> Mp4 Creation <$text_replacer> [ DONE ] <<"
                    mv "$mp3_file" "$move_directory"
                    rm -rf "$dump_directory"
                    #** bash send_message.sh "Super Gene Remake $file_name_no_ext by @a1b_d1"
                else
                    echo ">> ERROR in 'Mp4 Creation <$text_replacer>' <<"
                fi
            else
                echo ">> ERROR in 'PPTX to JPEG Conversion' <<"
            fi
        else
            echo ">> ERROR in 'PPTX Correction' <<"
        fi
    else
        echo ">> No MP3 files found in $input_directory <<"
    fi
done

# Optionally clean up the dump directory if needed
# rm -rf "$dump_directory"
