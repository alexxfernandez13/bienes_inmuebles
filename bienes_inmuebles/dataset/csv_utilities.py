"""IMPORTS"""
####IMPORT DE LIBRERIAS TERCERAS
import os
from pathlib import Path
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import pandas as pd
from numpy import *
import numpy as np
from numpy import set_printoptions
from pandas.plotting import scatter_matrix
from scipy import stats
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import Binarizer
#####imports de la libreria propia
from csv_exploracion import CSVExploracion
"""
.. significa hacia atras, o bajar un nivel, siempre que tengas que buscar carpetas que estan por debajo
"""
#from .. import csv_exploracion



"""CONSTANTES (se definen en mayuscula)"""
path = Path(__file__)  # PATH A LA FILE EN CUALQUIER ORDENADOR
path2 = Path(path.parent)  # La funcion path.parent va un directorio hacia atras
path3 = Path(path2.parent)
PATH4 = str(Path(path3.parent))

"""CLASES y FUNCIONES"""

"""
CSV --> df --> vistazo

CSV --> dropna() --> CSV2()--> df modificad


"""


class CSVPreprocesamiento():
    def __init__(self,csv):
        self.csv = csv
        self.df = pd.read_csv (self.csv)

    def _inplace(self, atributo, valor_atributo, inplace=False):
        if inplace:
            setattr(self, atributo, valor_atributo)
        else:
            nuevo_objeto = CSV(self.csv)
            setattr(nuevo_objeto, atributo, valor_atributo)
            # self.atributo = valor_atributo
            # self.df = resultado_df
            return nuevo_objeto

    def duplicados(self, inplace=False):
        df_resultado = self.df.drop_duplicates()
        return self._inplace("df", df_resultado, inplace)  # se le puede el csv antes de leerlo o el dataframe df

    def dropna(self, number=10000, axis=1,
               inplace=False):  # Elimina filas/registros axis=0 o columnas/atributos si axis=1. El limite de NaN lo marca number
        length = self.df.shape[axis - 1]  # -1 ¿porque era esto?
        df_resultado = self.df.dropna(thresh=length - number, axis=axis)
        return self._inplace("df", df_resultado, inplace)

    def ints(self, inplace=False):
        df_resultado = self.df.select_dtypes(include=["int64", "float64"])
        return self._inplace("df", df_resultado, inplace)

    def mvs(self, columns=None, strategy="mean", inplace=False):
        imp_mean = SimpleImputer(missing_values=np.nan, strategy=strategy)
        aux = imp_mean.fit_transform(self.df)
        try:
            df_resultado = pd.DataFrame(data=aux, columns=self.df.columns)
        except ValueError:
            raise ValueError(
                "Necesitas borrar columnas con NANs y columnas con Strings primero. Ejecutar self.dropna() y self.ints() antes de self.mvs()")
        return self._inplace("df", df_resultado, inplace)

    def outliers(self, grado=3, inplace=False):  # Eliminar filas con outlier y escoger grado de eliminacion)
        z_scores = stats.zscore(self.df)  # self.df.values ????
        where_are_NaNs = isnan(z_scores)
        z_scores[where_are_NaNs] = 0
        abs_z_scores = np.abs(z_scores)
        filtered_entries = (abs_z_scores < grado).all(
            axis=1)  # buscar solucion para sustituir nan por 0 en la lista de listas
        df_resultado = self.df[filtered_entries]
        return self._inplace("df", df_resultado, inplace)

    def reescalar(self, inplace=False):
        scaler = MinMaxScaler(feature_range=(0, 1))
        df_resultado = scaler.fit_transform(self.df)
        return self._inplace("df", df_resultado, inplace)

    def estandarizar(self, inplace=False):
        scaler = StandardScaler().fit(self.df)
        df_resultado = scaler.transform(self.df)
        return self._inplace("df", df_resultado, inplace)

    def normalizada(self, inplace=False):
        scaler = Normalizer().fit(self.df)
        df_resultado = scaler.transform(self.df)
        return self._inplace("df", df_resultado, inplace)

    def binarizar(self, inplace=False):
        binarizer = Binarizer(threshold=0.0).fit(self.df)
        df_resultado = binarizer.transform(self.df)
        return self._inplace("df", df_resultado, inplace)

"""
VEHICULO --> Moto o Coche

"""

#class Moto (VEHICULO)
#cosas especificas (cosas muy generales)
#HIJO(PADRE)

##--------------------------------------------

####CSVPLOT -> CSV_Explolaracion --> CSV
#####          CSV_Preprocesai   -->CSV

#-------------------------------------------

#####             Standarizar     -->    ML
#####

####--------------------------------------
"""
csv = CSV("datos.csv")
csv_dupl = csv.duplicados()
csv_na = csv_dupl.dropna()

ml = ML(csv_na.df)


"""
#from bienes_inmuebles.dataset.csv_exploracion import CSVExploracion
#class CSV (csv_exploracion.CSVExploracion,CSVPreprocesamiento) ---- (importas la file i llamas funcion de dentro)

class CSV(CSVExploracion, CSVPreprocesamiento):

    def __init__(self, csv):
        self.csv = csv
        self.df = pd.read_csv(self.csv)

"""EJECUCION"""
# PATH ABSOLUTO: SOLO FUNCIONA EN MI ORDENADOR
# PATH RELATIVO: SOLO FUNCIONA SI ESTAN EN EL MISMO WORKING DIRECTORY

# Te permite ejecutar el fichero si te posicionas directamente en él pero NO cuando lo importas
if __name__ == "__main__":
    csv = CSV(os.path.join(PATH4, "data/csv_barcelona.csv"))
    csv.plot()
    #csv.vistazo(show=True)
    #csv.plot()
    """
    csv_duplicados = csv.dropna()
    csv.vistazo(show=True)
    csv_duplicados.vistazo(show=True)
    #csv.vistazo(show=True)
    objeto_pr = CSVPreprocesamiento(csv.csv)
    obj = objeto_pr.dropna()
    """

    csv.vistazo(show=True)
    csv_2 = csv.dropna()
    print(csv_2)
    ##

    ######
    #Siempre cuando se crea algo!!!!! se tiene que primero utilizar solo
    #Luego se puede empalmar (linkar) con otras cosas
    #asi aseguramos darle las maximas cosas a utilizar al usuario ---> MODULARIDAD

    #objeto_plot = CSVPlot(csv.df)
    #objetos_plot.plot.plot()
    """
    print()
    # pd.set_option('max_rows', None)
    # pd.reset_option("max_rows")
    cabecera, final, columnas, faltantes, forma = csv.vistazo()
    print(forma)
    agrupar, describir, correlaciones, sesgo = csv.estadistica()
    csv.plot()
    df=csv.duplicados()
    print(df.shape)
    df=csv.dropna(number=1000, axis=1)
    print(df.shape)
    df=csv.dropna(number=10, axis=0)
    print(df.shape)
    df=csv.ints()
    print(df.dtypes)
    print(df.isnull().sum())
    df=csv.mvs(strategy="mode")
    print(df.isnull().sum())
    outliers = csv.outliers()
    print(outliers)
    csv.guardar_plot()
    pd.set_option('max_rows', None)
    #set_printoptions(precision=3)
    binar = csv.normalizada()
    print(binar[0:5,0:5])
    binar1 = csv.estandarizar()
    print(binar1[0:5,0:5])"""