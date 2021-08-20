import pandas as pd
import folium
from folium import plugins

#Importando base de dados e construindo modelo visual com DataFrame Pandas
df = pd.read_csv("olist_geolocation_dataset.csv")
df.head()
df.info()

#Lista de coordenadas
coordenadas = []

#Extrair regiões com o limite de 18000 dados de latitude e longitude e armazenar na var
for lat, lng in zip(df.geolocation_lat.values[:18000], df.geolocation_lng.values[:18000]):
    coordenadas.append([lat, lng])

#Rederizar mapa de visualização personalizado, na região do Brasil
mapa = folium.Map(location=[-15.788497, -47.879873], zoom_start=5, tiles='Stamen Toner')

#Adicionar registros armazenados no mapa, concentração dos registros
mapa.add_child(plugins.HeatMap(coordenadas))

#Verificar quais estados contem na base de dados
df.geolocation_state.unique()

#Estudar dados de registro por estado, soma total
df.geolocation_state.value_counts()

#Limitar base de dados aleatoriamente a 3% do valor para comparação
df2 = df.sample(frac = 0.03)

#Exibir dados de concentração por estado
df2.geolocation_state.value_counts()

#Lista de coordenadas para visão 3%
coordenadas_min = []

#Extrair regiões com o limite de 18000 dados de latitude e longitude e armazenar na var
for lat, lng in zip(df2.geolocation_lat.values[:18000], df2.geolocation_lng.values[:18000]):
    coordenadas_min.append([lat, lng])

#Rederizar mapa de visualização personalizado, na região do Brasil
mapa_min = folium.Map(location=[-15.788497, -47.879873], zoom_start=5, tiles='Stamen Toner')

#Adicionar registros armazenados no mapa, concentração dos registros
mapa_min.add_child(plugins.HeatMap(coordenadas_min))

#Rederizar resultado em arquivo HTML
mapa_min.save("mapa-consumidor.html")
