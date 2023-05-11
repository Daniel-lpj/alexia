import speech_recognition as sr
import pyttsx3

def calculadora():
    reconhecedor = sr.Recognizer()

    alexa = pyttsx3.init()
    alexa.setProperty('rate', 150)
    alexa.setProperty('volume', 1.0)

    while True:
        try:
            with sr.Microphone() as mic:
                alexa.say("Fale a conta que deseja calcular...")
                alexa.runAndWait()
                reconhecedor.adjust_for_ambient_noise(mic)
                audio = reconhecedor.listen(mic)
                texto = reconhecedor.recognize_google(audio, language='pt')
                conta = texto.split()

                if conta[1] == '+':
                    print(float(conta[0]) + float(conta[2]))
                elif conta[1] == '-':
                    print(float(conta[0]) - float(conta[2]))
                elif conta[1] == 'x':
                    print(float(conta[0]) * float(conta[2]))
                elif conta[1] == '/' and float(conta[2] != 0):
                    print(float(conta[0]) / float(conta[2]))

        except sr.UnknownValueError:
            alexa.say("Não entendi oque você disse")
            alexa.runAndWait()

calculadora()