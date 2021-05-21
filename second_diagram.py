import streamlit as st

def app():
    st.title('Second Diagram')

    if st.button('Say hello'):
        st.write('Why hello there')
    else:
        st.write('Goodbye')

