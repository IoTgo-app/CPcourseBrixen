import streamlit as st
st.header("hello world")
title = st.text_input('Gimme a movie title', '<enter a movie title here in English>')
st.write('The current movie title is', title)
