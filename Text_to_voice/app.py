# importing the pyttsx library
import pyttsx3

# initialisation
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)   #0- male voice, 1-female voice



# code for reading the .txt file
filename="text.txt"
text = open(filename).read()
text2 = text.lower()
text2

# code for text to speech conversion
engine.say(text2)
engine.say("welcome to github")
engine.runAndWait()
