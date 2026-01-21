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

    # Create move directory if it doesn't exist
    os.makedirs(move_directory, exist_ok=True)

    voice_1 = 'en-HK-YanNeural'  # Ensure this is the correct voice name

    # Get all text files in the input directory
    text_files = sorted(list(Path(input_directory).glob("*.txt")))
    if not text_files:
        print(f"No text files found in the input directory: {input_directory}")
        sys.exit(0)

    total_files = len(text_files)
    print("Total Files:\t",total_files)

    # Process each text file in the input directory
    for text_file in text_files:
        if text_file.is_file():
            # Extract filename without extension
            file_name_no_ext = text_file.stem

            # Define the output MP3 file path
            mp3_file = os.path.join(output_directory, f"{file_name_no_ext}.mp3")

            # Use edge-tts to convert text file to MP3
            try:
                with open(text_file, 'r') as r:
                    textr = r.read()  # Corrected line

                t1 = datetime.now()
                await txt2mp3(textr, voice_1, mp3_file)
                t2 = datetime.now()

                print(f"--> time : {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")
                print(f"--> time taken : {(t2-t1).total_seconds()}")
                print("--> Conversion successful..")
                total_files-=1
                print(f"- {total_files} file remaining")

                # Move the processed text file to the specified move_directory
                os.rename(text_file, os.path.join(move_directory, text_file.name))

                # Send message
                msg = f"> {comment}\n> {file_name_no_ext} mp3 [#] \n> time taken : {(t2-t1).total_seconds()} seconds "
                await send_telegram_message(msg)
                print("--> message send successful..")

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

async def txt2mp3(TEXT, VOICE, OUTPUT_FILE) -> None:
    max_retries = 3
    for attempt in range(max_retries):
        try:
            """Convert text to MP3 using edge-tts."""
            communicate = edge_tts.Communicate(TEXT, VOICE)
            await communicate.save(OUTPUT_FILE)
            print(f"--> Successfully saved to {OUTPUT_FILE}")
            return  # Exit the function if successful
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:  # If not the last attempt
                await asyncio.sleep(3)  # Wait before retrying
            else:
                print("Max retries reached. Exiting.")
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
