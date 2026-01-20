import sys
from moviepy.editor import ImageClip, AudioFileClip
from moviepy.audio.fx.all import audio_fadein, audio_fadeout

def create_video(image_path, audio_path, output_path, fps=2):
    # Load image and audio clips, resize image to match audio duration
    video_clip = ImageClip(image_path).set_duration(AudioFileClip(audio_path).duration)

    # Combine image and audio clips, add fade-in and fade-out effects
    video_clip = video_clip.set_audio(audio_fadein(AudioFileClip(audio_path), 2).fx(audio_fadeout, 2))

    # Write the final video file with the specified fps
    video_clip.write_videofile(output_path, codec="libx264", audio_codec="aac", fps=fps)

if __name__ == "__main__":
    # Check if enough command-line arguments are provided
    if len(sys.argv) < 4:
        print("Usage: python script.py <image_path> <audio_path> <output_path> [fps]")
        sys.exit(1)

    # Get command-line arguments
    image_path, audio_path, output_path = sys.argv[1:4]

    # Set a default fps value or use the provided one
    fps = float(sys.argv[4])

    create_video(image_path, audio_path, output_path, fps)

