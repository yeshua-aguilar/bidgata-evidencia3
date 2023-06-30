import pandas as pd

data = pd.read_csv('movies_dataset_corregido_transformado.csv')

#Encontrar las peliculas mas populares
peliculas_populares = data.sort_values('popularity', ascending=False).head(10)

print(peliculas_populares)