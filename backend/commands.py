import pyautogui
import subprocess
import keyboard
import webbrowser
import time
import sys
from voice import speak
from vision.gesture_control import *



def say_hello(command):
    speak("Hello, This is Atlas, a virtual assistance")

def open_google(command):
    speak("Starting Google")
    webbrowser.open("https://www.google.com")

def open_youtube(command):
    speak("Starting Youtube")
    webbrowser.open("https://www.youtube.com")

def open_linkdin(command):
    speak("Starting LinkdIn")
    webbrowser.open("https://www.linkedin.com/in/irfan-pathan-6494b0331")

def open_whatsapp(command):
    speak("Starting Whatsapp")
    webbrowser.open("https://web.whatsapp.com/")

def open_notepad(command):
    speak("Starting Notepad")
    subprocess.Popen("notepad.exe")

def toggle_desktop(command):
    keyboard.press_and_release("win + d")

def scroll_down(command):
    pyautogui.scroll(-500)

def scroll_up(command):
    pyautogui.scroll(500)

def write(command):
    keyboard.write(f"{command[5:]} \n")

def gesture_control(command):
    start_gesture_control()

def exit(command):
    sys.exit()


COMMANDS = {
    "introduce" : say_hello,
    "google" : open_google,
    "youtube" : open_youtube,
    "linkedin" : open_linkdin,
    "whatsapp" : open_whatsapp,
    "notepad" : open_notepad,
    "minimise" : toggle_desktop,
    "minimize" : toggle_desktop,
    "maximize" : toggle_desktop,
    "down" : scroll_down,
    "up" : scroll_up,
    "type" : write,
    "gesture control" : gesture_control,
    "exit" : exit
}

