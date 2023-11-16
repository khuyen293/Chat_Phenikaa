from gtts import gTTS
import os
import pygame
from pynput import keyboard
import time

def text_to_speech(text, lang='vi'):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("output.mp3")
    pygame.init()
    
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()
    
    # Lắng nghe sự kiện phím "s" để dừng âm thanh
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
    
    # Chờ cho âm thanh phát xong
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

def on_press(key):
    if key.char == 's':
        pygame.mixer.music.stop()
        return False

text_to_speech("haha")