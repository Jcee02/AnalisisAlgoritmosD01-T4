import testcsvreading as tcr
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

        #OPCION 1. Botones principales para abrir/crear la tabla de cadenas
        self.ui.boton_abrirOP1.clicked.connect(self.abrir_archivo)
        self.ui.boton_mostrarOP1.clicked.connect(self.crear_tabla)

        #OPCION 2. Botones principales para hacer combinaciones
        self.ui.boton_abrirOP2.clicked.connect(self.abrir_archivo)
        self.ui.boton_TodasCombinaciones.clicked.connect(self.combinar)
        self.ui.boton_abrirResultOP2.clicked.connect(self.abrir_archivo)
        self.ui.boton_mostrarOP2.clicked.connect(self.crear_tabla)
 
    #Creamos metodo para....
    def combinar(self):
        comb_cadena = tcr.DNAPermutations(self.direccion)

    #Obtenemos la direccion del archivo a seleccionar 
    def abrir_archivo(self):
        file, _ = QFileDialog.getOpenFileName(self, "Abrir Archivo", "", "CSV Files (*.csv);;Excel Files (*.xlsx);;All Files (*)")
        if file:
            self.direccion = file

    #Creamos el metodo para crear tabla en base al archivo CLV
    def crear_tabla(self):
        sender_button = self.sender()
        if sender_button == self.ui.boton_mostrarOP1:
            table_widget = self.ui.tableWidget
        elif sender_button == self.ui.boton_mostrarOP2:
            table_widget = self.ui.tableWidget_2
        else:
            return

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

        self.mostrar_tabla(df, table_widget)

    def mostrar_tabla(self, df, table_widget):
        try:
            # Convertimos las columnas/filas en una LISTA de LISTAS
            columnas = list(df.columns)
            df_fila = df.to_numpy().tolist()
            x = len(columnas)
            y = len(df_fila)

            table_widget.setRowCount(y)
            table_widget.setColumnCount(x)

            # Ciclo for para asignar elementos a cada posicion correspondiente de su columna/fila
            for j in range(x):
                encabezado = QtWidgets.QTableWidgetItem(columnas[j])
                table_widget.setHorizontalHeaderItem(j, encabezado)
                for i in range(y):
                    dato = str(df_fila[i][j])
                    if dato == 'nan':
                        dato = ''
                    table_widget.setItem(i, j, QTableWidgetItem(dato))
        except ValueError:
            QMessageBox.about(self, 'Informacion', 'Formato Incorrecto')
        except FileNotFoundError:
            QMessageBox.about(self, 'Informacion', 'El archivo esta corrupto')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mi_app = MiApp()
    mi_app.show()
    sys.exit(app.exec_())
