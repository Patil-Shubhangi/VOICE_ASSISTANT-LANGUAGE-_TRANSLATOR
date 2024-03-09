import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import subprocess


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source, timeout=10)  # Increase the timeout duration
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:" + query + "\n")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        speak("I didn't understand. Can you please repeat?")
        return "None"
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))
        speak("There was an error with the speech recognition service.")
        return "None"
    return query


def launch_translator():
    subprocess.Popen(["python", "language_translator.py"])


if _name_ == '_main_':

    speak("Amigo assistance activated ")
    speak("How can I help you")
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            try:
                results = wikipedia.summary(query, sentences=2)
                speak(
                    "According to Wikipedia")
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                print("Wikipedia DisambiguationError:", e)
                speak("There are multiple matches. Can you please be more specific?")
            except wikipedia.exceptions.PageError as e:
                print("Wikipedia PageError:", e)
                speak("Sorry, I couldn't find any information on that topic.")
        elif 'are you' in query:
            speak("I am Amigo developed by Jaspreet Singh")
        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
        elif 'open github' in query:
            speak("Opening GitHub")
            webbrowser.open("https://github.com")
        elif 'open spotify' in query:
            speak("Opening Spotify")
            webbrowser.open("https://www.spotify.com")
        elif 'play music' in query:
            speak("Opening music")
            webbrowser.open("https://www.spotify.com")
        elif 'launch translator' in query:
            speak("Launching Speech-to-Text and Text-to-Speech Translator")
            launch_translator()
        elif 'sleep' in query:
            exit(0)
