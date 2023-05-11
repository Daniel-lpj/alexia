import speech_recognition as sr
import requests
import pyttsx3


def cotacao_dolar():
    recohecedor = sr.Recognizer()

    alexa = pyttsx3.init()
    alexa.setProperty('rate', 150)
    alexa.setProperty('volume', 1.0)

    with sr.Microphone() as source:
        alexa.say("Com oque posso ajudar?")
        alexa.runAndWait()
        audio = recohecedor.listen(source)

    try:
        text = recohecedor.recognize_google(audio, language='pt-BR')

        if "dólar" in text.lower():
            response = requests.get(
                'https://economia.awesomeapi.com.br/json/USD-BRL')
            data = response.json()[0]
            alexa.say(data['bid'])
            alexa.runAndWait()

        else:
            alexa.say("Comando não conhecido")
            alexa.runAndWait()
    except sr.UnknownValueError:
        alexa.say("Não entendi oque você disse")
        alexa.runAndWait()
    except sr.RequestError as e:
        print("Não foi possível obter a resposta do servidor; {0}".format(e))


cotacao_dolar()
