import pandas as pd

class Cadena:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file)
        self.chunks = []

    def dividir_cadena(self):
        # Eliminar las filas con valores NaN en la columna "string_a_modificar"
        self.df.dropna(subset=['string_a_modificar'], inplace=True)

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

# Uso de la clase
divisor = Cadena("data/dataset.csv")
divisor.dividir_cadena()
divisor.guardar_resultados("result.csv")
