# import pyttsx3


# engine = pyttsx3.init('sapi5')
# voices = engine.getproperty('voices')
# print(voices)
# print(voice[0].id)
# engine.setProperty('voice' , voice[0].id)


# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()


# 
# import pyttsx3

# engine = pyttsx3.init()

# voices= engine.getProperty('voices') #getting details of current voice

# engine.setProperty('voice', voices[0].id)
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init()
# engine.say("Hello Yukta!")
# engine.runAndWait()
voices= engine.getProperty('voices')
print(voices[7].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:

        speak("Good Afternoon!")

    else:

        speak("Good Evening!")

    speak("Hey! Enchantee. i'm happy to meet you? ")

def takeCommand():

    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=3, phrase_time_limit=3)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

if __name__== "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            # music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            # songs = os.listdir(music_dir)
            # print(songs)    
            # os.startfile(os.path.join(music_dir, songs[0]))
            engine.say(" Leave in peace leave in peace and let all leave in peace thankyou ")
            engine.runAndWait()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        # elif 'open code' in query:
        #     codePath = "/home/user/Desktop/Doremon/py1.py"
        #     os.startfile(codePath)

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('youremail@gmail.com', 'your-password')
#     server.sendmail('youremail@gmail.com', to, content)
#     server.close()


    takeCommand()

