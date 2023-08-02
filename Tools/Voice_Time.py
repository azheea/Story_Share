import wave
import os
def get_wav_duration():
    with wave.open(os.getcwd()+ "/log/Story.wav", 'rb') as wav_file:
        # 获取音频文件的帧数
        frames = wav_file.getnframes()
        # 获取音频文件的采样率
        sample_rate = wav_file.getframerate()
        # 计算音频文件的时长
        duration = frames / float(sample_rate)
        return int(duration)
