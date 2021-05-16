import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import requests
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit 
import smtplib
import sys
import time
from bs4 import BeautifulSoup
import pyautogui
import pyjokes
from googletrans import Translator
import pygame
import wolframalpha
from pywikihow import search_wikihow
import phonenumbers
import instaloader
from twilio.rest import Client
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUi import Ui_MainWindow


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
newVoiceRate = 175
engine.setProperty('rate',newVoiceRate)


#text to speech
def speak(audio):

    engine.say(audio)
    print(audio)
    engine.runAndWait()




#for calculation
app = wolframalpha.Client("UHLRPR-T85W5GRV6T")


#To wish
def wish():
    hour = int(datetime.datetime.now().hour)
    speak("System initializing, Successfully connected to the satellite")
    if hour>=0 and hour<=12:
        speak("good morning sir")

    elif hour>12 and hour<18:
        speak("good afternoon sir")

    else:
        speak("good evening sir")
    speak("I am jarvis, Heavily programmed by Prajwal, please tell me how can i help you")

#for news update
def news():
    main_url= 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=3ae4390e85474194bcd4255e144ffa1c'

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first","second","third","fourth","fifth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")            

#random music
def Randommusic():
    path = "F:\\music\\English songs\\Random"  
    file = os.path.join(path, random.choice(os.listdir(path)))
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()          

    
#to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.login()
    server.sendmail('prajwalbhagwat2001@gmail.com', to, content)
    server.close()

def search_wikihow(query, max_results=10, lang="en"):
    return list(wikihow.search(query, max_results, lang))   
 
class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()    

    #To convert voice into text
    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source: 
            print("listneing....") 
            r.pause_threshold = 1
            audio = r.listen(source,timeout=2,phrase_time_limit=5) 

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")

        except Exception as e:
          #speak("Say that again please...")
          return "none"
        query = query.lower()
        return query


    
    def TaskExecution(self):
        wish()
        while True:
        
            self.query = self.takecommand().lower()

            #Logic building for tasks

            if "open notepad" in self.query:
                npath = "C:\\WINDOWS\\system32\\notepad.exe"
                os.startfile(npath)

            elif "what can you do" in self.query:
             speak("I can do lot of things, for example you can ask me time, date, weather, I can send emails, messages, also i can make a call to anybody with an international number. I can open websites for you, launch applications, and can do many more things that humans cannot do")

            elif "how are you" in self.query:
             speak("I am fine , how can I help you sir") 

            elif "thank you" in self.query:
             speak("It's my pleasure sir, always ready to help you sir")


            elif "open command prompt" in self.query:
                os.system("start cmd")    
            
            elif"open whatsapp" in  self.query:
                apath = "C:\\Users\\DELL\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
                os.startfile(apath)

            elif "temperature" in self.query:
                search = "temperature in mumbai"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(f"current {search} is {temp}")
           
              
            elif "calculate" in  self.query:
                speak("what should i calculate?")
                gh= self.takecommand().lower()
                res = app.query(gh)
                speak(next(res.results).text)

            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0) 
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitkey(50)
                    if k==27:
                        break;
                cap.release()
                cv2.destroyAllWindows()   


            elif 'play the song' in   self.query:
                song= self.query.replace('play','')
                speak('playing' +song)
                pywhatkit.playonyt(song)
    
            elif 'time' in   self.query:
                time= datetime.datetime.now().strftime(' %I: %M %p ')   
                speak('time is' + time) 
            
            elif "tell me the date" in  self.query:
             time()
            
            elif "ip address" in   self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")

            elif "wikipedia" in   self.query:
                person = self.query.replace("wikipedia","")
                info= wikipedia.summary(person, sentences=1)
                speak("searching wikipedia")
                speak(info)

            elif 'are you single' in   self.query:
                speak('I am in Relationship with wifi')
            

            elif "open youtube" in   self.query:
                webbrowser.open("www.youtube.com")

            elif "open google" in   self.query:
                speak("sir, what should i search on google")
                cm = self.takecommand().lower()
                webbrowser.open(f"{cm}")

            elif "open facebook" in  self.query:
                webbrowser.open("https:\\www.facebook.com")
                speak("opening facebook..")

            elif "open maps" in  self.query or "show my location" in  self.query:
                webbrowser.open("https://www.google.co.in/maps/@19.2855223,72.876081,16z?hl=en") 
                speak("opening maps")   

            elif "send message" in   self.query:
                pywhatkit.sendwhatmsg("+918928239769", "this is testing protocol",16,44)

            elif "who made you" in self.query or "who created you" in self.query:
                speak("I have been created by Prajwal.")



            elif "email to prajwal" in   self.query:
                try:
                    speak("what should i say?")
                    content = self.takecommand().lower()
                    to = "prajwalbhagwat2001@gmail.com"
                    sendEmail(to,content)
                    speak("Email has been sent to prajwal")

                except Exception as e:
                    print(e)
                    speak("sorry sir, i am not able to sent this male to prajwal")

                
            elif "you can sleep jarvis" in  self.query:
                speak("thanks for using me sir, you can call me anytime.")
                sys.exit()   

            

           #to close any application
        
            elif "close notepad" in   self.query:
                speak("okay sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")

            elif "close command prompt" in   self.query:
                speak("okay sir, closing command prompt")
                os.system("taskkill /f /im cmd.exe")  

            elif "close facebook" in self.query:
                speak("okay sir, closing facebook and youtube")
                os.system("taskkill /f /im  msedge.exe")


           # to set an alarm
            elif "set alarm" in  self.query:
                nn = int(datetime.datetime.now().hour)
                if nn==22:
                    music_dir = 'F:\music\English songs\Random'
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir,songs[0]))

         # to find joke
            elif "tell me a joke" in  self.query:
                joke = pyjokes.get_joke()
                speak(joke)            

            elif "shut down the system" in  self.query:
                os.system("shutdown /s /t 5")

            elif "restart the system" in   self.query:
                os.system ("shutdown /r /t 5")

            elif "sleep the system" in  self.query:
                os.system ("rund1132.exe powerproof.dll,SetSuspendState 0,1,0") 

            elif "play your favourite music" in  self.query:
                Randommusic()

            elif "pause music" in  self.query:
                pygame.mixer.music.pause()    


            elif "activate how to do mod" in  self.query:
                from pywikihow import search_wikihow
                speak("How to do mode is activated, please tell me what you want to know")
                how = self.takecommand()
                max_results = 1
                how_to = search_wikihow(how, max_results)
                assert len(how_to) == 1
                how_to[0].print()
                speak(how_to[0].summary)     

            elif "trace the phone number" in  self.query:
                from phonenumbers import geocoder,carrier
                speak("which phone number you want to trace sir")
                a = self.takecommand().lower()
                result = phonenumbers.parse(f"{'+91'+ a}")
                Carrier = carrier.name_for_number(result, 'en')  
                Region = geocoder.description_for_number(result, 'en') 
                speak(Carrier)
                speak(Region)

            elif "switch the window" in  self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab") 
                pyautogui.keyUp("alt")

            elif "tell me the news" in  self.query:
                speak("please wait sir, fetching the latest news")
                news()   

            elif "where i am" in  self.query or "where we are" in  self.query:
                speak("wait sir, let me check") 
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    country = geo_data['country'] 
                    speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
                except Exception as e:
                    speak(("sorry sir, due to network issue i am not able to find where we are."))          
                    pass

            #To check instagram profile
            elif "show me instagram profile" in  self.query or "instagram profile" in  self.query:
                speak("sir, please enter the username correctly.")
                name = input("Enter username here:")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"Sir here is the profile of the user {name}")
                time.sleep(5)
                speak("sir would you like to download profile picture of this account.")
                condition = self.takecommand().lower()
                if "yes" in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only=True)
                    speak("i am done sir, profile picture is saved in your main folder. now i am ready for next command")
                else:
                    pass   
                

            # to take screenshot
            elif "take screenshot" in  self.query or "take a screenshot" in  self.query:
                speak("sir,please tell me the name for this screenshot file")
                name = self.takecommand().lower()
                speak("please sir hold the screen for few seconds , i am taking screenshot")
                img = pyautogui.screenshot()
                img.save(f"{name}.png")    
                speak("i am done sir , the screenshot is saved in our main folder. now i am ready for the next command")
         
           #to hide files and folders
            elif "hide all files" in self.query or "hide this folder" in self.query or "visible for evryone" in self.query:
             speak("sir please tell me you want to hide this folder or make it visible for everyone")
             condition = takecommand().lower()
             if "hide" in condition:
                os.system("attrib +h /s /d")
                speak("sir, all the files in this folder are now hidden.")

             elif "visible" in condition:
                os.system("attrib -h /s /d")
                speak("sir, all the files in this folder are now visible to everyone.")

             elif "leave it" in condition or "leave for now" in condition:
                speak("ok sir")                

            
            elif"send text message"in self.query:
             speak("what should i send sir")
             msz = self.takecommand()

             account_sid = 'AC00d737b253a207ff8e8f936a1ef3d1c5'
             auth_token = 'a7fab5ab25e0b846ee1084d1f070c8b4'
             client = Client(account_sid, auth_token)

             message = client.messages \
                    .create(
                    body=msz,
                    from_='+19292654987',
                    to='+918928239769'
                    )
             speak("Message has been sent sir, waiting for your next command")

            elif"make a phone call"in self.query:
            

             account_sid = 'AC00d737b253a207ff8e8f936a1ef3d1c5'
             auth_token = 'a7fab5ab25e0b846ee1084d1f070c8b4'
             client = Client(account_sid, auth_token)

             message = client.calls \
                .create(
                twiml='<Response><Say>This is the testing message from Jarvis side..</Say></Response>',
                from_='+19292654987',
                to='+918928239769'
                )   
             speak("Phone call has been made sir, waiting for your next command")
            
            elif "how much power is left" in self.query or "how much power we have" in self.query or "battery" in self.query:
                import psutil
                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f" Sir our system have {percentage} percent battery")
                if percentage>=75:
                    speak("We have enough power to continue our work")
                elif percentage>=40 and percentage<=75:
                    speak("we should connect our system to charging point to charge our battery")
                elif percentage<=15 and percentage<=30:
                    speak("we don't have enough power to work, please connect to charging")
                elif percentage<=15:
                    speak("we have very low power, please connect to charging the system will shutdown very soon")
                                

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
       self.ui.movie = QtGui.QMovie("C:/Users/DELL/Desktop/Python/jarvis.gif/7LP8.gif")
       self.ui.label.setMovie(self.ui.movie)
       self.ui.movie.start() 
       self.ui.movie = QtGui.QMovie("C:/Users/DELL/Desktop/Python/jarvis.gif/Jarvis_Loading_Screen.gif")
       self.ui.label_2.setMovie(self.ui.movie)
       self.ui.movie.start()  
       self.ui.movie = QtGui.QMovie("C:/Users/DELL/Desktop/Python/jarvis.gif/iron-man-wallpaper-gif-2.gif")
       self.ui.label_3.setMovie(self.ui.movie)
       self.ui.movie.start() 
       timer = QTimer(self)
       timer.timeout.connect(self.showTime)
       timer.start(1000)
       startExecution.start()

    def showTime(self):
      while True:
       QApplication.processEvents()     
       current_time = QTime.currentTime()
       current_date = QDate.currentDate()
       label_time = current_time.toString('hh:mm:ss')
       label_date = current_date.toString(Qt.ISODate)  
       self.ui.textBrowser.setText(label_date)
       self.ui.textBrowser_2.setText(label_time) 


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())

if_name_=='__main__'
while True:
    permission = self.takecommand().lower()
    if "jarvis" in permission:
      MainThread.TaskExecution()
    elif"goodbye" in permission:
      sys.exit()   
