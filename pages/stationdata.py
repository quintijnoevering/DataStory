########### Python 3.2 #############
import urllib.request, json
import pandas as pd
import plotly.express as px
import streamlit as st

try:
    url = "https://gateway.apiportal.ns.nl/reisinformatie-api/api/v2/arrivals?station=ES"

    hdr ={
    # Request headers
    'Cache-Control': 'no-cache',
    'Ocp-Apim-Subscription-Key': 'dd03bbb7ab8847c4888c708280186197',
    }

    req = urllib.request.Request(url, headers=hdr)

    req.get_method = lambda: 'GET'
    response = urllib.request.urlopen(req)
    print(response.getcode())
    print(response.read())
    st.title(response.read())
except Exception as e:
    print(e)
    st.title(e)
####################################