import sys
import pandas as pd
from front import*
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog, QMessageBox
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QColor
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi


class MiApp(QtWidgets.QMainWindow):
    def __init__(self):
        #Creamos un objeto tipo GUI
        super(MiApp, self).__init__()
        loadUi('diseño.ui',self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #Botones principales para abrir/crear la tabla
        self.ui.boton_abrir.clicked.connect(self.abrir_archivo)
        self.ui.boton_mostrar.clicked.connect(self.crear_tabla)
        
    #OPCION 1. IMPORTAR TABLA DE CADENAS     
    #Obtenemos la direccion del archivo a seleccionar 
    def abrir_archivo(self):
        file, _ = QFileDialog.getOpenFileName(self, "Abrir Archivo", "", "CSV Files (*.csv);;Excel Files (*.xlsx);;All Files (*)")
        if file:
            self.direccion = file
    #Creamos el metodo para crear tabla en base al archivo CLV
    def crear_tabla(self):
        #Creamos las excepciones correspondientes en caso que se escoga el tipo de archivo incorrecto
        try:
            if self.direccion:
                if self.direccion.endswith('.csv'):
                    df = pd.read_csv(self.direccion)
                elif self.direccion.endswith('.xlsx'):
                    df = pd.read_excel(self.direccion)
                else:
                    QMessageBox.about(self, 'Informacion', 'Formato no soportado')
                    return
            else:
                QMessageBox.about(self, 'Informacion', 'No se ha seleccionado un archivo')
                return
            #Convertimos las columnas/filas en una LISTA de LISTAS
            columnas = list(df.columns)
            df_fila = df.to_numpy().tolist()
            x = len(columnas)
            y = len(df_fila)

        except ValueError: 
            QMessageBox.about (self, 'Informacion', 'Formato Incorrecto')
            return None

        except FileNotFoundError: 
            QMessageBox.about (self, 'Informacion', 'El archivo esta corrupto')
            return None

        self.ui.tableWidget.setRowCount(y)
        self.ui.tableWidget.setColumnCount(x)
        #Ciclo for para asignar elementos a cada posicion correspondiente de su columna/fila
        for j in range(x):
            encabezado = QtWidgets.QTableWidgetItem(columnas[j])
            self.ui.tableWidget.setHorizontalHeaderItem(j, encabezado)
            for i in range(y):
                dato = str(df_fila[i][j])
                if dato == 'nan':
                    dato = ''
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(dato))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mi_app = MiApp()
    mi_app.show()
    sys.exit(app.exec_())