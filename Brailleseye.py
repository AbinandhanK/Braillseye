#Welcome

import pyttsx3
engine = pyttsx3.init()
engine.say("Hello")
engine.runAndWait()

#Read choices

import pyttsx3
engine = pyttsx3.init()
engine.say("How can I help ? ")
engine.runAndWait()

#Collecting user Choices

print("1. Listen time")
print("2. Open Programs")
print("3. Open URL")
print("4. Open News channel only in Tamil")
c = int(input("Enter a choice : "))

#Time

if c == 1:
    from datetime import datetime
    now = datetime.now()
    engine = pyttsx3.init()
    engine.say(now.strftime("%H:%M:%S"))
    print("The time is" ,now.strftime("%H:%M:%S"))
    engine.runAndWait()

#Opening applications

if c == 2 :
    
    #Voice commands for Programs
    
    import pyttsx3
    engine = pyttsx3.init()
    engine.say("What program do you want to open")
    engine.runAndWait()
    print("What program do you want to open ? ") 
    print("1. Google Chrome")
    print("2. VLC media player")
    print("3. Notepad")
    print("4. Word")
    print("5. Powerpoint")
    print("6. Microsoft Edge")
    choice = int(input("Enter a value : "))
    
    #To open Notepad
    
    if choice == 3 :
        import pyttsx3
        engine = pyttsx3.init()
        engine.say("Opening Notepad")
        engine.runAndWait()
        import subprocess
        subprocess.Popen("C:\\Windows\\System32\\notepad.exe")
    
    #To open Google Chrome
    
    if choice == 1 :
        import pyttsx3
        engine = pyttsx3.init()
        engine.say("Opening Google Chrome")
        engine.runAndWait()
        import os 
        os.startfile("chrome")

    #To open VLC Media player
    
    if choice == 2 :
        import pyttsx3
        engine = pyttsx3.init()
        engine.say("Opening VLC Media player")
        engine.runAndWait()
        import os
        os.startfile("vlc")
    
    #To open Microsoft word
    
    if choice == 4 :
        import pyttsx3
        engine = pyttsx3.init()
        engine.say("Opening Microsoft word")
        engine.runAndWait()
        import os 
        os.startfile("winword")
    
    #To open Microsoft Powerpoint
    
    if choice == 5 :
        import pyttsx3
        engine = pyttsx3.init()
        engine.say("Opening microsoft powerpoint")
        engine.runAndWait()
        import os
        os.startfile("powerpnt")
        
    #To open Microsoft Edge
    
    if choice == 6 :
        import pyttsx3
        engine = pyttsx3.init()
        engine.say("Opening microsoft Edge")
        engine.runAndWait()
        import os
        os.startfile("msedge")

#To Open URL's

if c == 3 :        
    a = input("Enter a URL : ")
    import webbrowser
    import pyttsx3
    engine = pyttsx3.init()
    engine.say("Opening",a)
    engine.runAndWait() 
    webbrowser.open(a)

#To open News channel

if c == 4 :
    import pyttsx3
    engine = pyttsx3.init()
    engine.say("Opening news channel")
    engine.runAndWait() 
    import webbrowser
    webbrowser.open("https://www.youtube.com/watch?v=brE317oWHXo")
        