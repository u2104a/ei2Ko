import os
import sys
import asyncio
import edge_tts
from pathlib import Path
from telegram import Bot
from datetime import datetime

async def main(input_directory, output_directory, move_directory, comment):
    # Check if input directory exists
    if not os.path.isdir(input_directory):
        print(f"Error: Input directory does not exist: {input_directory}")
        sys.exit(1)

    # Create output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    mp3_directory = f"{output_directory}/mp3"
    os.makedirs(mp3_directory, exist_ok=True)

    srt_directory = f"{output_directory}/srt"
    os.makedirs(srt_directory, exist_ok=True)

    # Create move directory if it doesn't exist
    os.makedirs(move_directory, exist_ok=True)

    voice_1 = 'en-HK-YanNeural'  # Ensure this is the correct voice name

    # Get all text files in the input directory
    text_files = sorted(list(Path(input_directory).glob("*.txt")))
    if not text_files:
        print(f"No text files found in the input directory: {input_directory}")
        sys.exit(0)

    # Process each text file in the input directory
    for text_file in text_files:
        if text_file.is_file():
            # Extract filename without extension
            file_name_no_ext = text_file.stem

            # Define the output MP3 file path
            mp3_file = os.path.join(mp3_directory, f"{file_name_no_ext}.mp3")

            # Define the output .srt file path
            srt_file = os.path.join(srt_directory, f"{file_name_no_ext}.srt")


            # Use edge-tts to convert text file to MP3
            try:
                with open(text_file, 'r') as r:
                    textr = r.read()  # Corrected line

                t1 = datetime.now()
                await txt2mp3(textr, voice_1, mp3_file, srt_file)
                t2 = datetime.now()

                print(f"Conversion successful.\n> time taken : {(t2-t1).total_seconds()}\n> MP3 and SRT saved in {output_directory} as {file_name_no_ext}.mp3")

                # Move the processed text file to the specified move_directory
                os.rename(text_file, os.path.join(move_directory, text_file.name))
                
                # Send message
                msg = f"<{comment}> {file_name_no_ext} mp3 COMPLETED converted by @a1b_d1"
                msg = f"> {comment}\n> {file_name_no_ext} mp3 [#] \n> time taken : {(t2-t1).total_seconds()} seconds "
                await send_telegram_message(msg)

                # Print the current date
                print("Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

            except Exception as e:
                print(f"Error during conversion for file: {text_file}. Error: {e}")
        else:
            print(f"Error: Text file does not exist: {text_file}")

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

async def txt2mp3(TEXT, VOICE, OUTPUT_FILE, SRT_FILE) -> None:
    try:
        """Main function"""
        communicate = edge_tts.Communicate(TEXT, VOICE)
        submaker = edge_tts.SubMaker()
        with open(OUTPUT_FILE, "wb") as file:
            async for chunk in communicate.stream():
                if chunk["type"] == "audio":
                    file.write(chunk["data"])
                elif chunk["type"] == "WordBoundary":
                    submaker.feed(chunk)

        with open(SRT_FILE, "w", encoding="utf-8") as file:
            file.write(submaker.get_srt())
    except:
            sys.exit()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py 'input_directory' 'output_directory' 'move_directory' 'comment'")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_directory = sys.argv[2]
    move_directory = sys.argv[3]
    comment = sys.argv[4]

    asyncio.run(main(input_directory, output_directory, move_directory, comment))
