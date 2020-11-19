"""IMPORTS"""
# Import Librerias Externas
import os
from pathlib import Path
import pandas as pd

# Import libreria interna
from bienes_inmuebles.dataset.csv_exploracion import CSVExploracion
from bienes_inmuebles.dataset.csv_preprocesamiento import CSVPreprocesamiento
# from .. import csv_exploracion -> significa hacia atras o bajar un nivel (para buscar en carpetas por debajo)

"""CONSTANTES (en mayuscula)"""
path = Path(__file__)  # PATH A LA FILE EN CUALQUIER ORDENADOR
path2 = Path(path.parent)  # Un directorio hacia atras
path3 = Path(path2.parent)
PATH4 = str(Path(path3.parent))

"""CLASE y FUNCIONES"""
# class Moto o Coche (Vehiculo)
# class caracteristicas especificas (caracteristicas generales)
# class HIJO (PADRE)
# -------------------Dependencias------------------------
# CSV_PLOT -> CSV_Explolaracion --> CSV
# CSV_Preprocesamiento --> CSV
#
# CSV_ML --> CSV
# CSV --> main

# -------------------2 formas de Herenciar---------------
# from bienes_inmuebles.dataset.csv_exploracion import CSVExploracion
# class CSV (csv_exploracion.CSVExploracion, csv_prepocesamiento.CSVPreprocesamiento)

class CSV(CSVExploracion, CSVPreprocesamiento):
    def __init__(self, csv):
        self.csv = csv
        self.df = pd.read_csv(self.csv)

def _inplace(objeto, atributo, valor_atributo, inplace=False):  # funcion para sobrescribir ojbetos o realizar copias
    if inplace:
        setattr(atributo, valor_atributo)
    else:
        nuevo_objeto = CSV(objeto.csv)
        setattr(nuevo_objeto, atributo, valor_atributo)
        # self.atributo = valor_atributo
        # self.df = resultado_df
        return nuevo_objeto

"""EJECUCION"""
# Path Absoluto: solo funciona en mi PC
# Path Relativo: solo funciona si estan en el mismo Working Directory

# Permite ejecutar el fichero una vez posicionado directamente en él, pero NO cuando se importa
if __name__ == "__main__":
    # Programar como fichero unico -> linkar/empalmar con otros ficheros, clases ofunciones -> Asegurar Modularidad
    csv = CSV(os.path.join(PATH4, "data/csv_barcelona.csv"))
    csv.vistazo(show=True)
    csv.plot()
    csv_2 = csv.dropna()
    print(csv_2)
