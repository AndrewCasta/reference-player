import time
import os
import speech_recognition as sr
from playsound import playsound

path = os.getcwd()
reference_files = os.listdir(path + "/audio")


def check_references(audio):
    audio = audio.replace("'", "")
    print(audio)
    for reference in reference_files:
        if os.path.splitext(reference)[0] in audio:
            print(reference)
            playsound(path + "\\audio\\" + reference)


def callback(recognizer, audio):
    try:
        audio = recognizer.recognize_google(audio)
        check_references(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as error:
        print(
            f"Could not request results from Google Speech Recognition service; {error}"
        )


r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    r.adjust_for_ambient_noise(source)

stop_listening = r.listen_in_background(mic, callback)

# Placeholder for program that doesn't exit.
for _ in range(60):
    time.sleep(1)

# stop_listening(wait_for_stop=False)
