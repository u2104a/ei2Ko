# for this code, importing python module `pip install translate-shell`
# `pip install translators`
# [ https://pypi.org/project/translate-shell/ ]
# [ https://translate-shell.readthedocs.io/en/latest/index.html ]


import os
import sys
import time
import glob
import shutil
from translate_shell.translate import translate

def mtrans(original_text):
    result = translate(original_text, "en")
    translated_text = result.results[0].paraphrase
    return translated_text

def processing_text(bulk_text):
    b1 = len(bulk_text)
    a1 = []
    for text in bulk_text:
        translated_text = mtrans(text)
        time.sleep(0.5)
        a1.append(translated_text)
        b1 -= 1
        print(f"\t{b1} left", end='\r')
    return a1

    # def processing_list(raw_list):
    #     organized_list = []
    #     temp = None
    #     mark = 0
    #     for txt in raw_list:
    #         if mark == 5:
    #             pass
    #         else:
                

def create_directories(directories):
    """Create directories if they don't exist."""
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

def translateF(path,output_file):

    with open(path,'r') as a:
        large_text=a.readlines()

    print(f"- working file <{path}> with {len(large_text)} lines ")
    translated = processing_text(large_text)
    text=""
    for o in translated:
        text+="\n"+o
    with open(output_file,'w') as a:
        large_text=a.write(text)
    print(f"done file <{output_file}>")

def main(input_directory, output_directory, move_directory):
    # Create necessary directories
    create_directories([output_directory, move_directory])

    # Process each MP3 file in the input directory
    txt_files = sorted(glob.glob(os.path.join(input_directory, '*.txt')))

    if not txt_files:
        print(f">> No text files found in {input_directory} <<")
        return

    for txt_file in txt_files:
        if os.path.isfile(txt_file):
            file_name = os.path.basename(txt_file)
            output_file = os.path.join(output_directory, file_name)
            translateF(txt_file,output_file)
            shutil.move(txt_file, move_directory)

        else:
            print(f">> {txt_file} is not a valid file <<")

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: python script.py input_directory output_directory move_directory")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_directory = sys.argv[2]
    move_directory = sys.argv[3]

    main(input_directory, output_directory, move_directory)

