import pyttsx3
import datetime
import time
import speech_recognition as sr
import microphone
import wikipedia
import webbrowser
import os,sys
import random
import pyjokes
from tkinter import *
import pywhatkit as pwt
from pygame import mixer 
import keyboard
import pywhatkit.whats

global uname
uname='utkarsh'

My_joke = pyjokes.get_joke(language="en", category="all")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)


engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',200)
def username():
    
    speak("What should i call you sir")
    uname=takecommand()
    speak("Hi "+uname)
    print("Hi "+uname)


def shutdown():
    speak("bye bye !"+uname)
    sys.exit()
    
   

    

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
            speak("good morning!" +uname)
    elif hour>=12 and hour<18: 
            speak("good Afternoon! " +uname)
    else:
            speak( "good evening ! "+uname)


    print("I Am ERA, how can i help you sir?")
    speak("I Am ERA, Version 1.0 developed by "+uname)
    speak("How can i help you sir?")
   

def takecommand():
  
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...!")
        mixer.init()
        mixer.music.load("mic start.mp3")
        mixer.music.play()
        r.pause_threshold = 1
        r.energy_threshold= 100000
        audio = r.listen(source)
    
    try:
        print("recognizing.....")
        mixer.init()
        mixer.music.load("recognize.mp3")
        mixer.music.play()
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}\n")

    
    except Exception as e:
        #print(e)
        print("say that again please...")
        speak("say that again please... ")
        return "None"
    return query

wishme()

def process():
 
  run=1   
  if __name__ == "__main__":

    while run==1 :
        
        
        query= takecommand().lower()
        path = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        run += 1 
    #logic fro exe

        if 'play kk song' in query:
            speak('playing kk songs for '+uname)
            webbrowser.open("https://www.youtube.com/watch?v=4P4Oa0pbZNQ&list=RDEMXATXP62QJBEM2wmydMdcbA&start_radio=1")

        elif 'wikipedia' in query:
            speak('Searching wikipidia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=3)
            webbrowser.open("{qury}")
            wikipedia_screen(results)
            speak("According to wikipedia")
           
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open("www.youtube.com")

        elif 'play music' in query:
            speak("playing music")
            Music_dir = 'E:\\Music\\Marathi dj'
            songs =os.listdir(Music_dir)
            print(songs)
            i=random.randrange(0,10)
            os.startfile(os.path.join(Music_dir,songs[i]))
        
        elif 'the time' in query :
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(F"sir the time is {strTime}\n")
            print(strTime)

        elif 'open code' in query:
            speak('opening code')
            path = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            opc = os.startfile(path)

        elif 'close window' in query:
            speak('closing window')
            sys.exit(path)
      
        
        elif 'open word' in query:
            speak('opening word')
            path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word 2016"
            os.startfile(path)

        elif 'open powerpoint' in query:
            speak('opening powerpoint')
            path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint 2016"
            os.startfile(path)
        
        elif 'open excel' in query:
            speak('opening excel')
            path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel 2016"
            os.startfile(path)

        elif 'open chrome' in query:
            speak('opening chrome')
            path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome"
            os.startfile(path)

        elif 'open paint' in query:
            speak('opening paint')
            path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Paint"
            os.startfile(path)


        elif 'open google' in query:
            speak('opening google')
            webbrowser.open("www.google.com")

        
        elif 'open spotify' in query:
            speak('opening spotify')
            webbrowser.open("www.spotify.com")

        elif 'how are you' in query:
            speak("i am fine what about you ?")
            
        elif 'i am fine' in query:
            speak("nice,be always happy in your life")
        
        elif 'not' in query:
            speak('share your problem with me if you ok to share')
        
        elif 'about you' in query:
            speak('I am voice assistence for pc or deskstop application. Utkarsh Karale creted era voice assistance, he is computer science student.')
        
        elif 'joke' in  query:
            print(My_joke)
            speak(My_joke)
       
        elif 'search ' in query:
            query=query.replace("search ","")
            speak("Here some result from web")
            pwt.search(query)

        elif 'change my name' in query:
            username()
        
        elif 'shutdown' in query:
            shutdown()

        elif 'what is my name' in query:
            speak("your good name is "+uname)
            print("your good name is "+uname)

        elif 'happy new year' in query :
            speak("happy new year "+uname) 
            pwt.search("New Year's Eve 2022")

        elif 'i love you' in query:
            speak("i have boyfriend, so sorry"+uname)
            time.sleep(5)
            speak("you want leason a song, say  yes or no ")
            query=takecommand().lower()

            if 'yes' in query:
                 webbrowser.open("https://www.youtube.com/watch?v=JFT0d0UJWGk")
            else:
                webbrowser.open("https://www.youtube.com/watch?v=KwiDJclWo44")  
      
        
         
            
                
         
                
           
      
def wikipedia_screen(text):
    



  wikipedia_screen = Toplevel(gui_root)
  wikipedia_screen.title(text)

  message = Message(wikipedia_screen, text= text)
  message.pack()



         
def mainscreen():
    global gui_root
    gui_root=Tk()
    #w x H

    gui_root.geometry("412x635")
    gui_root.minsize(100,100)
    bg = PhotoImage(file = "1.png")
    gui_root.title("ERA DEKSTOP VOICE ASSISTANT")
  

    label1 = Label( gui_root, image = bg)
    label1.place(x = 0, y = 0)
    
    label2 = Label( gui_root, text = "ERA VOICE ASSISTANT ", bg="blue")
   
    label2.pack(pady=10)
    
    photo = PhotoImage(file = r"assistance1.png")
  

    photoimage = photo.subsample(6, 6)
  

    Button(gui_root, text = 'EXIT',command=shutdown).pack(side = BOTTOM)
    
    Button(gui_root, text = 'Click Me !', image = photoimage,compound = LEFT ,command=process,activebackground="gray").pack(side = BOTTOM)
    
    keyboard.add_hotkey("F4",process)
    # keyboard.add_hotkey("e",enter)


    

 


    # microphone_photo = PhotoImage(file = "assistance.png")
    # microphone_button = Button(image=microphone_photo,text="click here", command = process,compound=BOTTOM)
    # microphone_button.pack(pady=20)

    gui_root.mainloop()

mainscreen()

    
