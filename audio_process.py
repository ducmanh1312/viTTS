from moviepy.editor import VideoFileClip

def convert_mp4_to_wav(input_file, output_file):
    video = VideoFileClip(input_file)
    audio = video.audio
    audio.write_audiofile(output_file)
    audio.close()
    video.close()

# Convert the file
input_mp4 = "lesson.mp4"
output_wav = "model/lesson.wav"
convert_mp4_to_wav(input_mp4, output_wav)