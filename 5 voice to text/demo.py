import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
	audio = recognizer.listen(source)

try:
	print(recognizer.recognize_google(audio))
	
except :
	print("error")