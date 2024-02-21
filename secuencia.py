import itertools as it
import csv

class Secuencia:
  # Definimos los atributos de la clase
  cadena_original = None

  # Definimos booleano de paralelizacion
  cuda_cores = False

  # Listas para almacenar los datos de cada columna
  posicion = []
  referencia = []
  alteracion = []

  # Diccionario para almacenar los cambios a realizar en cada chunk
  cambios = {}

  # Diccionario para almacenar las combinaciones de chunks
  combinaciones = {}
  

  def __init__(self, file):
    self.file = file

    self.generar_cambios(file)
    self.generar_combinaciones()

    self.exportar_combinaciones()

  
  def generar_cambios(self, file):
    # Abrir el archivo CSV
    with open(file, newline='') as archivo_csv:
      lector_csv = csv.DictReader(archivo_csv)
      
      # Leer la primera fila del archivo CSV
      primera_fila = next(lector_csv)
      # Obtener el valor de string_a_modificar
      self.cadena_original = primera_fila['string_a_modificar']
      
      # Ahora puedes procesar las otras columnas
      # Crear listas vacías para almacenar los datos de cada columna
      self.posicion = [int(primera_fila['posicion'])]
      self.referencia = [primera_fila['referencia']]
      self.alteracion = [primera_fila['alteracion']]


      # Leer las filas restantes del archivo CSV
      for fila in lector_csv:
        # Almacenar los datos de cada columna en las listas correspondientes
        self.posicion.append(int(fila['posicion']))
        self.referencia.append(fila['referencia'])
        self.alteracion.append(fila['alteracion'])
      
    
    # Construimos la lista de cambios a realizar en base a los chunks
    # Iterar sobre los índices de la cadena_original utilizando un paso de 5
    for indice in range(0, len(self.cadena_original), 5):
      indx_cambios = []

      for x in range(indice, indice + 9):
        if x in self.posicion:
          indx_cambios.append(x)
          
      if indx_cambios and indx_cambios != cambios_prev:
        self.cambios[indice] = indx_cambios
      
      cambios_prev = indx_cambios
  
  def generar_combinaciones(self):
    pares_chunks = {}

    # Generamos las variaciones de los chunks individuales
    for chunk, cambios in self.cambios.items():
      if len(cambios) > 1: # Si el chunk tiene más de un cambio, generamos todas las combinaciones posibles
        variaciones = []
        for cambio in cambios:
          lista_cadena = list(self.cadena_original)
          lista_cadena[cambio] = self.alteracion[self.posicion.index(cambio)]

          variaciones.append(''.join(lista_cadena))
        self.combinaciones[chunk] = variaciones

      else: # Si el chunk tiene un solo cambio, generamos una sola combinacion
          lista_cadena = list(self.cadena_original)
          lista_cadena[cambios[0]] = self.alteracion[self.posicion.index(cambios[0])]

          self.combinaciones[chunk] = ''.join(lista_cadena)

    # Generar todas las combinaciones de pares de chunks
    for i in range(0, len(self.cambios.keys()), 2):
      pares = list(it.combinations(self.cambios.keys(), 2))

    # Generar los cambios a realizar en cada par de chunks
    for par in pares:
      pares_chunks[par] = list(sorted(set(self.cambios[par[0]] + self.cambios[par[1]])))
    
    # Generar las variaciones de cada par de chunks
    variaciones = []
    for par, cambios in pares_chunks.items():
      #print(f"Par: {par} - Combinación: {cambios}")

      

      lista_cadena = list(self.cadena_original)

      for i in cambios:
        lista_cadena[i] = self.alteracion[self.posicion.index(i)]
        variaciones.append(''.join(lista_cadena))

      self.combinaciones[par] = variaciones
  
  def exportar_combinaciones(self):
    # Exportamos las combinaciones a un csv
    with open('combinaciones.csv', mode='w', newline='') as archivo_csv:
      escritor_csv = csv.writer(archivo_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      escritor_csv.writerow(['chunk', 'combinacion'])

      for chunk, combinacion in self.combinaciones.items():
        escritor_csv.writerow([chunk, combinacion])
      
    

sec = Secuencia('dataset.csv')
