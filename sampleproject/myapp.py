import streamlit as st

from PIL import Image
wikiimage ='https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Wikipedia-logo-v2.svg/1024px-Wikipedia-logo-v2.svg.png' 
# wikiimage = Image.open('https://pngimg.com/uploads/wikipedia/wikipedia_PNG31.png')

st.image(wikiimage, width=100)

st.header("Audio-Wikipedia")
st.write("This app converts an wikipedia article to audio file so that you can can listen to it on the go.")
st.write("A project by BlahBlah Blah, for the course of Computer Programing, MS Applied Linguistics, at unibz, Brixen, Italy")
st.markdown("""---""")

st.write("How to use: Just paste the URL of the wikipedia article, select origin and target langauge and listen to the audio") 
st.markdown("""---""")

st.text_input("Please paste here the URL of the wikipedia page you want to convert to audio")
st.selectbox("Please select the origin langauge of the wikipedia page",( "English", "French", "Arabic", "Italian"))

st.selectbox("Please select the target langauge in which you want to hear the article",( "Italian", "Arabic", "English", "French"))

st.audio( "https://upload.wikimedia.org/wikipedia/commons/c/c4/Muriel-Nguyen-Xuan-Chopin-valse-opus64-1.ogg", format="audio/ogg")

st.markdown("""---""")

st.write("Credits:")
st.write("""
- For Wikipedia logo: https://en.wikipedia.org/wiki/Wikipedia_logo#/media/File:Wikipedia-logo-v2.svg, available under the Creative Commons Attribution-ShareAlike License 3.0; a
""")
st.write("""- For the sample audio file: Performer: Muriel Nguyen Xuan and Stéphane MagnenatComposer: Frédéric Chopin, License: Creative Commons Attribution-Share Alike 4.0 International, 3.0 Unported, 2.5 Generic, 2.0 Generic and 1.0 Generic license. https://creativecommons.org/licenses/by-sa/4.0/, URL: https://upload.wikimedia.org/wikipedia/commons/c/c4/Muriel-Nguyen-Xuan-Chopin-valse-opus64-1.ogg
""")
st.write("""- For the tutorial: https://docs.streamlit.io/library/api-reference/media/st.audio 
""")
