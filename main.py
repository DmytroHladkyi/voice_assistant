import speech_recognition 
import pyttsx3
from play_music import play_music
from create_task import create_task
from remove_task import remove_task
from open_todo_list import open_todo_list
from searching_file import searching_file
from sending_email import main2
# from test import main2
from weather import main1

import sys
sys.path.append(r'C:\Users\Hladkyi Dmytro\Desktop\IT Oprogromowanie\Python_Projects\searching_in_internet.py')


sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.7



commands_dict = {
    'commands': {
        'greeting': ['witaj', 'cześć'],
        'create_task': ['dodać notatkę', 'notatka'],
        'play_music': ['muzyka', 'włącz muzykę'],
        'open_todo_list': ['otwórz notatkę', 'pokaż notatkę'],
        'remove_task': ['usuń notatkę'],
        'searching_file': ['chcę znaleźć folder', 'folder'],
        'main2': ['poczta'],
        'main1': ['pogoda'],  
    }
    
}

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
         
    
def speak(text):
    """Произносит текст"""
    engine.setProperty('rate', 128, )
    engine.say(text)
    engine.runAndWait()
# инициализировать библиотеку для генерации речи
engine = pyttsx3.init()


def greeting():
    speak('Witam Ciebie!')
    return 'Witam Ciebie!'


def main():
    stop_words = ['stop','kończymy na dzisiaj','kończymy', 'nara']
    speak('Witam Ciebie')
    print("To jest Twój asystent głosowy.")
    
    while True:
      
        query = listen_command()
        # time.sleep(0.8)
        
        if any(word in query for word in stop_words):
            print('Do zobaczenia!')
            speak('Do zobaczenia!')
            break
        
        command_found = False
        for k, v in commands_dict['commands'].items():
            if query in v:
                print(globals()[k]())
                command_found = True
                speak("Co chcesz jeszcze?")
                print("Posłuchać muzyki lub dodać nową notatkę? Lub chcesz zobaczyć swoje notatki?")
                break

       
        if not command_found:
            print(f"Nie znaleziono komendy '{query}'")
            speak(f"Nie znaleziono komendy '{query}'")



if __name__ == '__main__':
    main()