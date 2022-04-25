#! python3
from googletrans import Translator
from gtts import gTTS 
import streamlit as st
st.write("hello")

tts1=gTTS(text='hello world')
tts1.save(f"temp/audio.mp3")

audio_file = open(f"temp/audio.mp3", "rb")
audio_bytes = audio_file.read()
st.markdown(f"## Your audio:")
st.audio(audio_bytes, format="audio/mp3", start_time=0)
