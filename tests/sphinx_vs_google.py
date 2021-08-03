# Import libraries

import speech_recognition as sr
import datetime

r = sr.Recognizer()

# Get the default microphone
with sr.Microphone() as source:
    # Listens to a command, using AVD
    while True:
        audio = r.listen(source)

        # Recognizes speech using Google as a service: online, slow.
        google = r.recognize_google(audio)
        sphinx = r.recognize_sphinx(audio)

        print(f'Google: [{google}]\nSphinx: [{sphinx}]\n\n')
