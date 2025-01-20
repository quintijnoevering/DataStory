import pandas as pd
import plotly.express as px
import streamlit as st

# CSV-bestanden paden
vertragingen_path_2011 = r'\disruptions-2011.csv'
vertragingen_path_2012 = r'\disruptions-2012.csv'
vertragingen_path_2013 = r'\disruptions-2013.csv'
vertragingen_path_2014 = r'\disruptions-2014.csv'
vertragingen_path_2015 = r'\disruptions-2015.csv'
vertragingen_path_2016 = r'\disruptions-2016.csv'
vertragingen_path_2017 = r'\disruptions-2017.csv'
vertragingen_path_2018 = r'\disruptions-2018.csv'
vertragingen_path_2019 = r'\disruptions-2019.csv'
vertragingen_path_2020 = r'\disruptions-2020.csv'
vertragingen_path_2021 = r'\disruptions-2021.csv'
vertragingen_path_2022 = r'\disruptions-2022.csv'
vertragingen_path_2023 = r'\disruptions-2023.csv'

all_vertragingen = [
    vertragingen_path_2011, vertragingen_path_2012, vertragingen_path_2013, 
    vertragingen_path_2014, vertragingen_path_2015, vertragingen_path_2016, 
    vertragingen_path_2017, vertragingen_path_2018, vertragingen_path_2019, 
    vertragingen_path_2020, vertragingen_path_2021, vertragingen_path_2022, 
    vertragingen_path_2023
]

# Functie om CSV-bestanden in te laden en te combineren
@st.cache_data
def load_data():
    all_data = []
    for file in all_vertragingen:
        df = pd.read_csv(f"E:\Python School\BDD\Story\data{file}")
        all_data.append(df)
    return pd.concat(all_data, ignore_index=True)

# Data laden
data = load_data()

# Datumkolom omzetten naar datetime
data['start_time'] = pd.to_datetime(data['start_time'])
data['year'] = data['start_time'].dt.year

# Bereken het aantal vertragingen per jaar
delays_per_year = data.groupby('year').size().reset_index(name='count')

# Streamlit interface
st.title("Overzicht van vertragingen in het OV (2011-2023)")

# Interactieve grafiek maken met Plotly
fig = px.line(delays_per_year, x='year', y='count', 
            labels={'year': 'Jaar', 'count': 'Aantal vertragingen'},
            title="Aantal vertragingen per jaar (2011-2023)")

# Weergave van de grafiek in Streamlit
st.plotly_chart(fig)
