import speech_recognition as sr
#para escolher qual microfone usar, rode:
for i, mic in enumerate(sr.Microphone().list_microphone_names()):
    print (i, mic)

# Criar um Reconhecedor

rec = sr.Recognizer()


# Ouvir o Audio do Microfone
with sr.Microphone() as microfone:
    rec.adjust_for_ambient_noise(microfone) #tratamento do ruido
    print("Pode começar a falar: ")
    #rec.pause_threshold() = 5 #coloque isso que quiser colocar um tempo ocioso para encerrar a captura
    audio = rec.listen(microfone) #pegando o som do microfone
try:
    # reconhece esse audio e traduz ele para texto
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)
except:
    print("Não consegui entender")