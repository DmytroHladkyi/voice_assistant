import requests
import speech_recognition 
import pyttsx3
import requests
import datetime
from pprint import pprint
from weathertoken import open_weather_token




sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.7

def listen_command():
    """Возвращает распознанную команду"""
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                sr.adjust_for_ambient_noise(source=mic, duration=0.5)
                audio = sr.listen(source=mic, timeout=10)
                query1 = sr.recognize_google(audio_data=audio, language='pl')
                return query1
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



def get_weather(query1):
    # open_weather_token = "open_weather_token"
    

    code_to_smile = {
        "Clear": "Bez chmurnie \U00002600",
        "Clouds": "Częściowo zachmurzenie \U00002601",
        "Rain": "Deszcz \U00002614",
        "Drizzle": "Deszcz \U00002614",
        "Thunderstorm": "Burza z piorunami \U000026A1",
        "Snow": "Śnieg \U0001F328",
        "Mist": "Mgła \U0001F32B"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={query1}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        query1 = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, не пойму что там за погода!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        speak("Pokazuje jaka jest pogoda w mieście:")
        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Pogoda w mieście: {query1}\nTemperatura: {cur_weather}C° {wd}\n"
              f"Wilgotność: {humidity}%\nCiśnienie: {pressure} mmHg\nWiatr: {wind} m/s\n")
        return ''

    except Exception as ex:
        print(ex)
        return("Sprawdź miasto")


def main1():
    
    speak("Wybierz miasto:")
    print("Wybierz miasto:")
    query1 = listen_command()
    speak(f"Wybrałeś miasto {query1}")
    print(f"Wybrałeś miasto {query1}")
    get_weather(query1)


if __name__ == '__main1__':
    main1()