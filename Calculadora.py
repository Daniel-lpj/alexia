import speech_recognition as sr

reconhecedor = sr.Recognizer()
microfone = sr.Microphone()

while True:
    try:
        with microfone as mic:
            reconhecedor.adjust_for_ambient_noise(mic)
            print('Fale a conta que deseja calcular...')
            audio = reconhecedor.listen(mic)
            texto = reconhecedor.recognize_google(audio, language='pt')
            print(texto)
            conta = texto.split()
            if conta[1] == '+':
                print(float(conta[0]) + float(conta[2]))
            elif conta[1] == '-':
                print(float(conta[0]) - float(conta[2]))
            elif conta[1] == 'x':
                print(float(conta[0]) * float(conta[2]))
            elif conta[1] == '/' and float(conta[2] != 0):
                print(float(conta[0]) / float(conta[2]))

    except:
        print('Bugou')