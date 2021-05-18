import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import json

st.set_page_config(layout="wide")

def clean_data():
    by_boro = pd.read_csv("https://raw.githubusercontent.com/nychealth/coronavirus-data/master/totals/group-data-by-boro.csv")
    by_boro.drop([12,13,14,15,16,17], inplace=True)
    by_boro = by_boro.fillna((by_boro[by_boro['group']=='Age'][:3].sum()))
    by_boro.drop([1,2,3],inplace=True)
    for col in by_boro.columns:
        if "RATE" in col or "HOSPITALIZED_COUNT" in col:
            by_boro = by_boro.drop(col, axis=1)
    by_boro.drop([0],inplace=True)
    by_boro["BK_FATALITY_RATE"] = by_boro["BK_DEATH_COUNT"]/by_boro["BK_CASE_COUNT"]
    by_boro["BX_FATALITY_RATE"] = by_boro["BX_DEATH_COUNT"]/by_boro["BX_CASE_COUNT"]
    by_boro["MN_FATALITY_RATE"] = by_boro["MN_DEATH_COUNT"]/by_boro["MN_CASE_COUNT"]
    by_boro["QN_FATALITY_RATE"] = by_boro["QN_DEATH_COUNT"]/by_boro["QN_CASE_COUNT"]
    by_boro["SI_FATALITY_RATE"] = by_boro["SI_DEATH_COUNT"]/by_boro["SI_CASE_COUNT"]
    by_boro.drop(columns = ['group'], axis=1, inplace=True)
    return by_boro

def population_density():
    r = requests.get("https://data.cityofnewyork.us/resource/xywu-7bv9.json?")
    population = pd.DataFrame(json.loads(r.text))
    total = population[["borough", "_2020"]]
    total = total.drop([0]).reset_index(drop=True)
    total["_2020"]=total._2020.astype(float)
    total["borough"]=total.borough.astype(str)
    total.loc[0, 'borough']  #there are white spaces at the front
    ##strip spaces
    total['borough'] = total['borough'].str.strip()
    #Land area in square miles per boro, taken from https://en.wikipedia.org/wiki/Boroughs_of_New_York_City
    d = {'Bronx': 42.10, 'Brooklyn':70.82, 'Manhattan':22.83, 'Queens':108.53, 'Staten Island':58.37}
    total['land'] = d.values()
    total["Density"] = total["_2020"]/total["land"]
    return total

def scatterplot_1():

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    age = 'subgroup'
    borough_filter = 'BK_CASE_COUNT'
    plt.style.use('fivethirtyeight')
    N = 8
    colors = np.random.rand(N)

    plt.scatter(clean_data()[age], clean_data()[borough_filter], c=colors, alpha=0.5)

    return fig

def scatterplot_2():

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    age = 'subgroup'
    borough_filter = 'BK_CASE_COUNT'
    plt.style.use('fivethirtyeight')
    N = 8
    colors = np.random.rand(N)

    columns = list(clean_data().columns)

    for col in columns[1:]:
        plt.scatter(clean_data()[age], clean_data()[col], c=colors, alpha=0.5, label=col)

    return fig

def app():
    st.title('First Diagram')
    
    st.write(clean_data())

    st.write(population_density())
    
    st.pyplot(scatterplot_1())

    st.pyplot(scatterplot_2())