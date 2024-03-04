import json

import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.title("About us...🔎")

st.sidebar.write('"Without music life would be a mistake"')
st.sidebar.subheader("-Friedrich Nietzsche")
st.header("This project is developed by the Members of E2 batch:-")
st.markdown("**🙍‍♂️ Rajguru (Backend/ML integration)**")
st.write("**🙍‍♂️ Mohan (Frontend/backend)**")
st.write("**🙍‍♀️ Nida (layout design)**")
st.write("**🙍‍♀️ Nanthini (Research analysis)**")


st.subheader("About this project:-")
st.write("The purpose of the project is to develop a Music Recommendation System with Emotion Analysis to enhance the "
         "way people discover and enjoy music. By incorporating algorithms that understand users' emotions, "
         "the system aims to provide personalized recommendations, ensuring a more meaningful and tailored music "
         "experience. The project addresses gaps in existing systems, including limited emotion-tagged datasets and "
         "the need for real-time emotion detection, with the goal of creating a user-friendly and culturally "
         "sensitive platform for music enthusiasts.")


st.subheader("THANK YOU!!!")


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_message = load_lottieurl("https://lottie.host/cf8e11b2-ef1f-41e0-83f3-3d3c5cbec427/1wGL4kwEjI.json")
st_lottie(lottie_message, key="message", width=700, height=400)

