import pyttsx3 # pip install pyttsx3
import datetime # pip install datetime
import speech_recognition as speech_r #pip install SpeechRecognition
import wikipedia # pip install wikipedia
import pyjokes # pip install pyjokes


machine = pyttsx3.init()

def speak(text): # text to speech
     machine.say(text)
     machine.runAndWait()

def time(): # get the time
     hour = int(datetime.datetime.now().hour)
     minute = int(datetime.datetime.now().minute)
     if minute == 0:
          minute = ""
     if hour > 12:
          hour -= 12
          speak(f"it's {hour} {minute} P M")
     else:
          speak(f"it's {hour} {minute} A M")

def date(): # get the date month and year
     year = int(datetime.datetime.now().year)
     month = int(datetime.datetime.now().month)
     day = int(datetime.datetime.now().day)
     month_list = ("", "january", "frbruary", "march", "april", "may", "june","july","august","september","october","november","december")
     month = month_list[month] # month in number to normal month using list 
     speak(f"{day}th {month}, {year}") # the format is 5 th february 2022

def wishMe(): #greet me using the time
     hour = int(datetime.datetime.now().hour)
     if 6 <= hour < 12:
          messege = "Good Morning Sir!"
     elif 12 <= hour < 18:
          messege = "good afternoon sir!"
     elif 18 <= hour < 24:
          messege = "good afternoon sir!"
     else:
          messege = "Good night sir!"
     speak(messege)

def hear_me(): # voice to text
     clip = speech_r.Recognizer()

     with speech_r.Microphone() as source: # take the microphone as source
          print("Listening your command ...")
          clip.pause_threshold = 1
          voice = clip.listen(source) # anything we speak will store in voice
     
     try:
          print("Recognizing your voice ....")
          speech = clip.recognize_google(voice, language = 'en-bd') # convert the voice to text
          print(speech)
     
     except Exception as x: # if any error 
          print(x)
          speak("Sir, Can you please say that again....")
          return "none"
     return speech

def wiki_search(voice):# wikipedia summary of 2 line
     voice = voice.replace("wikipedia", "")
     sumry = wikipedia.summary(voice, sentences = 2) #2 line summary
     return sumry

def jokes(): #jokes function
     speak(pyjokes.get_joke())

if __name__ == "__main__":
     speak("Wellcome back")
     wishMe()
     speak("i am your personal assistant! How can i help you.")
     while True:
          voice = hear_me().lower()
          if 'time' in voice:
               time()
          elif "date" in voice:
               date()
          elif "wikipedia" in voice:
               speak("searching .....")
               print(wiki_search(voice))
               speak(wiki_search(voice))
          elif "joke" in voice:
               jokes()
          elif "offline" in voice:
               quit()
