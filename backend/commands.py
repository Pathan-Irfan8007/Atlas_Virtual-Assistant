from voice import speak
import pyautogui
import subprocess
import keyboard
import webbrowser
import time
import sys

def say_hello(command):
    speak("Hello, This is Atlas, a virtual assistance")

def open_google(command):
    webbrowser.open("https://www.google.com")

def open_youtube(command):
    webbrowser.open("https://www.youtube.com")

def open_linkdin(command):
    webbrowser.open("https://www.linkedin.com/in/irfan-pathan-6494b0331")

def open_notepad(command):
    subprocess.Popen("notepad.exe")

def open_whatsapp(command):
    subprocess.Popen("whatsapp.exe")

def toggle_desktop(command):
    keyboard.press_and_release("win + d")

def scroll_down(command):
    pyautogui.scroll(-500)

def scroll_up(command):
    pyautogui.scroll(500)

def write(command):
    keyboard.write(f"{command[5:]} \n")

def exit(command):
    sys.exit()


COMMANDS = {
    "greet" : say_hello,
    "google" : open_google,
    "youtube" : open_youtube,
    "linkdin" : open_linkdin,
    "whatsapp" : open_whatsapp,
    "notepad" : open_notepad,
    "minimise" : toggle_desktop,
    "minimize" : toggle_desktop,
    "maximize" : toggle_desktop,
    "down" : scroll_down,
    "up" : scroll_up,
    "type" : write,
    "exit" : exit
}
