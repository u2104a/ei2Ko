# ei2Ko

## all code were created between Jan 2020 to Nov 2025

### for Text files

- **ch-char-checker.py**
>- **Search :** Scans all .txt files in a given directory for Chinese characters.
>- **Report :** Lists any files containing such characters.
>- **Move :** If desired, allows the user to relocate those files to a specified folder.

- **convert_html_to_text.py**
>- **Conversion :** Reads all HTML or XHTML files in a specified input directory and converts their content to plain text using the `html2text` library.
>- **Error Handling :** Catches and reports errors related to file access and conversion issues.
>- **Output :** Saves the converted plain text files to a specified output directory, preserving the original file names but changing the extension to `.txt`.
>- **Directory Management :** Automatically creates the output directory if it doesn't already exist, ensuring a seamless conversion process.

- **file-spliter.py**
>- **File Organization :** Scans a specified input directory for all .txt files and organizes them into subdirectories.
>- **Subdirectory Creation :** Uses a counter to create separate subdirectories (named numerically) for every set of files moved, with the number of splits defined by the user.
>- **File Movement :** Moves the found text files into their respective subdirectories, resetting the counter after reaching the defined number of splits.
>- **User Feedback :** Provides real-time feedback on the movement of files, indicating the source and destination paths.

- **lineMerge.py**
>- **Input Processing :** Reads all .txt files from a specified input directory and merges consecutive non-empty lines into single lines, removing unnecessary line breaks.
>- **Output Generation :** Saves the modified content to new .txt files in a specified output directory, preserving the original filenames.
>- **Error Handling :** Catches and reports errors related to file access, such as missing files or unexpected issues during processing.
>- **Directory Management :** Ensures the output directory exists, creating it if necessary, to facilitate smooth file writing.

- **translate_text.py**
>- **Translation :** Reads .txt files from a specified input directory, translates their content from Chinese to English using the translators library, and saves the results to an output directory.
>- **Chunk Processing :** Splits large texts into manageable chunks (up to 4990 characters) to facilitate smoother translation.
>- **Error Logging :** Logs any errors encountered during translation or file processing for debugging and record-keeping.
>- **Directory Management :** Creates specified output and move directories if they don't exist, and moves processed files to a designated directory after translation.
>- **User Feedback :** Provides real-time logging to track the translation progress and any encountered issues.

### for Image

- **barcode.sh**
>- **QR Code Generation :** Utilizes qrencode to generate a QR code from a specified URL, customizing the foreground and background colors.
>- **Success Verification :** Checks the success of the QR code generation process and provides feedback, indicating whether the QR code was generated successfully or if the process failed.

