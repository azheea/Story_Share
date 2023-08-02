from moviepy.editor import VideoFileClip, TextClip
import os
# 读取文本文件内容
with open(os.getcwd() + "/log/output.txt", 'r',encoding="utf-8") as file:
    text_content = file.read()
# 设置视频速率
rate = 30
# 读取视频文件
video = VideoFileClip(os.getcwd() + "/log/voc_changed.mp4")
# 创建字幕文本对象
text = TextClip(text_content, fontsize=30, color='white', bg_color='black')
# 设置字幕文本的位置和持续时间
text = text.set_position(('center', 'bottom')).set_duration(video.duration)
# 设置视频速率
video = video.set_duration(video.duration/rate)
# 合并视频和字幕
final = video.set_audio(None).set_audio(video.audio).set_fps(rate).set_duration(video.duration)
final = final.set_audio(None).set_audio(video.audio)
# 保存合成后的视频
final.write_videofile("output.mp4", codec="libx264", audio_codec="aac")