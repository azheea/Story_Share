#流程 拆解文章内容并以句子划分 -> 计算读取文章时间、检索视频总时长是否满足 -> 将目录下的视频拼接,剪辑到朗读文章的时长 -> 将文段生成为音频,合并到原视频中
#auther:啊这.

import Tools.Story_Break as sb
import Tools.Video_Time as vt
import Tools.Voice_spawn as vp
import Tools.Voice_Time as vot
import Tools.Movie_Cutting as mc
import Tools.Voice_Change as vc
import shutil,os
path = os.getcwd()

# 拆解文章内容并以句子划分
print("正在处理文章\n")
sb.Story_Break()

# 获取视频总时长
print("正在获取视频时长\n")
Total_Video_Time = vt.get_total_duration()
print(f"视频总时长：{Total_Video_Time} 秒\n")

#生成音频
print("正在生成文章音频\n")
vp.Voice_spawn()
Voice_Time = vot.get_wav_duration()
print(f"音频总时长：{Voice_Time} 秒\n")

#计算时间差
delta_time = -(Voice_Time - Total_Video_Time)
if delta_time < 0:#视频时长不足
    print(f"视频时长不足，缺少 {delta_time} 秒,请补齐时长\n")
    exit()

else:
    print(f"视频时长超出 {delta_time} 秒,仅选取前 {Voice_Time} 秒生成视频\n")

if (input("视频时长足够! 是否继续生成视频?(y/n)\n") == "n"):
    print("音频已生成,正在停止…")
    exit()

print("\n开始生成视频\n")
mc.merge_and_clip_videos(Voice_Time)
print("\n视频合成完毕\n开始替换音轨")
vc.Voc_change()
shutil.copy2(os.getcwd() + "/log/voc_changed.mp4", os.getcwd() + "/Video.mp4")
print(f"音轨已经替换完成,输出在{os.getcwd()}下\n")
#todo:将文段转为字幕并嵌入视频
print("完成! ")