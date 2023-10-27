import streamlit as st
from send_email import sendEmail
import pandas

df = pandas.read_csv("topics.csv")

st.header("Contact Us ")

with st.form(key= "email_forms"):
    user_email = st.text_input("Enter your email address")
    topic = st.selectbox('What topics do you want to discuss?', df["topic"])
    raw_message = st.text_area("Enter your message")
    button = st.form_submit_button("Submit")
message = f"""\
Subject: New email from {user_email}
From:{user_email}
Topic: {topic}
{raw_message} 
"""
if button:
    sendEmail(message)
    st.info("Your email was sent successfully")

