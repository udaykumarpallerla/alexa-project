#part1:Take user voice an convert it to text
#part2:process the next an give some result
#part3:convert result(text) into voice

#part1(speech regonition)

import speech_recognition as sr
import pyaudio
import pyttsx3
import pywhatkit
import wikipedia
from datetime import datetime
import pyjokes

def talk(answer):
      engine=pyttsx3.init()
      voices=engine.getProperty('voices')
      engine.setProperty('voice',voices[1].id)
      engine.say(answer)
      engine.runAndWait()

def processQuestion(question):
      if'what are you doing'in question:
              print('i am waiting for your question')
              talk('i am waiting for your question')
              return True
           
      elif 'how are you' in question:   
              print('I am good,thank you.How can I Help you')
              talk('I am good,thank you.How can I Help you')
              return True

      elif 'play' in question:
              question=question.replace('play','')
              pywhatkit.playonyt(question)
              return True
      
      elif 'who is' in question:
              question=question.replace('who is','')
              print(wikipedia.summary(question,1))
              talk(wikipedia.summary(question,1))
              return True

      elif "time" in question:
             time= datetime.today().time().strftime("%I:%M %p")
             print(time)
             talk(time)
             return True

      elif "joke" in question:
              joke=pyjokes.get_joke()
              print(joke)
              talk(joke)
              return True
      else:
            print("i didn't get your question,can you say that again")


def getquestion():
     r=sr.Recognizer()

     with sr.Microphone() as source:
               print('say something')
               audio=r.listen(source)

     try:
          print(r.recognize_google(audio))
          question=r.recognize_google(audio)
          if'Alexa' in question:
               question=question.replace('Alexa','')
               print(question)
               return question
          
          elif "bye" in question:
                 talk('bye,please take care.will meet you later')
                 return False
                    
          else:
               print('your not talking with me,please carry on')
               return True

     except sr.UnknownValueError:
               print('sorry i cant get your question')
               return "notwithme"
          
canAskQuestion=True
while canAskQuestion:
       question=getquestion()
       if(question=="notwithme"):
              talk("ok carry on with your friends,bye!")
              canAskQuestion=False
else:
     canAskQuestion=processQuestion(question)
