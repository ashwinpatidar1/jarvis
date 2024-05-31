import pyttsx3
import speech_recognition
import webbrowser
import wikipedia
import pywhatkit

engine = pyttsx3.init('sapi5')
voice = engine.getProperty("voices")
engine.setProperty("voices", voice[1].id)


def speek(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print('listening....')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print('recognising...')
        text = r.recognize_google(audio, language='en-in')
        print(f"you said : {text}")

    except r.UnknownValueError:
        print('i an anable to here...')
        return (0)

    return (text)


text = takeCommand()


def google(text):
    if 'google' in text:
        text = text.replace('search', '')
        text = text.replace('google', '')
        text = text.replace('on google', '')
        text = text.replace('jarvis', '')
        speek('this is what i found on google..')
        webbrowser.open('https://www.google.com/search?q=' + text)


def youtube(text):
    if 'youtube' in text:
        text = text.replace('search', '')
        text = text.replace('youtube', '')
        text = text.replace('jarvis', '')
        speek('this is what i found on youtube..')
        webbrowser.open('https://www.youtube.com/results?search_query=' + text)
        pywhatkit.playonyt(text)


def jiocinima():
    if 'ipl' in text:
        speek('done , sir...')
        webbrowser.open('https://www.jiocinema.com/sports')
        pywhatkit.playonyt()
