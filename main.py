#Import packages
import pyttsx3
import speech_recognition as sr
import subprocess
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

#Import functions from folders
from worldtimepy import worldtime
from mathematics import basic_arithmetic as calculator
from scraper import DataSpider as weather
from reminder import reminder as reminder
from todo import todo as todo

#Initiate Text To Speech
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 125)

#Speak Function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Listen to user input
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        print("Processing")
        speak("Processing")
        query = r.recognize_google(audio, language='en-CA')

        #Send query to analyze for function
        #analyze(format(query))
        dissect(format(query))

        print("User said: {}".format(query))
    except sr.UnknownValueError:
        print("Unknown")
        speak("Unknown")
    except sr.RequestError:
        print("Error")
        speak("Error")
        return "None"
    return query

#Dissect each word, appending to array and then analyze
def dissect(speech):
    string = ""
    info = []
    index = 0
    for x in speech:
        if index < len(speech):
            index += 1
            if x != ' ':
                string += x
            elif x == ' ':
                info.append(string)
                string = ""
            if index >= len(speech):
                info.append(string)
                string = ""
    analyze(info)

def analyze(info):

    for x in info:
        if x == "calculate":
            print(x)
            # firstOperand = string.split()[1]
            # secondOperand = string.split()[3]
            # operator = string.split()[2]
            # print(calculator.basic_calculator(int(firstOperand), int(secondOperand), operator))
        if x == "time":
            print(x)
            # country = string.split()[1]
            # worldclock(country)
        if x == "weather":
            print(x)
            # subprocess.run(["scrapy", "runspider", "--nolog" ,"scraper/scaper.py"])
        if x == 'remind':
            title = input("What will the title be")
            time = input("When")
            #reminder.insert(title, time)
        if x == 'note':
            todo.dissect(info)
        

#World clock/time Function
def worldclock(string):
    flag = False
    hours = ""
    result = worldtime.WorldTime().search(string)
    time = worldtime.WorldTime().get_location(result)
    time = str(time)
    time = time.split()[1]
    time = time.split(".")
    time = time[0]

    #Convert 24 hours to 12 hours
    time = time.split(":")
    if int(time[0]) > 12 and int(time[0]) < 24:
        flag = True
        hours = int(time[0]) - 12


    newTime = ""
    if flag:
        newTime = hours, time[1], "pm"
    else:
        newTime = time[0], time[1], "am"

    print(newTime)
    speak(newTime)

dissect("note get milk")