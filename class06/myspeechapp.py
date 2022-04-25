#! python3
from googletrans import Translator
from gtts import gTTS 
import streamlit as st
import os
try:
    os.mkdir("temp")
except:
    pass
  

st.write("hello")

tts1=gTTS(text='hello world')
tts1.save(f"audio.mp3")

audio_file = open(f"audio.mp3", "rb")
audio_bytes = audio_file.read()
st.markdown(f"## Your audio:")
st.audio(audio_bytes, format="audio/mp3", start_time=0)

st.download_button(label="Download audio file", data=audio_bytes.read(), file_name='youraudio.mp3',mime='audio/mp3')
