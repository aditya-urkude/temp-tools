from moviepy.editor import VideoFileClip

# Load the video file
video = VideoFileClip("video.mp4")

# Extract audio
audio = video.audio

# Save the audio to a file
audio.write_audiofile("output_audio.mp3")
