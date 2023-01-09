import os
from moviepy.editor import VideoFileClip

# Directory containing the MP4 files
directory = "C:\\Users\\SAI 1\\Desktop\\VAS\\data\\walk\\"

# Loop through all the files in the directory
for file in os.listdir(directory):
    # Check if the file is an MP4 file
    if file.endswith(".mp4"):
        # Create the output file name
        output_file = os.path.splitext(file)[0] + ".avi"

        # Read the MP4 file
        clip = VideoFileClip(directory + file)

        # Write the video to AVI
        clip.write_videofile(directory + output_file, codec='mpeg4')

print("Conversion completed!")