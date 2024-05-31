from pydub import AudioSegment
import os

def convert_audio(input_file, output_file, target_sample_rate, target_channels=1, target_sample_width=2, target_format='wav'):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    # Set the target parameters
    audio = audio.set_frame_rate(target_sample_rate)
    audio = audio.set_channels(target_channels)
    audio = audio.set_sample_width(target_sample_width)

    # Export the audio to the specified format
    audio.export(output_file, format=target_format)


input_file = "raw.m4a"
output_file = "audios/output_audio.wav"
target_sample_rate = 16000  
convert_audio(input_file, output_file, target_sample_rate)
