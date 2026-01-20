# for this code, importing python module `translators`
# `pip install translators`
# [ https://pypi.org/project/translators/ ]
# [ https://github.com/UlionTse/translators ]

import os
os.environ["translators_default_region"] = "EN" 
import sys
import time
import glob
import shutil
import logging
import translators as ts

# Configure logging to store logs in a file
#logging.basicConfig(filename='translation_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def mtrans(original_text):
    """Translate text from Chinese to English using modernMt translator."""
    try:
        result = ts.translate_text(
            original_text,
            translator="google",
            from_language="zh-CN",
            to_language="en"    #,"hi"
            #sleep_seconds=sleep_seconds
        )
        return result
    except Exception as e:
        logging.error(f"Error translating text: {e}")
        return original_text  # Return original text in case of error

def processing_text(bulk_text, sleep_seconds=3):
    """Process a list of text strings and translate them."""
    a1 = []
    for text in bulk_text:
        time.sleep(sleep_seconds)
        translated_text = mtrans(text)
        a1.append(translated_text+"\n")
        logging.info(f"{len(bulk_text) - len(a1)} translations left")
    return a1

def create_directories(directories):
    """Create directories if they don't exist."""
    for directory in directories:
        try:
            os.makedirs(directory, exist_ok=True)
            logging.info(f"Directory created: {directory}")
        except Exception as e:
            logging.error(f"Error creating directory {directory}: {e}")

def split_text(text, max_length=4990):
    """Split text into chunks of a specified maximum length."""
    chunks = []
    current_chunk = ""

    # Split the text into words
    words = text.split()

    for word in words:
        if len(current_chunk) + len(word) + (1 if current_chunk else 0) <= max_length:
            if current_chunk:
                current_chunk += " "
            current_chunk += word
        else:
            if current_chunk:
                chunks.append(current_chunk)
            current_chunk = word

    if current_chunk:
        chunks.append(current_chunk)

    return chunks

def translateF(path, output_file):
    """Translate the content of a file and save the result to another file."""
    try:
        with open(path, 'r', encoding='utf-8') as a:
            large_text = a.read()
            processed_text = split_text(large_text)

        logging.info(f"Working on file <{path}> with {len(processed_text)} chunks")
        translated = processing_text(processed_text)
        
        with open(output_file, 'w', encoding='utf-8') as a:
            a.write("\n".join(translated))
        
        logging.info(f"Done translating file <{output_file}>")
    except Exception as e:
        logging.error(f"Error processing file {path}: {e}")

def main(input_directory, output_directory, move_directory):
    """Main function to orchestrate the translation process."""
    create_directories([output_directory, move_directory])

    txt_files = sorted(glob.glob(os.path.join(input_directory, '*.txt')))

    if not txt_files:
        logging.warning(f"No text files found in {input_directory}")
        return

    for txt_file in txt_files:
        if os.path.isfile(txt_file):
            file_name = os.path.basename(txt_file)
            output_file = os.path.join(output_directory, file_name)
            translateF(txt_file, output_file)
            try:
                shutil.move(txt_file, move_directory)
                logging.info(f"Moved file {txt_file} to {move_directory}")
            except Exception as e:
                logging.error(f"Error moving file {txt_file} to {move_directory}: {e}")
        else:
            logging.warning(f"{txt_file} is not a valid file")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        logging.error("Usage: python script.py input_directory output_directory move_directory")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_directory = sys.argv[2]
    move_directory = sys.argv[3]

    main(input_directory, output_directory, move_directory)
