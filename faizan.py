import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = aa.Recognizer()

machine = pyttsx3.init()

def talk(text):
         machine.say(text)
         machine.runAndWait()

def input_instruction():
    global instruction

    try:
        with aa.Microphone() as origin:
             print("listening...")
             speech = listener.listen(origin)
             instruction = listener.recognize_google(speech)
             instruction = instruction.lower()
             if"faizan" in instruction:
                instruction = instruction.replace('faizan',' ')
                print(instruction)
      
    except:
        pass        

    return instruction

def play_faizan():

    instruction = input_instruction()
    print(instruction)
    if "play" in instruction:
         song = instruction.replace('Play'," ")
         talk("Playing" + song)
         pywhatkit.playonyt(song)

    elif 'time' in instruction: 
         time = datetime.datetime.now().strftime('%I:%M%p')
         talk('Current time' + time)

    elif 'date' in instruction:
         date = datetime.datetime.now().strftime('%d /%m /%Y')
         talk("Today's date" + date)

    elif 'how are you' in instruction:
         talk('I am Fine, how about you')

    elif 'Waht is your name' in instruction:
         talk('I am Faizan, What can I do for you?')

    elif 'joke' in instruction:
         talk(pyjokes.get_joke())    

    elif 'Who is ' in instruction:
         human = instruction.replace('Who is', " ")
         info = wikipedia.summary(human, 1)
         print(info)
         print(talk)
    else:
         talk('Please fir se bolo..')                    
play_faizan()         