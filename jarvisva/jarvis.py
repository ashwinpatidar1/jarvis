import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
from time import sleep
engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def recognize_speech():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")

        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)

        # Capture the audio
        audio = recognizer.listen(source)

        print("Recognizing...")

        try:
            # Recognize speech using Google Speech Recognition
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            respond(text)
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print("Error fetching results; {0}".format(e))
            return None

def respond(text):
    text = text.lower()
    while True:
        if 'wake up' in text:
            from greetings import greetings
            greetings()

        while True:
            if 'hello' in text:
                speak('hello sir , how are you...')
            elif 'i am fine' in text:
                speak('that`s great sir...')
            elif 'how are you' in text:
                speak('perfect sir...')
            elif 'time' in text:
                from greetings import telltime
                telltime()
            elif 'open' in text:
                from open import webapps
                webapps(text)

            elif 'google' in text:
                text = text.replace('search', '')
                text = text.replace('google', '')
                text = text.replace('on google', '')
                text = text.replace('jarvis', '')
                speak('this is what i found on google..')
                webbrowser.open('https://www.google.com/search?q=' + text)

            elif 'youtube' in text:
                text = text.replace('search', '')
                text = text.replace('youtube', '')
                text = text.replace('jarvis', '')
                speak('this is what i found on youtube..')
                webbrowser.open('https://www.youtube.com/results?search_query=' + text)
                pywhatkit.playonyt(text)
            elif 'wikipedia' in text:
                text = text.replace('search', '')
                text = text.replace('wikipedia', '')
                text = text.replace('jarvis', '')
                text = text.replace('on wikipedia', '')
                speak('this is what i found on wikipedia...')
                webbrowser.open('https://en.wikipedia.org/wiki/' + text)

            elif 'ipl' in text:
                  jiocinima()
            elif 'close' in text:
                from open import close
                close(text)

            elif 'stop' in text:
                speak('thank you sir...')
                sleep()
            else:
                recognize_speech()
            recognize_speech()

def jiocinima():
    speak('done , sir...')
    webbrowser.open('https://www.jiocinema.com/sports')
    pywhatkit.playonyt()



if __name__ == "__main__":
     recognize_speech()