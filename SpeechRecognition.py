import speech_recognition
import speech_recognition as sr

recognizer = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration= 0.2)
            print("listening...")
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(text)

    except speech_recognition.UnknownValueError():
        recognizer = sr.Recognizer()
        continue