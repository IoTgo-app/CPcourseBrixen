
import speech_recognition as sr
import streamlit as st

r = sr.Recognizer()

#AUDIO_FILE = "sample_audio_short.wav"   #mp3 files are not supported
#AUDIO_FILE = "sample_audio_long.wav"    #these files are in files-section of Class06 folder, on MS Teams.
#https://github.com/rizMehdi/CPcourseBrixen/blob/main/speechrecog/sample_audio_long.wav

AUDIO_FILE="https://raw.githubusercontent.com/rizMehdi/CPcourseBrixen/main/speechrecog/sample_audio_long.wav"

#st.file_uploader("upload your audio file", type="audio/wav")


st.audio(AUDIO_FILE, format="audio/wav")


with sr.AudioFile(AUDIO_FILE.getvalue()) as source:
    audio = r.record(source)  # read the entire audio file

recognised_text= r.recognize_google(audio)

st.text('the text recognized from the audio seems to be: ')
st.text( recognised_text)
