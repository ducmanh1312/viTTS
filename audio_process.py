# from moviepy.editor import VideoFileClip
from pydub import AudioSegment

def convert_mp3_to_wav(mp3_path, wav_path):
    # Load mp3 file
    sound = AudioSegment.from_mp3(mp3_path)
    # Export as wav
    sound.export(wav_path, format="wav")
    print(f"Converted {mp3_path} → {wav_path}")

# Ví dụ sử dụng
convert_mp3_to_wav("Minh.mp3", "Minh.wav")


# def convert_mp4_to_wav(input_file, output_file):
#     video = VideoFileClip(input_file)
#     audio = video.audio
#     audio.write_audiofile(output_file)
#     audio.close()
#     video.close()

# # Convert the file
# input_mp4 = "lesson.mp4"
# output_wav = "model/lesson.wav"
# convert_mp4_to_wav(input_mp4, output_wav)
