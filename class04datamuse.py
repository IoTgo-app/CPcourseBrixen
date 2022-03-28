#Remember to update the on code on github, and and create a NEW streamlit app for that code.

import streamlit as st

 #! python3
import json,requests
from pprint import pprint

## Access a word-finding query engine
## See API at http://www.datamuse.com/api/

#this library handles the query with the API so we do not need the following steps:
#Step1: Check the API documentation to see if the APIkey is needed. 
#No APIkey needed.


#Step2: Check API documentation to see what structure of URL is needed to access the data?
#For finding rhyming words for the keyword 'funny', the URL looks like this:
#'https://api.datamuse.com/words?rel_rhy=funny'
# make the above URL more generic, so that it is easy to replace the keyword
keyword=st.text_input('plz give me a keyword : ','peace')

option = st.selectbox(
     'Select a constraint',
     ('Synonyms', 'Antonyms', 'Sound like'))

st.write('You selected:', option)


if option == 'Synonyms':
  url='https://api.datamuse.com/words?rel_syn=' + keyword + '&max=4'
elif option =='Antonyms':
  url='https://api.datamuse.com/words?rel_ant=' + keyword + '&max=4'
else: 
  url= 'https://api.datamuse.com/words?sl=' + keyword + '&max=4'


#Step3: Download the JSON data from the API.
response = requests.get(url)   
#Uncomment to see the raw JSON text:
#print(response.text)  


#Step4: Load JSON data into a Python variable and use it in your program.
dataFromDatamuse = json.loads(response.text)  
#pprint(dataFromDatamuse1)
#pprint(dataFromDatamuse2)


for eachentry in dataFromDatamuse:
  st.write("-",eachentry['word']) 
  
  
#Uncomment to see the raw JSON text loaded in a Python Variable:
#print(dataFromDatamuse) 
#Uncomment to see a better readable version:£pprint(dataFromDatamuse) #dont forget to import the correct pprint library to make this work
#pprint(dataFromDatamuse[0]['word'])#if you just want to see the first 9 results
