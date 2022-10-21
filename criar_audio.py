#Essa biblioteca reconhece audios: raw, wav, aiff, flac

import speech_recognition as sr

rec = sr.Recognizer()

with sr.Microphone(device_index=1) as microfone:
    rec.adjust_for_ambient_noise(microfone)
    print("Pode começar a falar")
    audio = rec.listen(microfone)

#salvar o audio
with open("audio.wav", "wb") as arquivo: #r = read, w = write
    arquivo.write(audio.get_wav_data())
