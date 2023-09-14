import speech_recognition as sr
import os
import webbrowser
import openai
import time


def ai(prompt):
    text = ""
    openai.api_key = "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"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": ""
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response["choices"][0]["message"]["content"])
    text += response["choices"][0]["message"]["content"]

    if not os.path.exists("OpenAI"):
        os.mkdir("OpenAI")

    with open(f"OpenAI/{''.join(prompt.split('intelligence')[1:])}.txt", "w") as f:
        f.write(text)


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
        # say(query)
        print(query)
        time.sleep(1)
        print("Please wait for the response...")

        sites = [["youtube", "https://youtube.com"], ["google", "https://google.com"],
                 ["wikipedia", "https://wikipedia.org"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}...")
                webbrowser.open(site[1])

        if f"Open whatsapp".lower() in query.lower():
            os.system("open /Applications/WhatsApp.app")

        if "using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        if "exit".lower() in query.lower():
            break
