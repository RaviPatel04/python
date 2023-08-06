# Shutil Module

import shutil
import os

# shutil.copy("23.txt","43.txt") #copy content of file
# shutil.copytree("pthon", "new")#copy folder
# shutil.move("python/23.txt","23.txt")
# os.rename("23.txt")

# ----------------------------------------------------------------------------------

# text to speech in python

# using pyttsx3
import pyttsx3

# initialisation
speak = pyttsx3.init()

# testing
speak.say("Hello friends!! My self ravi patel")
speak.say("I study in computer engineering")

for i in range(1,11):
    speak.say(f"4 {i}zaa {4*i}")

speak.runAndWait()
speak.stop()

# ---------------------------------------------------------------------------------------

# # using win32
# from win32com.client import Dispatch

# speak = Dispatch("SAPI.SpVoice").Speak

# speak("Hello friends!! My self ravi patel")