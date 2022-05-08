
import speech_recognition as sr
import streamlit as st
import requests   

r = sr.Recognizer()

#AUDIO_FILE = "sample_audio_short.wav"   #mp3 files are not supported
#AUDIO_FILE = "sample_audio_long.wav"    #these files are in files-section of Class06 folder, on MS Teams.
#https://github.com/rizMehdi/CPcourseBrixen/blob/main/speechrecog/sample_audio_long.wav

AUDIO_FILEurl="https://raw.githubusercontent.com/rizMehdi/CPcourseBrixen/main/speechrecog/sample_audio_long.wav"
AUDIO_FILEdata = requests.get(AUDIO_FILEurl)

#st.file_uploader("upload your audio file", type="audio/wav")


st.audio(AUDIO_FILEurl, format="audio/wav")

with open(AUDIO_FILEurl, 'rb') as f:
    with sr.AudioFile(f) as source:
        audio = r.record(source)  # read the entire audio file

    
recognised_text= r.recognize_google(audio)

st.text('the text recognized from the audio seems to be: ')
st.text( recognised_text)
