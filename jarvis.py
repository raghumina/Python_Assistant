# Virtual Assistant for desktop


import pyttsx3  # Library for speak and listen features
import datetime  # Library for date and time related function
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)

engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am your virtual assistant, How may I help you")


def takeCommand():
    # It takes command from user via speakers or microphone and returns string output
    r = sr.Recognizer
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing")
        query = r.recognize_google(audio, language="en-in")
        print(f"user {query}")

    except Exception as e:
        #  print(e)

        print("Say that again Please")
        return "None"


if __name__ == "__main__":
    wishMe()
