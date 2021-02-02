import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bienes_inmuebles.dataset.csv_utilities import CSV
from bienes_inmuebles.dataset.csv_preprocesamiento import PATH4  # Importa clase csv y variable (CONSTANTE) PATH4

"""FUNCIONES --> API"""


def main():
    csv = CSV(os.path.join(PATH4, "data/datos_fotocasa_final.csv"))
    csv.vistazo()
    casteo_variables = {'precio':np.float64,
                      'tamano':np.float64,
                      'trastero':np.int64,
                      'balcon':np.int64,
                      'aireAcondicinado':np.int64,
                      'piscina':np.int64,
                      'ascensor':np.int64,
                      'terraza':np.int64,
                      'planta':np.int64}

    csv_casteados = csv.casteo_columnas(casteo_variables)
    csv_casteados.vistazo()

    # one hot encoding Garaje
    csv_oneHotEncoding = csv.one_hot_encoding("garaje")
    # one hot encoding Garaje

    # one hot encoding distrito
    csv_oneHotEncoding = csv.one_hot_encoding("distrito")
    # one hot encoding distrito

    # one hot encoding ciudad
    csv_oneHotEncoding = csv.one_hot_encoding("ciudad")
    # one hot encoding ciudad

    # one hot encoding eficienciaEnergetica
    csv_oneHotEncoding = csv.one_hot_encoding("eficienciaEnergetica")
    # one hot encoding eficienciaEnergetica

    print(csv_oneHotEncoding.df.head())
    print(csv_oneHotEncoding.vistazo())

    csv_dup = csv.duplicados()
    csv_na = csv_dup.dropna(number=10, axis=0)
    csv_int = csv_na.ints()
    csv_mvs = csv_int.mvs()
    csv_outliers = csv_mvs.outliers()
    estandarizar = csv_outliers.estandarizar()
    normalizar = csv_outliers.normalizar()



    #formulario
    enc = False
    while enc==False:
        tipoOperacion = input("Introduzca el tipo de operacion (1= Comprar, 2= Alquilar): \n")
        if (tipoOperacion=='1' or tipoOperacion=='2'):
            enc= True

    while enc==False:
        habitaciones = int(input("Introduzca las habiytaciones del inmueble (Minimo = 0, Max=16: \n"))
        if (habitaciones >= 0 or   habitaciones<=16):
            enc= True









    """csv = CSV(os.path.join(PATH4, "data/datos_fotocasa.csv"))
    pd.set_option('display.max_columns', None)
    csv.vistazo()"""




    """csv_dup = csv.duplicados()
    csv_na = csv_dup.dropna(number=10, axis=0)
    csv_int = csv_na.ints()
    csv_mvs = csv_int.mvs()
    csv_outliers = csv_mvs.outliers()
    estandarizar = csv_outliers.estandarizar()
    normalizar = csv_outliers.normalizar()"""

    """pd.set_option('max_rows', None)
    csv_binar = csv_outliers.normalizada()
    print(csv_binar.df[0:5, 0:5])
    binar1 = csv_outliers.estandarizar()
    print(binar1.df[0:5, 0:5])
    no_supervisado = NOsupervisado(binar1.df)
    print(no_supervisado.df)
    pca = no_supervisado.pca()
    # print(pca)
    #no_supervisado.df = pd.DataFrame(pca)
    # print("a")
    kmeans, labels, centroide = no_supervisado.kmeans_clustering(n_cluster=3)
    # print(kmeans)
    #no_supervisado.df = pd.DataFrame(kmeans)
    # no_supervisado.plot()
    plt.scatter(pca[:, 0],pca[:, 1],c=labels)
    plt.show()"""

""" COMMAND LINE / EJECUTAS LA FILE DIRECTO"""
if __name__ == "__main__":
    main()

"""
csv = CSV("datos.csv")
csv_dupl = csv.duplicados()
csv_na = csv_dupl.dropna()

ml = ML(csv_na.df)
"""
