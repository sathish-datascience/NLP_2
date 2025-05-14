from gtts import gTTS
from playsound import playsound

audio2 = "test2.mp3"

sp = gTTS("hello everyone welcome to python program",lang="en")
sp.save(audio2)


playsound(audio2)