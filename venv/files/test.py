import pyttsx3

def listen(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 120)
    engine.say(text)
    engine.runAndWait()
    engine.stop()