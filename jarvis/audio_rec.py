import pyttsx3
import speech_recognition as sr
import functions
recognizer = sr.Recognizer()
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
while True:
    try:
        with sr.Microphone() as mic:
            print("Say something : ")
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio,language="en-IN")
            text = text.lower()
            print(f"The text is: {text}")
            if (text=="hello"):
                functions.hello(text)
            elif(text=="what time is it"):
                functions.get_time()
            elif(text=="create files"):
                functions.create_files(text)
            elif(text=="delete files"):
                functions.del_files(text)
            elif("send this message to" in text):
                functions.whatsapp(text)
            elif("search on" in text):
                functions.search(text)
            elif("turn off" in text or "restart" in text or "logout" in text):
                functions.turn(text)
            elif("open app" in text):
                functions.open_app(text)
    except sr.UnknownValueError:
        recognizer = sr.Recognizer()
        continue
