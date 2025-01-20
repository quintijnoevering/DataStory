import pandas as pd
import plotly.express as px
import streamlit as st

# Bestanden laden
gebiedsindelingen_path = r'E:\Python School\BDD\story\data\ProRail_Gebiedsindelingen.csv'
basiskaart_path = r'E:\Python School\BDD\story\data\ProRail_Basiskaart.csv'
vertragingen_path = r'E:\Python School\BDD\story\data\disruptions-2023.csv'

# Laad de datasets
df_basiskaart = pd.read_csv(basiskaart_path)
df_vertragingen = pd.read_csv(vertragingen_path)

# Bereken de top 10 trajecten met de meeste vertragingen
top_vertragingen = df_vertragingen['rdt_lines'].value_counts().head(10)

# Kleurverloop van fel rood naar lichtrood
colors = px.colors.sequential.Reds

# Maak een lijst om de gegevens voor Plotly te verzamelen
plot_data = []

# Maak een mapping voor kleuren en het aantal vertragingen op basis van index
color_map = {line: colors[int((len(top_vertragingen) - 1 - idx) * (len(colors) - 1) / (len(top_vertragingen) - 1))] 
              for idx, line in enumerate(top_vertragingen.index)}
delay_count_map = top_vertragingen.to_dict()  # Map traject -> aantal vertragingen

for line in top_vertragingen.index:
    # Zoek naar overeenkomsten in de basiskaart
    subset = df_basiskaart[df_basiskaart['GEOCODE_NAAM'].str.contains(line.split(' ')[0], na=False, regex=False)]
    if not subset.empty:  # Controleer of er een subset is
        color = color_map[line]  # Kleur op basis van de mapping
        delay_count = delay_count_map[line]  # Aantal vertragingen
        for _, row in subset.iterrows():
            plot_data.append(dict(
                X=row['X'],
                Y=row['Y'],
                GEOCODE_NAAM=row['GEOCODE_NAAM'],
                Traject=line,
                Color=color,
                Vertragingen=delay_count  # Voeg aantal vertragingen toe
            ))

# Zet de gegevens om in een DataFrame voor Plotly
df_plot = pd.DataFrame(plot_data)

# Hoofdpagina
st.title("ProRail Gebiedsindelingen met Interactieve Map")

# Maak de interactieve scatter plot met Plotly
fig = px.scatter_mapbox(df_plot, 
                        lat='Y', 
                        lon='X', 
                        color='Traject',  # Gebruik Traject als kleur
                        color_discrete_map=color_map,  # Kleur mapping
                        hover_name='Traject', 
                        hover_data={
                            'GEOCODE_NAAM': False, 
                            'Color': True,  # Verberg de kleurwaarde
                            'Vertragingen': True  # Toon aantal vertragingen
                        },
                        title='Trajecten met Vertragingen',
                        mapbox_style="carto-positron",
                        zoom=6, 
                        height=600)

# Toon de plot in Streamlit
st.plotly_chart(fig)

# Optioneel: Voeg een sectie toe voor extra informatie of filters
st.subheader("Top 10 Trajecten met Vertragingen")
st.write(top_vertragingen)