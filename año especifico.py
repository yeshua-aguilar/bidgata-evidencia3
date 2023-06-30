import pandas as pd

data = pd.read_csv('movies_dataset_corregido_transformado.csv')

#Encontrar las peliculas que se lanzaron en un año especifico
peliculas_1998 = data[data['release_year'] == 1998].head(12)

print(peliculas_1998)