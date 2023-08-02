import pyttsx3
import os
from moviepy.editor import AudioFileClip

def Voice_spawn():
    engine = pyttsx3.init()
    with open(os.getcwd()+ "\log\output.txt", 'r', encoding='utf-8') as file:
        text = file.read()
    
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 10)
    engine.save_to_file(str(text),os.getcwd()+ "/log/Story.wav")
    engine.runAndWait()