import edge_tts
import asyncio

async def list_voices():
    # Get the list of voices
    voices = await edge_tts.list_voices()
    list_of_required_voices = []
    for di in voices:
        if di['Locale'] == "en-US":
            list_of_required_voices.append(di["ShortName"])
    return list_of_required_voices

async def synthesize_sample(voice_name, text):
    # Create a TTS client
    communicate = edge_tts.Communicate(text, voice_name)
    await communicate.save(f"{voice_name}.mp3")

async def main():
    try:
        # Step 1: List voices
        voices = await list_voices()
        
        # Print the list of English (US) voices
        print("Available English (US) Voices:", voices)

        # Step 2: Record a sample from each voice in the list
        for sample_voice in voices:
            sample_text = "Hello! This is a sample text to demonstrate the voice."
            print(f"\nRecording sample from voice: {sample_voice}")
            await synthesize_sample(sample_voice, sample_text)
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
