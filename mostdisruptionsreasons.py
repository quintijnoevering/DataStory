"""
    @Author: Quintijn Oevering
    @Date: 29-9-2024
    @Links: https://canvas.hu.nl/courses/45341/assignments/311823
"""
import pandas as pd
import matplotlib.pyplot as plt

# CSV inlezen
disruptions = pd.read_csv(r"F:\Python School\BDD\Opdracht 3\data\disruptions-2023.csv")

# Groeperen op oorzaak en het totale aantal verstoringen berekenen
disruption_count = disruptions["cause_nl"].value_counts()

# Selecteer de oorzaken met de meeste verstoringen, bijvoorbeeld de top 10
top_causes = disruption_count.head(10)

# Filter de dataset voor alleen deze top 10 oorzaken
top_disruptions = disruptions[disruptions["cause_nl"].isin(top_causes.index)]

# Gemiddelde verstoringstijd per oorzaak voor de top oorzaken berekenen
average_disruptions = top_disruptions.groupby("cause_nl")["duration_minutes"].mean()

# Namen en waarden opslaan
names = top_causes.index
values = average_disruptions[names].values

# Barchart
plt.figure(figsize=(15, 6))  

plt.bar(names, values, color='skyblue')
plt.xlabel('Cause of Disruption')
plt.ylabel('Average Disruption Duration (minutes)')
plt.title('Average Disruption Duration of Top 10 Most Frequent Causes in 2023')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()