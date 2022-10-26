import time

import speech_recognition as sr
import os
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser

from pip._internal.vcs import vcs

master = 'Mister'
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
import subprocess


def talking(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    talking("hey it's me, ratio")
    hour = int(datetime.datetime.now().hour)
    if 12 > hour > 5:
        talking(f"good morning {master}")
    elif 18 >= hour >= 12:
        talking(f"good afternoon {master}")
    elif 24 >= hour > 18:
        talking(f"good evening {master}")
    elif 5 >= hour > 24:
        talking(f"why did'nt you sleep? ")
    talking(f"what can i help you{master}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing..")
        query = r.recognize_google(audio, language='en-uk')
        print(f"{master} said: {query}\n")
    except Exception as e:
        print(e)
        talking("sorry, sir. can you repeat it? ")
        return "NONE"
    return query


if __name__ == "__main__":
    wishMe()
    jam = int(datetime.datetime.now().hour)
    while True:
        query = takeCommand().lower()
        if 'hello' in query:
            talking(f"hey{master} what can i do, ser? ")

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'google search' in query:
            talking('sir, what can i search for you?')
            data = takeCommand().lower()
            webbrowser.open(f"{data}")

        elif 'play spotify' in query:
            webbrowser.open("spotify.com")

        elif 'open spotify' in query:
            os.startfile("spotify")

        elif 'what time is it' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            talking(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'studio code' in query:
            os.startfile(r"C:\Users\IT\AppData\Local\Programs\Microsoft VS Code\Code.exe")
            talking('opening visual studio code, ser')

        elif 'open bitcoin' in query:
            webbrowser.open("https://id.tradingview.com/chart/?symbol=BINGX%3ABTCUSDT")

        elif 'play song' in query:
            song = query.replace("play song", "")
            talking('playing' + song)
            print('playing' + song)
            pywhatkit.playonyt(song)

        elif 'exit' in query:

            talking("thank you for using me")
            if jam >= 6 and jam < 12:
                talking(f"have a nice morning {master}")

            elif jam >= 12 and jam <= 18:
                talking(f"have a nice  day {master}")

            else:
                talking(f"good night {master}")
            exit()

        elif 'code web' in query:
            os.startfile(r"C:\Users\IT\AppData\Local\Programs\Microsoft VS Code\Code.exe")
            os.startfile("XAMPP Control Panel")

        elif 'stand by' in query:
            try:
                while True:
                    sleeping = query.replace("stand by", "")
                    sleeping_minute = sleeping * 60
                    sleep = ("ok i'll be stand by for" + sleeping_minute + "minute")
                    time.sleep(sleeping_minute)
                    talking(f"hey already sillent for " + sleeping_minute + "minute")
            except KeyboardInterrupt:
                pass
