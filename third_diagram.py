import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import requests
import json
from matplotlib import style
from first_diagram import population_density_fatality

#Filter Variables
user_filter = "CASE_COUNT"
boroughs = "BOROUGH_GROUP"
population = "POPULATION"
ticks = ["Bronx", "Brooklyn", "Manhattan", "Queens", "StatenIsland","Citywide" ]

def by_boro():
	totals_boro = pd.read_csv("https://raw.githubusercontent.com/nychealth/coronavirus-data/master/totals/by-boro.csv")
	return totals_boro

def join():
	totals_boro = by_boro()
	data = population_density_fatality()
	totals_boro = totals_boro.set_index('BOROUGH_GROUP').join(data.set_index('borough'))
	totals_boro.drop(columns = ["CASE_RATE","HOSPITALIZED_RATE", "DEATH_RATE"], axis=1, inplace=True)
	totals_boro = totals_boro.rename(columns={"_2020": "POPULATION"})

	return totals_boro



def graph():
	totals_boro = join()
	df_grouped = totals_boro.groupby("BOROUGH_GROUP").sum()
	fig,ax=plt.subplots(figsize=(20,10))
	color = ("red", "purple")
	ax.barh(ticks, totals_boro[population],color="#f3e151")
	ax.barh(ticks, totals_boro[user_filter], left= totals_boro[population], color="#6c3376")
	ax.set_title(f'Number of Cases vs Total Population per Borough',size=35)
    #ax.set_xlabel('Total Population + Number of cases',size=25)
    #ax.legend(loc='lower right',prop={"size":20})
	return fig

def app():
    st.title('Third Diagram')

    st.write(join())
    st.write('In this diagram we are representing the correleation between Total Population and\
    Number of Cases per borough. We see that in boroughs where the population is higher there are\
    more COVID-19 cases.')

    st.pyplot(graph())