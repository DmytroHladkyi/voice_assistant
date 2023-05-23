import os
import random
import speech_recognition 
import time
import pyttsx3
import fnmatch

sr = speech_recognition.Recognizer()
sr.pause_threshold = 1


# commands_dict = {
#     'commands': {
#         'greeting': ['witaj', 'cześć'],
#         'create_task': ['dodać notatkę', 'notatka'],
#         'play_music': ['muzyka', 'włącz muzykę'],
#         'open_todo_list': ['otwórz notatkę', 'pokaż notatkę'],
#         'remove_task': ['usuń notatkę'],
#         'searching_file': ['chcę znaleźć folder'],
#     }
# }

# инициализировать библиотеку для генерации речи
engine = pyttsx3.init()

def speak(text):
    """Произносит текст"""
    engine.setProperty('rate', 128, )
    engine.say(text)
    engine.runAndWait()

def listen_command():
    """Возвращает распознанную команду"""
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                sr.adjust_for_ambient_noise(source=mic, duration=0.5)
                audio = sr.listen(source=mic, timeout=10)
                query = sr.recognize_google(audio_data=audio, language='pl').lower()
                return query
        except speech_recognition.UnknownValueError:
            print("Nie rozpoznałem")
            speak("Nie rozpoznałem")
            continue


def searching_file():
    print("Powiedz jak ma się nazywać folder.")
    speak("Powiedz jak ma się nazywać folder.")
    query = listen_command()

    # распознаем речь с помощью Google Speech Recognition
    try:
        print(f"Powiedziałeś: {query}")
        speak(f"Powiedziałeś: {query}")

        # ищем папки на компьютере
        folder_name = query.lower()
        matches = []
        
        for root, dirnames, filenames in os.walk("D:\\"):
            for dirname in dirnames:
                if fnmatch.fnmatch(dirname.lower(), folder_name):
                    matches.append(os.path.join(root, dirname))
                    print(f"Folder {folder_name} znaleziony w {root}")
                    
                    
        if matches:
            for match in matches:
                if os.path.isdir(match):
                    print(match)
                    return(f"Znalezione następujące pliki o nazwie {folder_name}:")  
        else:
            print(f"Folder {folder_name} nie znaleziony na komputrze")
    except speech_recognition.UnknownValueError:
        return "Nie rozpoznałem"