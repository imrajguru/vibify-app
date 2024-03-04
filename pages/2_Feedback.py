import json

import requests  # pip install requests
import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie


st.sidebar.write('"One good thing about music, when it hits you, you feel no pain."')
st.sidebar.subheader("-Bob marley")


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Define a function to get star rating
def get_star_rating():
    star_rating = 0
    for i in range(1, 6):
        if st.button(f"{i}"):
            star_rating = i
            break
    return star_rating


# Collect user feedback
st.title("Feedback...🤙")
st.write("Thank you for taking the time to provide feedback. We appreciate your input!")

name = st.text_input("Your Name:")
email = st.text_input("Your Email (Optional):")

feedback = st.text_area("Your Feedback:")

st.write("Rate between 1 to 5:")
star_rating = get_star_rating()

# Display feedback and rating summary
st.subheader("Summary")
st.write(f"Name: {name}")
st.write(f"Email: {email if email else 'Not Provided'}")
st.write(f"Feedback: {feedback}")
st.write(f"Rating: {star_rating}/5")
btn = st.button("Submit")

if name and email and btn:
    lottie_hello = load_lottieurl("https://lottie.host/102f3d4b-4a8e-49ef-aa27-e1a72af18b0f/7Lzkcs71Mq.json")
    st_lottie(lottie_hello, key="hello", width=500, height=300)
    st.success("Thanks for your feedback!")