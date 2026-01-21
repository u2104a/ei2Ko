# ei2Ko

## all code were created between Jan 2020 to Nov 2025

---

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

---

### for Image

- **barcode.sh**
>- **QR Code Generation :** Utilizes qrencode to generate a QR code from a specified URL, customizing the foreground and background colors.
>- **Success Verification :** Checks the success of the QR code generation process and provides feedback, indicating whether the QR code was generated successfully or if the process failed.

---

### for Mp3

- **mp3-merge.py**
> This **Python** script *is designed to process MP3 files in a specified directory by merging them into segments based on their durations, sending notifications through a Telegram bot upon successful merging.*
>- **Directory Structure:** The script creates an output directory to store merged MP3 files.
>- **MP3 Duration Calculation:** It retrieves the duration of each MP3 file using `moviepy`.
>- **Merging Logic:** MP3 files are merged continuously until the total duration reaches 11 hours and 30 minutes, sending a notification for each successful merge.
>- **Telegram Notifications:** Sends messages to a specified Telegram chat upon completion of each merge, indicating success and time taken for the operation.
>- **Command Execution:** Utilizes `subprocess` to run the `sox` command for audio processing.

- **text2mp3withSRT.py**
>This **Python** script *converts text files into MP3 audio files and corresponding SRT subtitle files using the* `edge_tts` *library, while also sending notifications through a Telegram bot.*
>- **Directory Structure:** The script organizes files by creating an output directory for MP3 and SRT files, as well as a separate directory for processed text files.
>- **Text to Speech Conversion:** It reads text from `.txt` files in the specified input directory and converts them to MP3 using the specified voice.
>- **Success Notification:** Sends a Telegram message upon successful conversion, including the elapsed time and indicating the completion of the process.
>- **Error Handling:** Includes checks for the existence of directories and files, handling exceptions during the conversion process.

- **text2mp3.sh**
> This **Bash** script *processes text files in a specified directory, converting them into MP3 audio files using the* `edge-tts` *command, and moves the original text files to another directory.*
>- **Directory Management:** *Ensures the existence of input, output, and move directories, creating them if necessary.*
>- **Text File Processing:** *Scans the input directory for `.txt` files and converts each to MP3 using a specified voice.*
>- **Conversion Notification:** *If the conversion is successful, it sends a message (through `send_message.sh`) indicating the completion along with the file name.*
>- **Error Handling:** *Provides feedback for missing files or issues during the conversion process.*

- **text2mp3.py**
> *This* **Python** *script processes text files by converting them into MP3 audio files using the* `edge_tts` *library and sends notifications through a Telegram bot.*
>- **Directory Management:** *Ensures that the specified input, output, and move directories exist and creates them if they do not.*
>- **Text File Conversion:** *Reads and converts `.txt` files in the input directory to MP3 using a specified voice, handling multiple files with progress updates.*
>- **Error Handling:** *Implements retries with delays for failed conversions, providing robust error messages and ensuring the script exits gracefully if errors reach the maximum retry limit.*
>- **Notification System:** *Sends a Telegram message after each successful conversion, detailing the time taken and the file converted.*

- **mp3Compress.py**
> *This* **Python** *script creates compressed tar.gz archives from a range of MP3 files located in a specified input directory, allowing for file grouping based on a defined range.*
>- **Command-Line Interface:** *Utilizes `argparse` to accept parameters such as start, end, and difference values to define which files to archive, along with input and output directories.*
>- **File Naming Convention:** *Constructs file names in a zero-padded format (e.g., `0001.mp3`), ensuring consistency and correct sorting.*
>- **Conditional Archiving:** *Only files that exist in the input directory are included in the generated tar.gz files. Messages are printed for any missing files.*
>- **Batch Archiving:** *Groups files based on the specified difference, creating a new tar.gz file for each range of valid files.*

---

### for MP4

- **mp4_maker.sh**
> *This* **Bash** *script processes MP3 files by generating MP4 videos with associated images derived from a PPTX presentation, utilizing Python scripts for conversion and handling errors effectively.*
>- **Command-Line Interface:** *Accepts five parameters, including input and output directories, a PPTX file path, and directories for moving and dumping files.*
>- **File Handling:** *Creates necessary directories if they do not exist and processes each MP3 file in the input directory.*
>- **PPTX Manipulation:** *Corrects the content of the specified PPTX file based on the MP3 filename, replacing placeholders with meaningful text.*
>- **Conversion Process:** *Converts the corrected PPTX to JPEG images and then merges these images with the MP3 audio to create MP4 videos.*
>- **Error Checks:** *Provides feedback for errors at each step, ensuring clear communication on the process status.*

- **revise_mp4_maker.py**
> *This* **Python** *script creates a video file from a specified image and audio track using the `moviepy` library, offering simple video editing capabilities.*
>- **Command-Line Interface:** *Accepts command-line arguments to specify the paths for the image, audio, and output video file, along with an optional frames per second (fps) setting.*
>- **Video Creation:** *Loads the image and audio files, setting the video duration to match the audio length and applying fade-in and fade-out effects to the audio.*
>- **Output Configuration:** *Generates the final video file with specified encoding options, including codec settings for music quality.*

- **00CompleteMp4Maker.py**
> *This* **Python** *script processes MP3 files by generating MP4 videos from a PPTX presentation and associated audio, sending notifications via Telegram.*
>- **Command-Line Interface:** *Accepts parameters for input and output directories, a PPTX file path, directories for moving processed files, a dump directory, a message for notifications, and frames per second (fps) for video output.*
>- **PPTX Manipulation:** *Uses the `TextReplacer` class to modify text in the PPTX file based on MP3 filename segments, creating a new PPTX for conversion.*
>- **Conversion Pipeline:** *Converts the modified PPTX to JPEG images and combines these images with the MP3 audio to create MP4 videos, applying fade-in and fade-out effects to audio.*
>- **Telegram Notifications:** *Sends an image and a message to a Telegram chat after processing each MP3 file, including information about the processed video.*
>- **Error Handling:** *Provides detailed logging for errors during file processing and handles cleanup of temporary files.*

---

### achive

- **edge-sample.py**
> *This* **Python** *script utilizes the `edge_tts` library to list available English (US) text-to-speech voices and generate audio samples from each voice.*
>- **Voice Listing:** *The `list_voices` function retrieves all voices, filtering to include only English (US) voices, which are then printed.*
>- **Sample Audio Generation:** *For each voice, the script synthesizes a short audio sample using a sample text, saving the output as an MP3 file labeled with the voice name.*
>- **Error Handling:** *The main function includes basic error handling to capture and report issues during voice listing or audio synthesis.*

- **move_files.py**
> *This* **Python** *script moves all files from subdirectories into the current working directory.*
>- **Directory Traversal:** *Utilizes `os.walk` to explore all subdirectories and files starting from the current directory.*
>- **File Movement:** *For each file found in subdirectories, it constructs the full file path and moves the file to the current directory using `shutil.move`, skipping files already present in the current directory.*
>- **Logging:** *Prints a message for each file moved, providing clear feedback on the operation’s progress.*

- **soxDurationFillter.py**
> *This* **Python** *script processes MP3 files in a specified directory to generate commands for merging them using the `sox` utility, which must be installed on a Linux system.*
>- **Directory Management:** *Creates a subdirectory named `0` within the specified directory to store the output files.*
>- **MP3 Duration Calculation:** *Computes the total duration of MP3 files, grouping them into segments for merging based on a cumulative duration of up to 11 hours and 30 minutes.*
>- **Command Generation:** *Constructs `sox` commands for the necessary merging operations. The commands are printed to the console in a format that can be piped directly into a bash shell for execution.*
>- **File Search:** *Recursively finds all MP3 files within the specified directory for processing.*

- **translate_0.1.py**
> *This* **Python** *script translates the contents of text files from a specified input directory to English, saving the translated content in a designated output directory and moving the original text files to a different directory.*
>- **Translation Process:** *Utilizes the `translate-shell` and `translators` Python packages to perform translations. Each line of text is translated individually with a brief delay to avoid rate limits.*
>- **File Management:** *Creates necessary directories for output and moving original files, and processes each text file in the input directory sequentially.*
>- **Logging:** *Provides feedback on the number of lines remaining to be translated, as well as the status upon completion of each file's translation.*

- **compress_open.py**
> *This* **Python** *script extracts all ZIP files from a specified directory, placing the contents into separate folders based on the ZIP file names.*
>- **Directory Setup:** *Specifies a source directory for ZIP files and a target directory for extraction. It creates the extraction directory if it does not exist.*
>- **File Handling:** *Iterates through all files in the specified directory, checking for files with the `.zip` extension.*
>- **Extraction Process:** *For each ZIP file, it creates a corresponding folder named after the file (without the `.zip` extension) and extracts the contents into that folder.*
>- **Feedback Mechanism:** *Prints a confirmation message indicating where each ZIP file has been extracted and confirms the completion of the extraction process.*

- **venv-pip.sh**
> *This code snippet lists several Python package installations necessary for a project, using `pip` to manage dependencies.*
>- **Package Installations:** Installs essential libraries including:
>>- **moviepy:** *For video editing and processing.*
>>- **html2text:** *For converting HTML content to plain text.*
>>- **edge-tts:** *For text-to-speech capabilities using Microsoft Edge.*
>>- **python-pptx-text-replacer:** *For manipulating text in PowerPoint presentations.*
>>- **python-telegram-bot:** *For building Telegram bots.*
>>- **Pillow:** *For image processing tasks.*
>>- **deep-translator (commented out):** *Could be used for translation tasks, but is currently not installed.*
>- **Environment Management:** *The `deactivate` command suggests that these installations were done within a virtual environment, allowing for better dependency management.*
>- **Usage Example:** *Run these commands in your terminal or command prompt to set up your Python environment with the necessary packages for your project.*

