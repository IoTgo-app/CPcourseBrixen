import streamlit as st

# ! python3
import json, requests 

# add your own APIkey
#APIkey = 'this should not be public'

#location = 'london'
st.header('Weather Forecast Service')
#location = st.text_input('Gimme a city name:', 'Rome')
location = st.radio('Gimme a city name:',
     ('Bozen', 'Merano', 'Brixen'))

# check API documentation to see what structure of URL is needed to access the data
# http://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + APIkey + '&units=metric'
# print(url)


# Download the JSON data from OpenWeatherMap.org's API.
response = requests.get(url)  
# Uncomment to see the raw JSON text:
# print(response.text)  


# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
# Uncomment to see the raw JSON text:
# print(weatherData) 
# from pprint import pprint 
# pprint(weatherData) 

#st.write(weatherData)

st.write('The max temp today in', location, 'is', (weatherData['main']['temp_max']), 'C')
st.write('The min temp today in', location, 'is', (weatherData['main']['temp_min']), 'C')
