#! python3
from googletrans import Translator
import streamlit as st

#this library handles the query with the API so we do not need the following steps:
#[NotNeeded] Step1: Get the APIkey. NB: Some APIs dont require APIkey. 
#[NotNeeded] Step2: check API documentation to see what structure of URL is needed to access the data?
#[NotNeeded] Step3: Download the JSON data from the API.
#[NotNeeded] Step4: Load JSON data into a Python variable and use it in your program.
translator = Translator()
word= st.text_input('Gimme a word to translate: ','word' )
#destlang=input('Tell me a two letter code for the destination language like es or en: ')
abc = translator.translate(word, dest='it') 
st.write('the translation is', abc.text)
