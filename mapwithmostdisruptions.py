"""
    @Author: Quintijn Oevering
    @Date: 29-9-2024
    @Links: https://canvas.hu.nl/courses/45341/assignments/311823
"""
import pandas as pd
import matplotlib.pyplot as plt

gebiedsindelingen_path = r'F:\Python School\BDD\Opdracht 3\data\ProRail_Gebiedsindelingen.csv'
basiskaart_path = r'F:\Python School\BDD\Opdracht 3\data\ProRail_Basiskaart.csv'
vertragingen_path = r'F:\Python School\BDD\Opdracht 3\data\disruptions-2023.csv'

# Laad de datasets
df_gebiedsindelingen = pd.read_csv(gebiedsindelingen_path)
df_basiskaart = pd.read_csv(basiskaart_path)
df_vertragingen = pd.read_csv(vertragingen_path)

# Bereken de top 10 trajecten met de meeste vertragingen
top_vertragingen = df_vertragingen['rdt_lines'].value_counts().head(10)

# Vergroot de figuur om meer ruimte te geven
plt.figure(figsize=(100, 100))

# Plot de basiskaart met X en Y als coördinaten
plt.scatter(df_basiskaart['X'], df_basiskaart['Y'], c='blue', alpha=0.5, label='Locaties')

# Voeg unieke labels toe op basis van GEOCODE_NAAM
unique_geocodes = df_basiskaart['GEOCODE_NAAM'].unique()

for geocode in unique_geocodes:
    subset = df_basiskaart[df_basiskaart['GEOCODE_NAAM'] == geocode]
    x_midden = subset['X'].mean()
    y_midden = subset['Y'].mean()
    plt.text(x_midden, y_midden, geocode, fontsize=8, ha='center', alpha=0.7)

# Lijsten voor de legende
legend_labels = []

# Kleurverloop van fel rood naar geel
colors = plt.get_cmap('autumn', 10)  # Gebruik de 'autumn' colormap voor een verloop van rood naar geel

# Plot de top 10 trajecten met vertragingen met kleurverloop
for idx, line in enumerate(top_vertragingen.index):
    # Zoek naar overeenkomsten in de basiskaart
    subset = df_basiskaart[df_basiskaart['GEOCODE_NAAM'].str.contains(line.split(' ')[0], na=False, regex=False)]
    if not subset.empty:  # Controleer of er een subset is
        color = colors(idx)  # Kleur op basis van de index
        plt.scatter(subset['X'], subset['Y'], color=color, s=200, alpha=0.8)
        # Voeg de trajectnaam toe zonder reden
        x_midden = subset['X'].mean()
        y_midden = subset['Y'].mean()
        plt.text(x_midden, y_midden, line, fontsize=10, ha='center', color='black', weight='bold')
        
        # Voeg labels toe aan de legende
        legend_labels.append(line)

# Voeg de legende toe met alleen de trajectnamen
plt.legend(legend_labels, title="Trajecten met Vertragingen", loc='upper left', bbox_to_anchor=(1.05, 1))

# Plot labels en titels
plt.title("ProRail Gebiedsindelingen met Locaties en Trajecten met Vertragingen", fontsize=16)
plt.xlabel("X-coördinaat", fontsize=12)
plt.ylabel("Y-coördinaat", fontsize=12)

# Zet de marges handmatig als tight_layout niet werkt
plt.subplots_adjust(left=0.1, right=0.85, top=0.9, bottom=0.1)

# Toon de plot
plt.show()