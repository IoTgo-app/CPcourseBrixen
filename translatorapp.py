import numpy as np
import streamlit as st

st.title("Guess The Number")
st.markdown("## Welcome to the game of deciding number")
st.sidebar.title("Guess The Number")
st.sidebar.markdown("## Welcome to the game of deciding number")

st.sidebar.write("What is your name mate")
name = st.sidebar.text_input("Enter your name")


if  st.sidebar.checkbox("Show Instructions", False):
    st.write("Nice to meet you", name)
    st.write("Let's play a game, i will guess a number between 1 and 20 and you have guess it in less than 6 guesses")

number = np.random.randint(1,20)

g = 0

while True :
    if g
    if x> number:
        st.write("Wrong, Your guess is greater than the number")
    if x< number:
        st.write("Wrong, Your guess is lesser than the number")
    if x==number :
        st.success("Congratulations, you won")
        st.stop()
