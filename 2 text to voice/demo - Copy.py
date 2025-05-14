
from gtts import gTTS
from playsound import Playsound

audio  = "otp.mp3"

sp = gTTS(text = f"your otp is {otp}",lang="eng")

sp.save(audio)

playsound(audio)
