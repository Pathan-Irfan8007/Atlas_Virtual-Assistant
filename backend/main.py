import pyttsx3
import speech_recognition as sr
import time
import webbrowser
import keyboard
import pyautogui
import subprocess


engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

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

    if "say hello" in command:
        speak("Hello friend, Nice to meet you !")
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
    elif "minimise" in command or "maximize" in command:
        keyboard.press_and_release("win + d")
    elif "scroll down" in command:
        pyautogui.scroll(-500)
    elif "scroll up" in command:
        pyautogui.scroll(500)
    elif "open notepad" in command:
        subprocess.Popen("notepad.exe")
    else:
        speak("Sorry but I am not prepared for that .")



if __name__ == "__main__" :
    
    while True:
        initialize = take_command()
        if "wake up" in initialize.lower():
            print("Hello I am Atlas, a virtual assistant")
            speak("Hello I am Atlas, a virtual assistant")
            

            while True:
                print()
                command = take_command()

                if command :
                    # print(command)
                    process_command(command)
                else:
                    print("No command recognize !")
                    speak("No command recognize !")

        