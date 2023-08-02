from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
def merge_and_clip_videos(duration):
    folder_path = os.getcwd()+ "/videos"
    video_clips = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".mp4") or filename.endswith(".avi"):
            file_path = os.path.join(folder_path, filename)
            video = VideoFileClip(file_path)
            video_clips.append(video)
    
    final_clip = concatenate_videoclips(video_clips)
    final_clip = final_clip.subclip(0, duration)
    final_clip.write_videofile(os.getcwd()+ "/log/Good_time.mp4")