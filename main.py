import folium
import pandas as pd
from pyodide.http import open_url
import matplotlib.pyplot as plt

# Define o URL base da API
url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.csv'

# Define os parâmetros da consulta
df = pd.read_csv(open_url(url))

m = folium.Map(location=[-15.77,-47.94],zoom_start=1,tiles='Stamen Terrain')
grupo_terremotos = folium.map.FeatureGroup()
for lat, lon,magi in zip(df['latitude'],df['longitude'],df['mag']):
        grupo_terremotos.add_child(
        folium.CircleMarker([lat,lon],radius=magi,fill_color='red', fill_opacity=0.5, color='red')
        )
m.add_child(grupo_terremotos)
display(m,target="mapa")
len(df)
plt.plot(1,1)
plt.show()
display(plt,target="block1")