import speech_recognition as sr
import time
import webbrowser
import keyboard
import pyautogui
import subprocess
from commands import *
from voice import speak


def take_command():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language = "en-IN")
        return query.lower()
    
    except Exception :
        return ""

def process_command(command):
    
    command = command.lower()
 
    for query, action in COMMANDS.items():
        if query in command:
            action(command)
            return
    else:
        speak("Sorry, but I am not prepared of that")

    


if __name__ == "__main__" :
    
    while True:
        initialize = take_command()
        if "wake up" in initialize.lower():
            speak("")
            time.sleep(0.5)
            print("Welcome back Chief")
            speak("Welcome back Chief")
            

            while True:
                print()
                command = take_command()
                print(command)

                
                if command :
                    process_command(command)
                else:
                    print("No command recognize !")
                    speak("No command recognize !")

        