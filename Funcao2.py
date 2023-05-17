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
            if texto == "Qual o endereço da FIAP":
                robo = pyttsx3.init()
                robo.setProperty('rate', 150)
                robo.setProperty('volume', 1.0)
                robo.say(f"Qual unidade?")
                robo.runAndWait()
                if texto == "Vila Olimpia":
                    robo = pyttsx3.init()
                    robo.setProperty('rate', 150)
                    robo.setProperty('volume', 1.0)
                    robo.say(f"Rua Fidêncio Ramos, número 308")
                    robo.runAndWait()
                if texto == "Paulista":
                    robo = pyttsx3.init()
                    robo.setProperty('rate', 150)
                    robo.setProperty('volume', 1.0)
                    robo.say(f"Avenida Paulista, número 1106")
                    robo.runAndWait()
                if texto == "Aclimação":
                    robo = pyttsx3.init()
                    robo.setProperty('rate', 150)
                    robo.setProperty('volume', 1.0)
                    robo.say(f"Avenida Lins de Vasconcelos, número 1264")
                    robo.runAndWait()
                else:
                    robo = pyttsx3.init()
                    robo.setProperty('rate', 150)
                    robo.setProperty('volume', 1.0)
                    robo.say(f"Unidade não encontrada")
                    robo.runAndWait()

        print(texto)
