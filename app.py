import home
import about
import hypothesis_one
import hypothesis_two
import borough_cases
# import folium_map
import overview
import streamlit as st

PAGES = {
    "Home": home,
    # "NYC Covid Map": folium_map,
    "Totals Overview": overview,
    "Borough Cases": borough_cases,
    "Hypothesis One": hypothesis_one,
    "Hypothesis Two": hypothesis_two,

    "About": about,
}

# st.set_page_config(layout="wide")

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()