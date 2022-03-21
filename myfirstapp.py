import streamlit as st
st.header("hello world")
title = st.text_input('Gimme a movie title', '<enter a movie title here in EN', max_chars=7)
st.write('The current movie title is', title)
