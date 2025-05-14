import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
	print("say something")
	recognizer.adjust_for_ambient_noise(source)
	audio = recognizer.listen(source)

try:
	print("You said : " + recognizer.recognize_google(audio))

except:
	print("error")