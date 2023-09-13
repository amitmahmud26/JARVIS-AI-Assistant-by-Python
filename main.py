import speech_recognition as sr
import os
import webbrowser


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
    say("Hello, How can I help you?")

    while True:
        print("Listening...")
        query = takeCommand().lower()
        say(query)
        print(query)
        sites = [["youtube", "https://youtube.com"], ["google", "https://google.com"], ["wikipedia", "https://wikipedia.org"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}...")
                webbrowser.open(site[1])\


        if f"Open whatsapp".lower() in query.lower():
            os.system("open /Applications/WhatsApp.app")
