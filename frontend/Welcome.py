import streamlit as st


def app():
    st.title("Welcome to this streamlit example")
    st.write("Click the button below to submit your long request")
    if st.button("Submit"):
        st.write("Redirecting to the submit page")
        st.switch_page("pages/1_Submit.py")


app()
