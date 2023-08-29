import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    speak("Welcome back sir!")
    speak("Jarvis at your service. Please tell me how can I help you today?")
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir!")
    elif hour >= 18 and hour < 24:
        speak("Good evening sir!")
    else:
        speak("Good night sir!")


def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"
    return query

input("Press Enter to continue...")

if __name__ == "__main__":
    
    wishme()
    while True:
        query = TakeCommand().lower()

        if "open youtube" in query:
            speak("Opening Youtube")
            webbrowser.open("www.youtube.com")

        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("www.pornhub.com")

        elif "open stackoverflow" in query:
            speak("Opening Stackoverflow")
            webbrowser.open("www.stackoverflow.com")

        elif "play music" in query:
            speak("Playing Music")
            music_dir = "C:\\Users\\Admin\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "open code" in query:
            speak("Opening Visual Studio Code")
            codePath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "wikedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "offline" in query:
            speak("Going Offline")
            quit()

        elif "open notepad" in query:
            speak("Opening Notepad")
            notepadPath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(notepadPath)