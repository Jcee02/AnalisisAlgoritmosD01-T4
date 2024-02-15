import pandas as pd

gd = pd.read_csv("data/dataset.csv")


# Función para reemplazar caracteres en la cadena
def reemplazar_caracteres(string, posicion, alteracion):
    return string[:posicion - 1] + alteracion + string[posicion:]


# Lista de las combinaciones modificadas
combinaciones_modificadas = []

# recorrer las filas del .csv
for index, row in gd.iterrows():
    referencia = str(row['referencia'])
    alteracion = str(row['alteracion'])
    string_a_modificar = str(row["string_a_modificar"])

    # recorrer cada ventana de 10 caracteres
    for i in range(0, len(string_a_modificar) - 9, 5):
        ventana = string_a_modificar[i:i + 10]

        # Reemplazar caracter en la posicion especificada
        ventana_modificada = reemplazar_caracteres(ventana, int(row['posicion']), alteracion)
        combinaciones_modificadas.append(ventana_modificada)

df = pd.DataFrame(combinaciones_modificadas)

df.to_csv("result.csv")
