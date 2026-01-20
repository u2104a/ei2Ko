# this program is for linux with 'sox' installed
# sudo apt update && sudo apt install sox libsox-fmt-all
# if it shows support issue
# sudo apt install libsox-fmt-mp3

# using moviepy, import `pip install moviepy`

'''
output put should be piped in bash like
$ python script.py <directory_path> | bash
'''


import os
import sys
from moviepy import AudioFileClip

def create_directories(directories):
    os.makedirs(directories, exist_ok=True)

def get_mp3_duration(file_path):
    """Get the duration of an MP3 file."""
    audio_clip = AudioFileClip(file_path)
    duration = audio_clip.duration
    audio_clip.close()
    return duration

def format_duration(seconds):
    """Format duration from seconds to hh:mm:ss."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return (hours,minutes,seconds)

def find_mp3_files(directory):
    """Find all MP3 files in the specified directory."""
    mp3_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.mp3'):
                mp3_files.append(os.path.join(root, file))
    return sorted(mp3_files)

def baseN(a):
    a = os.path.basename(a)
    a = os.path.splitext(a)[0]
    return a


def sox(l1):
    for i1 in l1:
        t1 = "sox "
        for i in i1:
            t1+=f"{i} "
        t1+=f"{directory}/0/{baseN(i1[0])}-{baseN(i1[-1])}.mp3"
        print(f"echo '--WORKING-- {directory}/0/{baseN(i1[0])}-{baseN(i1[-1])}.mp3'")
        print(t1)
        print(f"echo '{directory}/0/{baseN(i1[0])}-{baseN(i1[-1])}.mp3  ++DONE++'")



if __name__ == "__main__":
    # Check if a directory path was provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    # Get the directory path from command-line arguments
    directory = sys.argv[1]
    create_directories(f"{directory}/0")
    # Find all MP3 files in the directory
    mp3_files = find_mp3_files(directory)

    # Print the duration of each MP3 file
    if not mp3_files:
        print("No MP3 files found in the specified directory.")
    else:
        # lit = []
        rduration=0
        alit = []
        rlit = []
        first = None

        for mp3_file in mp3_files:
            duration = get_mp3_duration(mp3_file)
            # formatted_duration = format_duration(duration)

            if rduration==0:
                first=mp3_file

            rduration+=duration
            check = format_duration(rduration)

            rlit.append(mp3_file)

            if mp3_file==mp3_files[-1]:
                # lit.append(f"---\n{first} --TO-- {mp3_file}\nDuration (hh:mm:ss): {check[0]:02}:{check[1]:02}:{check[2]:02}")
                alit.append(rlit)
                rlit=[]
                rduration=0


            if check[0]==11 and 30<check[1] and check[2]<60:
                # lit.append(f"---\n{first} --TO-- {mp3_file}\nDuration (hh:mm:ss): {check[0]:02}:{check[1]:02}:{check[2]:02}")
                alit.append(rlit)
                rlit=[]
                rduration=0

        sox(alit)
