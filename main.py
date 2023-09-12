import speech_recognition as sr
import os


def say(text):
    os.system(f'say "{text}"')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en")
            return query
        except Exception as e:
            print(e)
            return "Some error occurred. Sorry JARVIS"


if __name__ == '__main__':
    say("Hello, I'm JARVIS.")

    while True:
        print("Listening...")
        text = takeCommand().lower()
        print(text)
        say(text)
