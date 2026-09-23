import speech_recognition as sr
import pyttsx3
import webbrowser
import os

# Initialize text-to-speech
engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        speak("Sorry, I didn't catch that.")
        return ""

def open_youtube():
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")

def open_settings():
    speak("Opening Settings")
    os.system("start ms-settings:")  # Works on Windows

def open_camera():
    speak("Opening Camera")
    os.system("start microsoft.windows.camera:")  # Windows Camera

def run_jarvis():
    speak("Hello, I am Jarvis. How can I help you?")
    
    while True:
        command = listen()

        if "youtube" in command:
            open_youtube()

        elif "settings" in command:
            open_settings()

        elif "camera" in command:
            open_camera()

        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break

        else:
            speak("Command not recognized")

# Run the assistant
run_jarvis()
