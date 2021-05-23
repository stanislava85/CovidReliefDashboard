import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import requests
import json
from matplotlib import style

st.set_page_config(layout="wide")

def by_boro():
	totals_boro = pd.read_csv("https://raw.githubusercontent.com/nychealth/coronavirus-data/master/totals/by-boro.csv")
	return totals_boro

def population():
	r = requests.get("https://data.cityofnewyork.us/resource/xywu-7bv9.json?")
	population =pd.DataFrame(json.loads(r.text))
	data = population[["borough", "_2020"]].copy()
	data.loc[data['borough']=='NYC Total', 'borough']= 'Citywide'
	data['borough'] = data['borough'].str.strip()
	data.loc[data['borough'] == "Staten Island", 'borough'] = "StatenIsland"
	data["_2020"] = data["_2020"].astype(int)
	data[["borough","_2020"]]
	return data

def join():
	totals_boro = pd.read_csv("https://raw.githubusercontent.com/nychealth/coronavirus-data/master/totals/by-boro.csv")
	r = requests.get("https://data.cityofnewyork.us/resource/xywu-7bv9.json?")
	population =pd.DataFrame(json.loads(r.text))
	data = population[["borough", "_2020"]].copy()
	data.loc[data['borough']=='NYC Total', 'borough']= 'Citywide'
	data['borough'] = data['borough'].str.strip()
	data.loc[data['borough'] == "Staten Island", 'borough'] = "StatenIsland"
	data["_2020"] = data["_2020"].astype(int)
	data[["borough","_2020"]]
	totals_boro = totals_boro.set_index('BOROUGH_GROUP').join(data.set_index('borough'))
	totals_boro.drop(columns = ["CASE_RATE","HOSPITALIZED_RATE", "DEATH_RATE"], axis=1, inplace=True)
	totals_boro = totals_boro.rename(columns={"_2020": "POPULATION"})
	return totals_boro

def graph():
	totals_boro = pd.read_csv("https://raw.githubusercontent.com/nychealth/coronavirus-data/master/totals/by-boro.csv")
	r = requests.get("https://data.cityofnewyork.us/resource/xywu-7bv9.json?")
	population =pd.DataFrame(json.loads(r.text))
	data = population[["borough", "_2020"]].copy()
	data.loc[data['borough']=='NYC Total', 'borough']= 'Citywide'
	data['borough'] = data['borough'].str.strip()
	data.loc[data['borough'] == "Staten Island", 'borough'] = "StatenIsland"
	data["_2020"] = data["_2020"].astype(int)
	data[["borough","_2020"]]
	totals_boro = totals_boro.set_index('BOROUGH_GROUP').join(data.set_index('borough'))
	totals_boro.drop(columns = ["CASE_RATE","HOSPITALIZED_RATE", "DEATH_RATE"], axis=1, inplace=True)
	totals_boro = totals_boro.rename(columns={"_2020": "POPULATION"})
	df_grouped = totals_boro.groupby("BOROUGH_GROUP").sum()
	user_filter = "CASE_COUNT"
	boroughs = "BOROUGH_GROUP"
	population = "POPULATION"
	ticks = ["Bronx", "Brooklyn", "Manhattan", "Queens", "StatenIsland","Citywide" ]

	plt.style.use('fivethirtyeight')
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

    # st.write(by_boro())
    # st.write(population())
    st.write(join())
    st.write('In this diagram we are representing the correleation between Total Population and\
    Number of Cases per borough. We see that in boroughs where the population is higher there are\
    more COVID-19 cases.')
    st.pyplot(graph())