import pandas as pd

data = pd.read_csv('movies_dataset_corregido_transformado.csv')


#Filtrar peliculas por idioma original
peliculas_espanol = data[data['original_language'] == 'es'].head(20)

print(peliculas_espanol)