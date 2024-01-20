import pyttsx3
import speech_recognition as sr
import functions
recognizer = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as mic:
            print("Say something : ")
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = text.lower()
            print(f"The text is: {text}")
            if (text=="hello"):
                functions.hello(text)
            elif(text=="create files"):
                functions.create_files(text)
            elif(text=="delete files"):
                functions.del_files(text)
            elif("send this message to" in text):
                functions.whatsapp(text)
            elif(text=="open vi talk" or text=="open v-top"):
                username_text=str(input("Enter your username : "))
                password_text=str(input("Input your password : "))
                functions.open_vtop(username_text,password_text)
            elif("search on" in text):
                functions.search(text)
    except sr.UnknownValueError:
        recognizer = sr.Recognizer()
        continue
