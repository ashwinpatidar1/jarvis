import pyttsx3
import datetime
import time

engine=pyttsx3.init('sapi5')
voice=engine.getProperty("voices")
engine.setProperty("voices", voice[1].id)


def speek(audio):
    engine.say(audio)
    engine.runAndWait()

def greetings():
     hour=int(datetime.datetime.now().hour)
     if hour>=0 and hour<=12:
         speek('good morning , sir..')
     elif hour>12 and hour<17:
         speek('good aftroon , sir..')
     else:
          speek('good evening,sir..')
     speek('how can i help you...')

def telltime():
    hour=int(time.strftime('%H'))
    min=int(time.strftime('%M'))
    speek(f"the time is {hour} hours and {min} minuts")