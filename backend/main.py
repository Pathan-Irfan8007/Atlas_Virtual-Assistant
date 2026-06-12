import pyttsx3
import speech_recognition as sr


def speak(text):
    engine = pyttsx3.init()
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

if __name__ == "__main__" :
    print("Hello I am Atlas, a virtual assistant")
    speak("Hello I am Atlas, a virtual assistant")

    while True:
        print()
        command = take_command()

        if command :
            print(f"This is Your Command : {command}")
            speak(f"This is Your Command : {command}")
        else:
            print("No command recognize !")
            speak("No command recognize !")