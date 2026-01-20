# importing python module
# `pip install html2text`
# [https://pypi.org/project/html2text/]

import os
import html2text
import sys

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 3:
    print("Usage: python script.py input_directory output_directory")
    sys.exit(1)

# Get input and output directories from command-line arguments
input_directory = sys.argv[1]
output_directory = sys.argv[2]

# Create output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Process each HTML or XHTML file in the input directory
for filename in os.listdir(input_directory):
    if filename.lower().endswith(('.html', '.htm', '.xhtml', '.xhtm')):
        input_file_path = os.path.join(input_directory, filename)

        try:
            with open(input_file_path, 'r', encoding='utf-8') as rt:
                html_content = rt.read()
        except FileNotFoundError:
            print(f"Error: File '{input_file_path}' not found.")
            continue
        except Exception as e:
            print(f"Error: An unexpected error occurred - {e}")
            continue

        # Create an instance of HTML2Text
        h = html2text.HTML2Text()

        # Ignore links in the HTML content
        h.ignore_links = True

        # Convert HTML to plain text
        try:
            plain_text = h.handle(html_content)
        except Exception as e:
            print(f"Error: An error occurred during HTML to text conversion - {e}")
            continue

        # Create output directory for plain text files if it doesn't exist
        # output_directory = os.path.join(output_directory, 'txt')
        
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Create output file path
        output_file_path = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}.txt")

        # Write plain text to the output file
        with open(output_file_path, 'w', encoding='utf-8') as text_file:
            text_file.write(plain_text)

        print(f"Conversion successful. Plain text saved in {output_file_path}")
