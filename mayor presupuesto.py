import pandas as pd

data = pd.read_csv('movies_dataset_corregido_transformado.csv')

#Obtener la pelicula con el mayor presupuesto

pelicula_mayor_presupuesto = data[data['budget'] == data['budget'].max()]

print(pelicula_mayor_presupuesto)