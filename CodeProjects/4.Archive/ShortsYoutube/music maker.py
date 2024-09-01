from pydub import AudioSegment
from pydub.generators import Sine
import os

def create_audio_file(duration, output_file):
    # Create a 2-minute audio file (you can replace Sine with other generators)
    audio = Sine(440).to_audio_segment(duration=duration * 1000)

    # Export the audio file as WAV
    audio.export(output_file, format="wav")
    return output_file

def adjust_duration(input_file, output_file, target_duration):
    # Load the audio file
    audio = AudioSegment.from_file(input_file, format="wav")

    # Repeat the audio to achieve the target duration
    repeated_audio = audio * (target_duration // len(audio) + 1)

    # Trim the audio to the target duration
    final_audio = repeated_audio[:target_duration * 1000]

    # Export the final audio file as MP3
    final_audio.export(output_file, format="mp3")

if __name__ == "__main__":
    original_duration = 2  # minutes
    target_duration = 60  # minutes

    input_file = "Violet Vape - Cheel.mp3"
    output_file = "extended_audio.mp3"

    create_audio_file(original_duration, input_file)
    adjust_duration(input_file, output_file, target_duration)

    # Cleanup: Delete the temporary WAV file
    os.remove(input_file)

    print(f"Audio file with {original_duration} minutes duration adjusted to {target_duration} minutes and saved as {output_file}.")
