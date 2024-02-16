import pandas as pd

#TO:DO Equipar con los métodos necesarios a la clase para que una sola instancia de ella pueda ser usada para correr todo el programa.
# - Método para crear todas las variantes de los 8 cambios iniciales, resultado final 8!
# - Método para crear las variantes de un par de chunks dados (la validación del primero > segundo la hace el Front)
# - Método para crear las variantes de un rango de chunks dados (la validación de que el rango sea válido la hace el front)


class Programa:

    chunks = []
    
    def __init__(self, csv_file):
        #inicializar DataFrame para cada instania de Cadena
        self.df = pd.read_csv(csv_file)
        #Eliminar los fakin valores NaN de la columna string_a_modificar
        self.df.dropna(subset=['string_a_modificar'], inplace=True)
        #Lista de diccionarios con cada fila del dataframe
        self.dic_df = df.to_dic(orient='records')
        
        

    def 
    
    def dividir_cadena(self):        

        # Iterar sobre las filas restantes para dividir las cadenas
        for _, row in self.df.iterrows():
            string_a_dividir = str(row["string_a_modificar"])

            for i in range(0, len(string_a_dividir) - 9, 5):
                chunk = string_a_dividir[i:i + 10]
                self.chunks.append(chunk)

            # Verificar si hay un chunk restante al final
            if len(string_a_dividir) % 5 != 0:
                chunk = string_a_dividir[-(len(string_a_dividir) % 5):]
                self.chunks.append(chunk)

    def guardar_resultados(self, output_file):
        df_resultado = pd.DataFrame(self.chunks, columns=['chunk'])
        df_resultado.to_csv(output_file, index=False)

# Instancia de prueba???????????????????????????????
divisor = Programa("data/dataset.csv")
divisor.dividir_cadena()
divisor.guardar_resultados("result.csv")
