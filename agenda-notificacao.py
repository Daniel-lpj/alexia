import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound


def reconhecer_comando():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Diga 'Ok sexta-feira' para iniciar.")
        audio = r.listen(source)

    try:
        # Utilizando o serviço de reconhecimento da Google
        comando = r.recognize_google(audio, language='pt-BR')
        if "Ok sexta-feira" in comando:
            return True
        else:
            return False
    except sr.UnknownValueError:
        return False
    except sr.RequestError as e:
        print("Erro ao usar o serviço de reconhecimento da Google: {0}".format(e))
        return False


# Função para processar o comando de voz
def processar_comando():
    print("Sim, mestre. O que posso fazer?")
    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        comando = r.recognize_google(audio, language='pt-BR')
        print("Comando: ", comando)

        if "notificações" in comando:
            ler_notificacoes()
        elif "anotação" in comando:
            fazer_anotacao(comando)
        else:
            print("Comando não reconhecido.")

    except sr.UnknownValueError:
        print("Não entendi o comando. Por favor, repita.")
    except sr.RequestError as e:
        print("Erro ao usar o serviço de reconhecimento da Google: {0}".format(e))


# Função para ler notificações
def ler_notificacoes():
    print("Lendo notificações...")
    # Lê o arquivo de notificações
    with open("notificacoes.txt", "r") as file:
        notificacoes = file.readlines()

    if notificacoes:
        for notificacao in notificacoes:
            print(notificacao.strip())
            # Converte a notificação em fala e reproduz o áudio
            tts = gTTS(text=notificacao.strip(), lang='pt-br')
            tts.save("notificacao.mp3")
            playsound("notificacao.mp3")
            os.remove("notificacao.mp3")
    else:
        print("Não há notificações.")


# Função para fazer anotações
def fazer_anotacao(comando):
    anotacao = comando.replace("anotação", "")
    anotacao = anotacao.strip()

    if anotacao:
        print("Anotando: ", anotacao)

        # Adiciona a anotação ao arquivo de anotações
        with open("anotacoes.txt", "a") as file:
            file.write(anotacao + "\n")

        # Converte a confirmação em fala e reproduz o áudio
        tts = gTTS(text="Anotação feita com sucesso.", lang='pt-br')
        tts.save("anotacao.mp3")
        playsound("anotacao.mp3")
        os.remove("anotacao.mp3")
    else:
        print("Nenhuma anotação fornecida.")


# Loop principal
while True:
    if reconhecer_comando():
        processar_comando()
