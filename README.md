# AnalisisAlgoritmosD01-T4
La intención de este texto es implementar los requisitos y pasos a seguir para la correcta implementación del programa:
Somos: 
Equipo 4
- Juan Carlos Torres
- Pablo De Robles
- Angela Delgado
  
Instrucciones:

1. Implementación del Algoritmo:
Aplicando los principios de fuerza bruta, y con el conjunto de datos proporcionado, modificar la cadena de caracteres que se indica reemplazando el caracter "referencia" por el de la columna de "alteracion". 
Usar la librería pandas para importar el archivo .csv.
Generar las distintas combinaciones del string con las alteraciones en una ventana de 10 caracteres, y recorrer esta ventana cada 5 espacios. Es decir: 
Tomar la primera ventana:
 TGTAGTGCAGTGGCGTGATCTTGGCTCACTG.....
|----------------------|
     ventana 1

reemplazar los caracteres indicados por "posicion" cubriendo todas las combinaciones posibles de ese segmento,

avanzar al siguiente segmento recorriéndose 5 posiciones,

 TGTAGTGCAGTGGCGTGATCTTGGCTCACTG.....
             |----------------------|
                  ventana 2

repetir el proceso de reemplazo de caracteres, y así suvesivamente hasta cubrir toda la secuencia.

2. Conjunto de Datos:
Usar el archivo .csv proporcionado

3. Resultado :

Todas las distintas combinaciones posibles de la cadena de caracteres proporcionada, llevadas a cabo con las especificaciones descritas en el apartado número 1.
