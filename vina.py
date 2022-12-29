import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from instabot import Bot

engine= pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    '''To speak whatever data is send to it.'''
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    '''To greet according to the time'''
    hour= int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am vina. Please tell me how may I help you")

def takeCommand():
    '''It takes microphone input from the user and returns string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
def sendEmail(to,content):
    server = smtplib.SMTP('smntp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your-password-here')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")
        
    except Exception as e:
        #print(e)

        print("Say that again please....")
        return "None"
    return query


if __name__== "__main__":
    wishMe()
    while(True):
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            try:
                query =query.replace("wikipedia","")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak("Can't find it.... please speak again")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'play music' in query:
            music_dir = #you fav music directory path here
            songs = os.listdir(music_dir)
            print(songs)
            os.start file(os.path.join(music_dir,songs[0])) 

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        
        elif 'open code' in query:
            codePath = "C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak("what should I send")
                content = takeCommand()
                speak("to which email id you want to send")
                #to = "yourEmail@gmail.com"
                to = takeCommand()
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print (e)
                speak("sorry my friend email is not sent")


        

    #logic for executing tasks based on query
