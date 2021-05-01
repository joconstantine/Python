import pyttsx3

engine_object = pyttsx3.init()

engine_object.setProperty('rate', 150)  # 200 words per min
engine_object.setProperty('voice', 'f1')  # voice format f1
engine_object.say('hello world')

engine_object.runAndWait()
