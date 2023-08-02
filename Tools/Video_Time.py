import os
from moviepy.editor import VideoFileClip
def get_total_duration():
    total_duration = 0
    for filename in os.listdir(os.getcwd() + "/videos"):
        filepath = os.path.join(os.getcwd() + "/videos", filename)
        if os.path.isfile(filepath):
            try:
                video = VideoFileClip(filepath)
                duration = video.duration
                total_duration += duration
            except Exception as e:
                print(f"Failed to process file: {filename}")
                print(e)
    return total_duration