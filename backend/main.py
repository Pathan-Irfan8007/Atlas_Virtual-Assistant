import pyttsx3
import speech_recognition as sr

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
        print(f"User Said : {query}")
        return query.lower()
    
    except Exception :
        print("I can't recognize...")
        return ""

if __name__ == "__main__" :
    print("Hello I am Atlas, a virtual assistant")
    speak("Hello I am Atlas, a virtual assistant")

    while True:
        print()
        command = take_command()
        print(f"This is Your Command : {command}")