import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import random

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 175)


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
                voice = listener.listen(source, phrase_time_limit=5)
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
        print('playing ' + song)
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = f"the current time is {datetime.datetime.now().strftime('%I:%M %p')}"
        print(time)
        talk(time)

    elif 'i want to know about something' in command:
        print("Enter the topic you want to know about")
        talk("Enter the topic you want to know about")
        person = input(">>>")
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)

    elif 'joke' in command:
        file = ['''Why can’t Elsa from Frozen have a balloon?. Because she will “let it go, let it go”. ''',
                'Why did the kid bring a ladder to school?. Because she wanted to go to high school.',
                'What do you call a dog magician?. A labracadabrador.',
                'Where would you find an elephant?. The same place you lost her.',
                'How are false teeth like stars?. They come out at night.',
                'What building in your town has the most stories?. The public library.',
                'What is a computer’s favorite snack?. Computer chips.',
                'How do we know that the ocean is friendly?. It waves.',
                'What animal is always at a baseball game?. A bat.',
                'What falls in winter but never gets hurt?. Snow.',
                'Why was the baby strawberry crying?. Because her mom and dad were in a jam.',
                'How do you make a lemon drop?. Just let it fall.',
                'Why does a seagull fly over the sea?. Because if it flew over the bay, it would be a baygull.',
                'What kind of tree fits in your hand?. A palm tree.',
                'Why did the teddy bear say no to dessert?. Because she was stuffed.',
                'Why did the student eat his homework?. Because the teacher told him it was a piece of cake.',
                'What’s the one thing will you get every year on your birthday?. A year older.',
                'What does every birthday end with?.The letter Y.',
                "Why is the obtuse triangle always so frustrated?. Because it’s never right.",
                "Why was the equal sign so humble?. Because he wasn’t greater than or less than anyone else.",
                "How do you stay warm in any room?. Go to the corner it’s always 90 degrees.",
                'Why was the math book sad?. Because it had too many problems.',
                'How do you make an octopus laugh?. With ten-tickles.']
        joke = random.choice(file)
        print(joke)
        talk(joke)

    else:
        print("Sorry, Couldn't hear you properly")
        talk("Sorry, Couldn't hear you properly")
        run_ultron()


run_ultron()
