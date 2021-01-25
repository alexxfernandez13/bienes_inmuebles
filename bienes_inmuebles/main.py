import os
import pandas as pd
import matplotlib.pyplot as plt
from bienes_inmuebles.dataset.csv_utilities import CSV
from bienes_inmuebles.dataset.csv_preprocesamiento import PATH4  # Importa clase csv y variable (CONSTANTE) PATH4

"""FUNCIONES --> API"""


def main():
    csv = CSV(os.path.join(PATH4, "data/datos_fotocasa.csv"))
    pd.set_option('display.max_columns', None)
    csv.vistazo()
    csv_dup = csv.duplicados()
    csv_na = csv_dup.dropna(number=10, axis=0)
    csv_int = csv_na.ints()
    csv_mvs = csv_int.mvs()
    csv_outliers = csv_mvs.outliers()
    estandarizar = csv_outliers.estandarizar()
    normalizar = csv_outliers.normalizar()

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
