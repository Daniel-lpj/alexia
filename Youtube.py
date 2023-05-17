import speech_recognition as sr
import pyttsx3
import requests
import json
import webbrowser

reconhecedor = sr.Recognizer()
alexa = pyttsx3.init()

# URL base da API
base_url = 'https://www.googleapis.com/youtube/v3/'


def play_music(query):
    # Montando a URL de busca da API do YouTube
    search_url = base_url + 'search?q=' + query + '&part=snippet&type=video&key=AIzaSyBI1fTGjwBWUtJWA_y-poSeKTelhPEhOK0'

    # Requisição da API
    response = requests.get(search_url)
    response_json = json.loads(response.text)

    video_id = response_json['items'][0]['id']['videoId']

    # Monta a URL do vídeo
    video_url = 'https://www.youtube.com/watch?v=' + video_id

    # Abri o vídeo no navegador padrão
    webbrowser.open(video_url)


# Função para reconhecer a voz do usuário
def reconhece_voz():
    with sr.Microphone() as mic:
        reconhecedor.adjust_for_ambient_noise(mic)
        alexa.say("O que posso fazer?")
        alexa.runAndWait()
        reconhecedor.adjust_for_ambient_noise(mic)
        audio = reconhecedor.listen(mic)
        query = reconhecedor.recognize_google(audio, language='pt')
        print('Você disse:', query)
        alexa.say('Tocando ' + query)
        alexa.runAndWait()
        play_music(query)


reconhece_voz()
