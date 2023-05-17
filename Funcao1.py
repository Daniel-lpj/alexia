import speech_recognition as sr
import requests
import pyttsx3
from datetime import datetime
from pytz import timezone

microfone = sr.Microphone()
reconhecedor = sr.Recognizer()

with microfone as mic:
    while True:
        reconhecedor.adjust_for_ambient_noise(mic)

        audio = reconhecedor.listen(mic)
        texto = reconhecedor.recognize_google(audio, language='pt')
        print(texto)
        if texto == "sexta-feira" or texto == "cesta" or texto == "sexta":
            print("No que posso ajudar?")
            audio = reconhecedor.listen(mic)
            texto = reconhecedor.recognize_google(audio, language='pt')
            print(texto)
            if texto == "Quando é seu aniversário":
                robo = pyttsx3.init()
                robo.setProperty('rate', 150)
                robo.setProperty('volume', 1.0)
                robo.say(f"Nasci no dia 15/05, fui criada pelos alunos da FIAP")
                robo.runAndWait()

        print(texto)
