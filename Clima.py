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
            if texto == "Como está o clima":
                API_KEY = "fc794327278b692f30a3cc8b881d223b"
                cidade = "são paulo"
                link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

                requisicao = requests.get(link)
                requisicao_dic = requisicao.json()

                descricao = requisicao_dic['weather'][0]['description']

                temperatura = requisicao_dic['main']['temp']

                temperatura_celsius = int(temperatura - 273)
                humidade = requisicao_dic['main']['humidity']
                robo = pyttsx3.init()
                robo.setProperty('rate', 150)
                robo.setProperty('volume', 1.0)
                robo.say(
                    f"O céu em São Paulo está {descricao}, a temperatura é de {temperatura_celsius}°C, e a humidade do ar está em {humidade}%")
                robo.runAndWait()
            if texto == "Que horas são":
                data_e_hora_atuais = datetime.now()
                fuso_horario = timezone('America/Sao_Paulo')
                data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(
                    fuso_horario)
                data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime(
                    '%H:%M')

                robo = pyttsx3.init()
                robo.setProperty('rate', 150)
                robo.setProperty('volume', 1.0)
                robo.say(
                    f"Agora são {data_e_hora_sao_paulo_em_texto}")
                robo.runAndWait()

        print(texto)
