import streamlit as st
st.write("Welcome to my app")
import streamlit as st
st.write("<h1>Hello world</h1>",unsafe_allow_html=True)
#ing colour of test
st.write("<h1ss style='color:red;'>hello world</h1>",unsafe_allow_html=True)
st.file_uploader("upload file")
import streamlit as st

st.write("<h1>Hello snehitha</h1>",unsafe_allow_html=True)

#apply style
st.write("<h1 style='color:blue;'>Hello snehitha</h1>",unsafe_allow_html=True)

#upload file
st.file_uploader("upload file")

#upload image
st.image("https://img.freepik.com/free-photo/beautiful-rose-nature_23-2150737339.jpg")

#upload video
st.video("https://www.youtube.com/watch?v=DBlMnnuVBO4")

#taking an image as input and displaying it
img=st.file_uploader("upload image")
st.image(img)










