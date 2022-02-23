import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 165)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    loop = True
    print("Hi im Ultron, What can I do for you?")
    talk("Hi im Ultron, What can I do for you?")
    while loop:
        try:
            with sr.Microphone() as source:

                print('listening...')
                voice = listener.listen(source, phrase_time_limit=4)
                cmd = listener.recognize_google(voice)
                cmd = cmd.lower()
                if 'ultron' in cmd:
                    cmd = cmd.replace('ultron', '')
                    loop = False

        except:
            print("Sorry, Couldn't hear you properly")
            talk("Sorry, Couldn't hear you properly")
    return cmd


def run_ultron():
    command = take_command()
    if "play" in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = f"the current time is {datetime.datetime.now().strftime('%I:%M %p')}"
        print(time)
        talk(time)

    elif 'tell me about' in command:
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 2  )
        print(info)
        talk(info)

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    else:
        print("Sorry, Couldn't hear you properly")
        talk("Sorry, Couldn't hear you properly")
        run_ultron()


run_ultron()
