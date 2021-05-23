import streamlit as st

def app():
    st.title('Third Diagram')

    display = ("male", "female")

    options = list(range(len(display)))

    value = st.selectbox("gender", options, format_func=lambda x: display[x])

    st.write(value)