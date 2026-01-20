import os
import sys

def lines(input_data):
    # Split the input into lines and process
    lines = input_data.strip().split('\n')
    output = []
    current_line = ""

    for line in lines:
        if line.strip():  # If the line is not empty
            current_line += ' '
            current_line += line.strip()  # Append the line to the current line
        else:
            if current_line:  # If current_line is not empty, add it to output
                output.append(current_line)
                current_line = ""  # Reset current_line for the next segment

    # Add the last segment if it exists
    if current_line:
        output.append(current_line)

    return output

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 3:
    print("Usage: python script.py input_directory output_directory")
    sys.exit()

# Get input and output directories from command-line arguments
input_directory = sys.argv[1]
output_directory = sys.argv[2]

# Create output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Process each text file in the input directory
for filename in os.listdir(input_directory):
    if filename.lower().endswith('.txt'):
        input_file_path = os.path.join(input_directory, filename)

        try:
            with open(input_file_path, 'r', encoding='utf-8') as text_file:
                input_data = text_file.read()

            # Process the input data to merge lines
            merged_lines = lines(input_data)

            # Create output file path
            output_file_path = os.path.join(output_directory, filename)

            # Write the modified content to the output file
            with open(output_file_path, 'w', encoding='utf-8') as text_file:
                for line in merged_lines:
                    text_file.write(line + '\n')

            print(f"Modified text file saved in {output_file_path}")

        except FileNotFoundError:
            print(f"Error: File '{input_file_path}' not found.")
            continue
        except Exception as e:
            print(f"Error: An unexpected error occurred - {e}")
            continue
