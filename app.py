import home
import about
import first_diagram
import second_diagram
import third_diagram
import dashboard
import streamlit as st

PAGES = {
    "Home": home,
    "About": about,
    "Dashboard": dashboard,
    "First Diagram": first_diagram,
    "Second Diagram": second_diagram,
    "Third Diagram": third_diagram,

}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()