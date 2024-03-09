import speech_recognition as sr
from gtts import gTTS
import pygame
from googletrans import Translator, LANGUAGES
from tkinter import *
from tkinter import messagebox, simpledialog


def print_supported_languages():
    print("Supported Languages:")
    for code, language in LANGUAGES.items():
        print(f"{code}: {language}")


def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print("Error with the service; {0}".format(e))
        return None


def speak_text(text, lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("output.mp3")

    # Use pygame to play the audio
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()
    pygame.event.wait()  # Wait for the playback to finish before proceeding


def translate_and_speak():
    text_v = recognize_speech()
    if not text_v:
        messagebox.showerror(message="Failed to recognize speech.")
        return

    lang_v = simpledialog.askstring(
        "Input", "Enter target language code (e.g., 'es' for Spanish):")
    if not lang_v:
        lang_v = 'en'  # Default to English if no language code is provided

    try:
        translator = Translator()
        translated_text = translator.translate(text_v, dest=lang_v).text
        messagebox.showinfo(message="Translated Text: " + translated_text)
        speak_text(translated_text, lang=lang_v)
    except sr.UnknownValueError:
        messagebox.showerror(message="Could not understand audio")
    except sr.RequestError as e:
        messagebox.showerror(message=f"Error with the service; {str(e)}")
    except Exception as e:
        error_message = str(e)


if _name_ == "_main_":
    print_supported_languages()

    window = Tk()
    window.geometry("500x300")
    window.title("Speech-to-Text and Text-to-Speech Translator")
    title_label = Label(window, text="Speech-to-Text and Text-to-Speech Translator", font=(
        "Gayathri", 12)).pack()

    button1 = Button(window, text='Translate and Speak', bg='Turquoise',
                     command=translate_and_speak, font=("arial", 10)).pack(padx=10, pady=10)

    window.mainloop()
