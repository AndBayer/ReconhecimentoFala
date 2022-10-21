import time
import speech_recognition as sr

def tratar_audio(rec, audio):
    global acabou
    # tratar o meu audio
    try:
        texto = rec.recognize_google(audio, language="pt-BR")
        print(texto)
        # Aqui a linha que voce da os comandos necessários para executar o que voce quiser
        if "encerrar gravação" in texto:
            acabou = True
    except:
        print("Não reconheci")

acabou = False

rec = sr.Recognizer()

with sr.Microphone() as microfone:
    rec.adjust_for_ambient_noise(microfone)
    #rec.pause_threshold = 0.5
    # Ajusta a diferença do volume da sua voz para ruídos
    #rec.dynamic_energy_adjustment_ratio = 2
    print("Pode começar a falar:")

# Multi thread - Ele roda em paralelo com seu código, ele continua o código e fica rodando de fundo
# Thread 1
parar_ouvir = rec.listen_in_background(microfone, tratar_audio)

# Thread 2
while True:
    time.sleep(0.1)
    # Falar para ele encerrar a gravação
    if acabou == True:
        break

# Thread 1
parar_ouvir(wait_for_stop=False)

