import os
from moviepy.editor import VideoFileClip

def convert_mp4_to_mov(input_folder, output_folder):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over files in input folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.mp4'):
            # Construct input and output file paths
            input_file = os.path.join(input_folder, file_name)
            output_file = os.path.join(output_folder, file_name.replace('.mp4', '.mov'))

            # Convert MP4 to MOV
            video_clip = VideoFileClip(input_file)
            video_clip.write_videofile(output_file, codec='libx264', audio_codec='aac')
            video_clip.close()

if __name__ == "__main__":
    input_folder = r'C:\Users\pieru\Desktop\Reb\Video'
    output_folder = r'C:\Users\pieru\Desktop\Reb\Video\MOV'

    convert_mp4_to_mov(input_folder, output_folder)
