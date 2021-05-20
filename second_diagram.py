import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import style
from first_diagram import clean_data

#Setting dataset variable with cleaned data
group_data = clean_data()

#Creating Filter variables
boro_initials = "BK"
borough_filter = f'{boro_initials}_CASE_COUNT'
borough_fatality_filter = f'{boro_initials}_FATALITY_RATE'

#Declaring chart variables
labels = ["0-17", "18-24", "25-34", "35-44", "45-54", "55-64", "65-74", "75+"]
x = np.arange(len(labels))
width = 0.25

y1 = group_data.iloc[:,2:12:2]
y2 = group_data.iloc[:, 12:]
data1 = group_data.groupby('subgroup')[borough_filter].sum()
data2 = group_data.groupby('subgroup')[borough_fatality_filter].sum()

def bar_1():

    plt.style.use('fivethirtyeight')
    fig, ax1= plt.subplots(figsize=(30,15))
    ax2 = ax1.twinx()

    ax1.bar(x-width/2, data1, width=width*2,label='Number of Cases', color='#0077B6')
    ax2.bar(x+width/2, data2,width=width*2,label='Fatality Rate',color= '#C5DCA0')

    ax1.set_xticks(x)
    ax1.set_xticklabels(labels)
    ax1.set_xlabel('Age')
    ax1.set_ylabel('Number of cases')
    ax2.set_ylabel('Fatality Rate')
    ax1.set_title('Infection (Number of cases) and Fatality Rate(deaths/number of cases) Per Age Group', size=35)
    # plt.legend(loc='upper right', prop={"size":20})
    ax1.legend(loc='upper left', prop={"size":20})
    ax2.legend(loc='upper right',prop={"size":20})
    return fig


def bar_2():
    fig,ax=plt.subplots(figsize=(30,15))

    ax.bar(x-width/2, data1, width=width*2,label='Number of Cases', color='red')

    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_title(f'Number of cases per age group in {borough_filter[:2]}',size=35)
    ax.set_xlabel('Age group',size=15)
    ax.set_ylabel('Number of cases', size=15)
    ax.legend(loc='upper left',prop={"size":20})
    return fig


def app():
    st.title('Second Diagram')
    
    st.write(clean_data())
    
    st.pyplot(bar_1())

    st.pyplot(bar_2())