from moviepy.editor import VideoFileClip

# Input and output file paths
input_video = r"C:\Users\pieru\Desktop\Video matrimonio\tim\video.mp4"
output_video = r"C:\Users\pieru\Desktop\Video matrimonio\tim\video.avi"

# Load the video file
clip = VideoFileClip(input_video)

# Write the video to AVI format
clip.write_videofile(output_video, codec="mpeg4", audio_codec="libmp3lame")

print("Conversion completed!")
