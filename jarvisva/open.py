import os
import webbrowser
import pyttsx3
import pyautogui
import subprocess
from time import sleep

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


dictapp = {"instagram": 'instagram', 'whatsapp': 'WhatsApp', 'chrome': 'chrome', 'word': 'winword', 'powerpoint':
    'powerpoint', 'paint': 'paint', 'commandprompt': 'cmd', 'files': 'file explorer'}


def webapps(text):
    speak('launching ,sir')
    if '.com' in text or '.co.in' in text or '.org' in text:
        text = text.replace('open', '')
        text = text.replace('jarvis', '')
        text = text.replace('launch', '')
        text = text.replace(' ', '')
        webbrowser.open(f'https://www.{text}')
   #else:
    #   keys= list(dictapp.keys())
     #  for app in keys:
      #      if app in text:
       #      ap=(f'{dictapp[app]}.exe')
        #     os.open(ap)\\\


def close(text):
    speak('closing sir..')
    if 'tab' in text:
        pyautogui.hotkey('ctrl', 'w')
    else:
        keys = list(dictapp.key())
        for app in keys:
            if app in text:
                os.system(f'taskki11 /f /im {dictapp[app]}.exe')