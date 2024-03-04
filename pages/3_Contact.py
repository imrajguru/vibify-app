import json

import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.sidebar.write('"Where words fail, music speaks."')
st.sidebar.subheader("-Heinrich Heine")
st.title("Contact Us...📫")

contact_form = """<form action="https://formsubmit.co/rajguruthevar@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)
# Use Local CSS File


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css(r"C:\Users\rajrs\PycharmProjects\facedetection\pages\style\style.css")


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_message = load_lottieurl("https://lottie.host/b96b5edb-16a3-4597-9baf-c8b6eb36d577/GtLCmQ5Rmo.json")
st_lottie(lottie_message, key="message", width=700, height=400)

