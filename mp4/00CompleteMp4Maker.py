import os
import shutil
import sys
import subprocess
import glob
import asyncio


from python_pptx_text_replacer import TextReplacer
from moviepy import ImageClip, AudioFileClip
from moviepy.audio.fx import AudioFadeIn, AudioFadeOut
from telegram import Bot


# Telegram bot token and chat ID
TELEGRAM_BOT_TOKEN = "6969578979:AAHVOmPy8sYdKB0bb3cz_q9aT1celA6ahOg"  # Replace with your bot token
TELEGRAM_CHAT_ID = '-1002136069032'  # Replace with your chat ID

async def send_telegram_message(message):
    """Send a message to a Telegram chat."""
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

async def send_photo(photo_path, caption):
    """Send a photo to a Telegram chat with an optional caption."""
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    with open(photo_path, 'rb') as photo:
        await bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=photo, caption=caption)

def create_directories(directories):
    """Create directories if they don't exist."""
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

def process_mp3_file(mp3_file, pptx_file_path, dump_directory, output_directory, move_directory, message, fps):
    """Process a single MP3 file."""
    file_name = os.path.basename(mp3_file)
    file_name_no_ext = os.path.splitext(file_name)[0]

    # Extract information from the MP3 filename
    ad = file_name_no_ext.split('-')

    # Check if the filename contains a hyphen
    if len(ad) < 2:
        print(f">> ERROR: Filename '{file_name}' does not contain a hyphen ('-'). Exiting... <<")
        sys.exit(1)  # Exit the program if the filename is not valid

    # Safely access ad[0] and ad[1]
    text_replacer = f"{ad[0]} to {ad[1]}"

    # Define paths
    dump_ppt_file = os.path.join(dump_directory, f"{os.path.splitext(os.path.basename(pptx_file_path))[0]}.pptx")
    mp4_file = os.path.join(output_directory, f"{file_name_no_ext}.mp4")
    n_mp4_file = os.path.join(output_directory, f"Chapter {text_replacer} | {message} | #audiobook.mp4")

    try:
        # PPTX Correction
        replacer = TextReplacer(pptx_file_path, slides='1', tables=True, charts=True, textframes=True)
        replacer.replace_text([('XXXXxXXXX', text_replacer)])
        replacer.write_presentation_to_file(dump_ppt_file)
        print(">> PPTX Correction DONE <<")

        # PPTX to JPEG Conversion
        subprocess.run(
            ["libreoffice", "--convert-to", "jpg", dump_ppt_file, "--outdir", dump_directory],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print(">> PPTX to JPEG Conversion [ DONE ] <<")

        # Define paths for MP4 creation
        image_path = os.path.join(dump_directory, f"{os.path.splitext(os.path.basename(pptx_file_path))[0]}.jpg")
        audio_path = mp3_file

        # Load audio clip
        audio_clip = AudioFileClip(audio_path)

        # Load image and create a video clip with the same duration as the audio
        video_clip = ImageClip(image_path).with_duration(audio_clip.duration)

        # Apply fade-in and fade-out effects to the audio
        audio_clip = audio_clip.with_effects([AudioFadeOut("00:00:02"),AudioFadeIn("00:00:02")])

        # Set audio to the video clip
        video_clip = video_clip.with_audio(audio_clip)

        # Write the final video file with the specified fps
        video_clip.write_videofile(mp4_file, codec="libx264", audio_codec="aac", fps=fps)

        print(f">> Mp4 Creation <{mp4_file}> [ DONE ] <<")

        # reanaming mp4 file
        os.rename(mp4_file,n_mp4_file)

        # Move the processed MP3 file
        shutil.move(mp3_file, move_directory)

        # Send a message to Telegram
        message = f"Novel: {message}\nProcessed MP3 file: {file_name_no_ext}.mp4"
        asyncio.run(send_photo(image_path,message)) # Send message synchronously
        cleanup_dump_directory(dump_directory)

    except subprocess.CalledProcessError as e:
        print(f">> ERROR during subprocess execution: {e.stderr.decode().strip()} <<")
    except Exception as e:
        print(f">> ERROR: {str(e)} <<")

def cleanup_dump_directory(dump_directory):
    """Remove all files in the dump directory."""
    for file in os.listdir(dump_directory):
        file_path = os.path.join(dump_directory, file)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f">> Removed {file_path} <<")
        except Exception as e:
            print(f">> ERROR: Could not remove {file_path}. Reason: {str(e)} <<")

def main(input_directory, output_directory, pptx_file_path, move_directory, dump_directory, message, fps=1):
    # Create necessary directories
    create_directories([output_directory, move_directory, dump_directory])

    # Process each MP3 file in the input directory
    mp3_files = sorted(glob.glob(os.path.join(input_directory, '*.mp3')))

    if not mp3_files:
        print(f">> No MP3 files found in {input_directory} <<")
        return

    for mp3_file in mp3_files:
        if os.path.isfile(mp3_file):
            process_mp3_file(mp3_file, pptx_file_path, dump_directory, output_directory, move_directory, message, fps)
        else:
            print(f">> {mp3_file} is not a valid file <<")

    # Optionally clean up the dump directory
    cleanup_dump_directory(dump_directory)

if __name__ == "__main__":
    if len(sys.argv) != 8:
        print("Usage: python script.py input_directory output_directory pptx_file_path move_directory dump_directory message fps")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_directory = sys.argv[2]
    pptx_file_path = sys.argv[3]
    move_directory = sys.argv[4]
    dump_directory = sys.argv[5]
    message = sys.argv[6]

    # Convert fps argument to an integer
    try:
        fps = int(sys.argv[7])
    except ValueError:
        print(">> ERROR: FPS must be an integer <<")
        sys.exit(1)

    main(input_directory, output_directory, pptx_file_path, move_directory, dump_directory, message, fps)
