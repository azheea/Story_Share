from moviepy.editor import *
import os
def Voc_change():
    # 读取视频
    videoclip = VideoFileClip(os.getcwd()+ "/log/Good_time.mp4")
    # 提取A视频
    audio_a = AudioFileClip(os.getcwd()+ "/log/Story.wav")
    videoclip = videoclip.set_audio(audio_a)
    # 输出新的视频文件
    videoclip.write_videofile(os.getcwd()+ "/log/voc_changed.mp4")