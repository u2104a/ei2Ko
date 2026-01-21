import os, sys, time, asyncio, subprocess

from telegram import Bot
from datetime import datetime
from moviepy import AudioFileClip

def create_directories(directories):
    os.makedirs(directories, exist_ok=True)

def get_mp3_duration(file_path):
    """Get the duration of an MP3 file."""
    try:
        audio_clip = AudioFileClip(file_path)
        duration = audio_clip.duration
        audio_clip.close()
        return duration
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return 0  # Return 0 duration if there's an error

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

async def send_telegram_message(message):
    try:
        """Send a message to a Telegram chat."""
        # Telegram bot token and chat ID
        TELEGRAM_BOT_TOKEN = None # Replace with your Bot Token
        TELEGRAM_CHAT_ID = None # Replace with your chat ID
        bot = Bot(token=TELEGRAM_BOT_TOKEN)
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
    except:
        print('message function not working....')

async def sox(l1,c1):
    for i1 in l1:
        t1 = ["sox"]
        for i in i1:
            t1.append(i)
        output_file = f"{directory}/0/{baseN(i1[0])}-{baseN(i1[-1])}.mp3"
        t1.append(output_file)
        
        print("Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print(f"--[ ]-- {output_file}")

        start_time = time.time()  # Start timing
        commandr(t1)  # Execute the command
        end_time = time.time()  # End timing

        print(f"------- time taken : {end_time - start_time:.6f} seconds")
        print(f"--[#]-- merging successful. {output_file}")

        msg = f"> {c1}\n>  merging successful. {output_file}\n> time taken : {end_time - start_time:.6f} seconds "
        await send_telegram_message(msg)

def commandr(command):
    if command and type(command)==list:
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e.stderr}")
    elif not command:
        print(" <`command`> list is empty")

if __name__ == "__main__":
    # Check if a directory path was provided as a command-line argument
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory_path> <comment> ")
        sys.exit()

    # Get the directory path from command-line arguments
    directory = sys.argv[1]

    comment = str(sys.argv[2])

    # for creating output directory
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

        asyncio.run(sox(alit,comment))
