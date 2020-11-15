"""IMPORTS"""
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
class CSVPlot ():
    def __init__(self, df):
        self.df =df

    def plot (self, grafico = 2, columnas = []):
        if columnas:
            df = self.df[columnas]
        else:
            df = self.df
        if grafico == 0:
            self.plot_histograma(df)
        elif grafico == 1:
            self.plot_densidad(df)
        elif grafico == 2:
            self.plot_bigotes(df)
        elif grafico == 3:
            self.plot_correlacion(df)
        elif grafico == 4:
            self.plot_dispersion(df)
        else:
            pass

    def plot_histograma(self,df):
        df.hist()
        plt.show()

    def plot_densidad(self,df):
        df.plot(subplots=True, layout=(10, 4), sharex=False)  # kind="density" ¿No funciona?
        plt.show()

    def plot_bigotes(self,df):
        df.plot(kind='box', subplots=True, layout=(10, 4), sharex=False, sharey=False)
        plt.show()

    def plot_correlacion(self,df):
        correlaciones = df.corr()
        fig = plt.figure()
        ax = fig.add_subplot(111)
        cax = ax.matshow(correlaciones, vmin=-1, vmax=1)
        fig.colorbar(cax)
        plt.show()

    def plot_dispersion(self,df):
        scatter_matrix(df)
        plt.show()

    def guardar_plot(self, save = True):  # Opcion a guardar el plot
        columns = self.df.columns.values
        for column in columns:
            try:
                self.df.hist(column = column)
                if save:
                    my_file=f'data/{column}.png'
                    plt.savefig(os.path.join(PATH4, my_file))
                else:
                    pass
            except ValueError:
                pass
    """Opcion a eliminar el plot"""


class CSVExploracion(CSVPlot):

    def __init__(self, df):
        self.df = df

    def vistazo(self, show=False):  # ¿Pasar lineas predeterminadas?
        if show:
            self.df.info()
        else:
            pass
        cabecera = self.df.head()
        final = self.df.tail()
        columnas = self.df.columns.values
        faltantes = self.df.isnull().sum()
        forma = self.df.shape
        return cabecera, final, columnas, faltantes, forma

    def estadistica(self, columnas = [], agrupar = None, method = "pearson"):
        if columnas:
            df = self.df[columnas]
        else:
            df = self.df
        try:
            agrupar = df.groupby(agrupar).size()
        except TypeError:
            agrupar = None
        describir = df.describe()
        correlaciones = df.corr(method=method)
        sesgo = df.skew()
        return agrupar, describir, correlaciones, sesgo


"""
VEHICULO --> MOTO


"""
#class Moto(VEHICULO)
#HIJO(PADRE)
class CSV(CSVExploracion):

    def __init__(self, csv):
        self.csv = csv
        self.df = pd.read_csv(self.csv)
        #self.df_procesada = self.df.copy()
    """
    def vistazo(self,show=False):  # ¿Pasar lineas predeterminadas?
        if show:
            self.df.info()
        else:
            pass
        cabecera = self.df.head()
        final = self.df.tail()
        columnas = self.df.columns.values
        faltantes = self.df.isnull().sum()
        forma = self.df.shape
        return cabecera, final, columnas, faltantes, forma

    def estadistica(self, columnas = [], agrupar = None, method = "pearson"):
        if columnas:
            df = self.df[columnas]
        else:
            df = self.df
        try:
            agrupar = df.groupby(agrupar).size()
        except TypeError:
            agrupar = None
        describir = df.describe()
        correlaciones = df.corr(method=method)
        sesgo = df.skew()
        return agrupar, describir, correlaciones, sesgo
    """



    def duplicados(self, inplace=False):
        """
        df_resultado = self.df.drop_duplicades()
        nuevo_objeto = CSV(self.csv)
        nuevo_objeto.df = df_resultado
        return nuevo_objeto

        csv = CSV("input.csv")
        csv_sin_duplicados = csv.drop_duplicados()
        """
        df_resultado = self.df.drop_duplicates()
        return self._inplace("df", df_resultado, inplace) # se le puede el csv antes de leerlo o el dataframe df


    def _inplace (self, atributo, valor_atributo, inplace=False):
        if inplace:
            setattr(self, atributo, valor_atributo)
        else:
            nuevo_objeto = CSV(self.csv)
            setattr(self, atributo, valor_atributo)
            return nuevo_objeto

    def dropna(self, number = 10000, axis = 1, inplace=False):  #Elimina filas/registros axis=0 o columnas/atributos si axis=1. El limite de NaN lo marca number
        length = self.df.shape[axis - 1]  # -1 ¿porque era esto?
        df_resultado = self.df.dropna(thresh=length - number, axis=axis)
        self.csv = df_resultado
        return self._inplace("df", df_resultado, inplace)

    def ints(self):
        self.df_procesada = self.df_procesada.select_dtypes(include=["int64", "float64"])
        return self.df_procesada

    def mvs(self, columns = None, strategy = "mean"):
        imp_mean = SimpleImputer(missing_values = np.nan, strategy = strategy)
        aux = imp_mean.fit_transform(self.df_procesada)
        try:
            self.df_procesada = pd.DataFrame(data = aux, columns = self.df_procesada.columns)
        except ValueError:
            raise ValueError("Necesitas borrar columnas con NANs y columnas con Strings primero. Ejecutar self.dropna() y self.ints() antes de self.mvs()")
        return self.df_procesada

    def outliers(self,  grado = 3):  # Eliminar filas con outlier y escoger grado de eliminacion)
        z_scores = stats.zscore(self.df_procesada)  # self.df.values ????
        where_are_NaNs = isnan(z_scores)
        z_scores[where_are_NaNs] = 0
        abs_z_scores = np.abs(z_scores)
        filtered_entries = (abs_z_scores < grado).all(axis = 1)  # buscar solucion para sustituir nan por 0 en la lista de listas
        self.df_procesada = self.df_procesada[filtered_entries]
        return self.df_procesada

    def reescalar(self):
        scaler = MinMaxScaler(feature_range = (0, 1))
        self.df_reescalar = scaler.fit_transform(self.df_procesada)
        return self.df_reescalar

    def estandarizar (self):
        scaler = StandardScaler().fit(self.df_procesada)
        self.df_estandarizada = scaler.transform(self.df_procesada)
        return self.df_estandarizada

    def normalizada (self):
        scaler = Normalizer().fit(self.df_procesada)
        self.df_normalizada = scaler.transform(self.df_procesada)
        return self.df_normalizada

    def binarizar (self):
        binarizer = Binarizer(threshold=0.0).fit(self.df_procesada)
        self.binarizada = binarizer.transform(self.df_procesada)
        return self.binarizada







"""EJECUCION"""
# PATH ABSOLUTO: SOLO FUNCIONA EN MI ORDENADOR
# PATH RELATIVO: SOLO FUNCIONA SI ESTAN EN EL MISMO WORKING DIRECTORY

# Te permite ejecutar el fichero si te posicionas directamente en él pero NO cuando lo importas
if __name__ == "__main__":
    csv = CSV(os.path.join(PATH4, "data/csv_barcelona.csv"))
    csv.vistazo(show=True)
    csv.plot()

    ##

    ######
    #Siempre cuando se crea algo!!!!! se tiene que primero utilizar solo
    #Luego se puede empalmar (linkar) con otras cosas
    #asi aseguramos darle las maximas cosas a utilizar al usuario ---> MODULARIDAD

    #objeto_plot = CSVPlot(csv.df)
    #objetos.plot.plot()
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