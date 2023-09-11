import speech_recognition as sr
import os


def say(text):
    os.system(f'say "{text}"')


if __name__ == '__main__':
    say("hello i'm jarvis A I")
