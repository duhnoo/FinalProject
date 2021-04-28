'''
Date: 04/28/2021
Section: 3
File: D'AnnolfoFinalProject.py
Description:
This program uses StreamlitUI and other tools to create a dynamic web application that
illustrates a heat map and bar chart based on a CSV dataset. This is the final project.
I pledge that I have completed this programming assignment independently.
I have not copied from a student or any source.
I have not given my code to any student.
'''

# Import libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap
from streamlit_folium import folium_static

# Get Data Function with Default
def get_data(file="collisions.csv"):
    csv = pd.read_csv(file)
    return csv

def bar_chart():

    # Initialize and Make Bar Chart
    earlyCount, morningCount, afternoonCount, eveningCount, nightCount = 0, 0, 0, 0, 0
    data['TIME'] = pd.to_datetime(data['TIME'], format='%H:%M')
    for time in data['TIME']:
        if 0 <= time.hour <= 5:
            earlyCount += 1
        elif 6 <= time.hour <= 11:
            morningCount += 1
        elif 12 <= time.hour <= 16:
            afternoonCount += 1
        elif 17 <= time.hour <= 20:
            eveningCount += 1
        elif 21 <= time.hour <= 23:
            nightCount += 1

    x = ["Early Morning (12-5 AM)", "Morning Commute (6-11 AM)", "Afternoon (12-4 PM)",
             "Evening Rush Hour (5-8 PM)", "Night (9-11 PM)"]
    y = [earlyCount, morningCount, afternoonCount, eveningCount, nightCount]
    plt.bar(x, y, color='red', edgecolor='cyan')
    plt.title("Time Period of Car Collisions in All 5 Boroughs")
    plt.xticks(rotation=45, ha='right')
    plt.xlabel("Time Period")
    plt.ylabel("Frequency")

    return plt

# Get data
data = get_data()

# Titles and Sidebar
st.title("NYC Traffic Collisions from Dec. 2016 - Feb. 2017")
st.sidebar.subheader("Data Inputs")

# Toggles heatmap and histogram selections
show_heatmap = st.sidebar.checkbox("Show Heatmap")
show_barchart = st.sidebar.checkbox("Show Bar Chart")

# Filter Data
st.write(f'Data Points: {len(data):,}')

if show_heatmap:
    heatMap = folium.Map(location=[40.7128, -74.0060], zoom_start=10)

    # filter and remove NaNs
    dataFrame = data[["LATITUDE", "LONGITUDE"]]
    dataFrame = dataFrame.dropna(axis=0, subset=['LATITUDE', 'LONGITUDE'])

    # List Comprehension to store lats and longs in a list
    heatMapList = [[row["LATITUDE"], row["LONGITUDE"]] for index, row in dataFrame.iterrows()]

    # Plot it
    HeatMap(heatMapList).add_to(heatMap)

    # Subheader and Streamlit
    st.subheader("Where do the most accidents occur in NYC's 5 Boroughs?")
    folium_static(heatMap)

    # Heat Map Borough Filter
    st.sidebar.subheader("Heat Map Filters")
    st.sidebar.write("By Borough")
    boroughsList = data['BOROUGH'].drop_duplicates().dropna(axis='index', how='any').sort_values().to_list()
    borough_options = st.sidebar.radio('', boroughsList)
    st.markdown(f'**{borough_options}**')
    if borough_options == 'BRONX':
        newMap = folium.Map(location=[40.7128, -74.0060], zoom_start=10)
        newDF = data[['LATITUDE', 'LONGITUDE']].loc[data['BOROUGH'] == 'BRONX']
        newDF = newDF.dropna(axis=0, subset=['LATITUDE', 'LONGITUDE'])
        newList = [[row["LATITUDE"], row["LONGITUDE"]] for index, row in newDF.iterrows()]
        HeatMap(newList).add_to(newMap)
        folium_static(newMap)

    elif borough_options == 'BROOKLYN':
        newMap = folium.Map(location=[40.7128, -74.0060], zoom_start=10)
        newDF = data[['LATITUDE', 'LONGITUDE']].loc[data['BOROUGH'] == 'BROOKLYN']
        newDF = newDF.dropna(axis=0, subset=['LATITUDE', 'LONGITUDE'])
        newList = [[row["LATITUDE"], row["LONGITUDE"]] for index, row in newDF.iterrows()]
        HeatMap(newList).add_to(newMap)
        folium_static(newMap)

    elif borough_options == 'MANHATTAN':
        newMap = folium.Map(location=[40.7128, -74.0060], zoom_start=10)
        newDF = data[['LATITUDE', 'LONGITUDE']].loc[data['BOROUGH'] == 'MANHATTAN']
        newDF = newDF.dropna(axis=0, subset=['LATITUDE', 'LONGITUDE'])
        newList = [[row["LATITUDE"], row["LONGITUDE"]] for index, row in newDF.iterrows()]
        HeatMap(newList).add_to(newMap)
        folium_static(newMap)

    elif borough_options == 'QUEENS':
        newMap = folium.Map(location=[40.7128, -74.0060], zoom_start=10)
        newDF = data[['LATITUDE', 'LONGITUDE']].loc[data['BOROUGH'] == 'QUEENS']
        newDF = newDF.dropna(axis=0, subset=['LATITUDE', 'LONGITUDE'])
        newList = [[row["LATITUDE"], row["LONGITUDE"]] for index, row in newDF.iterrows()]
        HeatMap(newList).add_to(newMap)
        folium_static(newMap)

    elif borough_options == 'STATEN ISLAND':
        newMap = folium.Map(location=[40.7128, -74.0060], zoom_start=10)
        newDF = data[['LATITUDE', 'LONGITUDE']].loc[data['BOROUGH'] == 'STATEN ISLAND']
        newDF = newDF.dropna(axis=0, subset=['LATITUDE', 'LONGITUDE'])
        newList = [[row["LATITUDE"], row["LONGITUDE"]] for index, row in newDF.iterrows()]
        HeatMap(newList).add_to(newMap)
        folium_static(newMap)

# Add Space between Charts
st.text("\n\n\n\n\n")


# uses get_data function passing in csv
data = get_data("collisions.csv")

# If show bar chart button is toggled, run it
if show_barchart:
    
    # Show Filters and Title
    st.subheader("At what general time period (morning commute, late morning, afternoon, rush hour, evening) did the majority of these accidents occur?")

    # Call in function
    st.pyplot(bar_chart())

