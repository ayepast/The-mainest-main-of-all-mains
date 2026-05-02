import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator

lan = "en"

print("Выберите язык для перевода:")
print("en — Английский")
print("zh — Китайский (мандарин)")
print("hi — Хинди")
print("es — Испанский")
print("ar — Арабский")
print("bn — Бенгальский")
print("pt — Португальский")
print("ja — Японский")
print("de — Немецкий")
lan = input()

duration = 5  # секунды записи
sample_rate = 44100

print("Говори...")
recording = sd.rec(
  int(duration * sample_rate),
  samplerate=sample_rate,  
  channels=1,            
  dtype="int16")       
sd.wait() 

wav.write("output.wav", sample_rate, recording)
print("Запись завершена, теперь распознаём...")

recognizer = sr.Recognizer()

with sr.AudioFile("output.wav") as source:
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio, language="ru-RU")
    print("Ты сказал:", text)
    translator = Translator()
    translated = translator.translate(text, dest=lan) 
    print(f"🌍 Перевод на {lan}:", translated.text)
except sr.UnknownValueError:    
    print("Не удалось распознать речь.")
except sr.RequestError as e:  
    print(f"Ошибка сервиса: {e}")
