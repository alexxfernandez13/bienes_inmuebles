import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from joblib import dump, load

from bienes_inmuebles.dataset.csv_plot import CSVPlot
from bienes_inmuebles.dataset.csv_utilities import CSV
from bienes_inmuebles.dataset.csv_preprocesamiento import PATH4  # Importa clase csv y variable (CONSTANTE) PATH4
from bienes_inmuebles.machine_learning.supervisado import prepare_dataset, regresion,clasificacion, Supervisado
from sklearn.ensemble import GradientBoostingRegressor
"""FUNCIONES --> API"""


def main():
    csv = CSV(os.path.join(PATH4, "data/datos_fotocasa_final2.csv"))
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
    csv_oneHotEncoding = csv_oneHotEncoding.one_hot_encoding("distrito")
    # one hot encoding distrito

    # one hot encoding ciudad
    csv_oneHotEncoding = csv_oneHotEncoding.one_hot_encoding("ciudad")
    # one hot encoding ciudad

    # one hot encoding eficienciaEnergetica
    csv = csv_oneHotEncoding.one_hot_encoding("eficienciaEnergetica")
    # one hot encoding eficienciaEnergetica


    print("1",csv.df.columns)
    csv_dup = csv.duplicados()
    print("2",csv_dup.df.columns)
    csv_na = csv_dup.dropna(number=10, axis=0)
    print("3",csv_na.df.columns)
    csv_int = csv_na.ints()
    print(csv_na.vistazo())
    print("4",csv_int.df.columns)
    csv_mvs = csv_int.mvs()
    print("5",csv_mvs.df.columns)
    csv_outliers = csv_mvs.outliers()
    print("6",csv_outliers.df.columns)
    estandarizar = csv_outliers.estandarizar()

    print(estandarizar.df.columns)

    X_columns = estandarizar.df[['tipoInmueble', 'tipoOperacion', 'habitaciones',
       'tamano', 'planta', 'ascensor', 'terraza', 'trastero', 'balcon',
       'aireAcondicinado', 'piscina', 'banos', 'garaje_Comunitario',
       'garaje_No-detallado', 'garaje_Privado', 'distrito_arganzuela',
       'distrito_barajas', 'distrito_carabanchel', 'distrito_centro',
       'distrito_chamartin', 'distrito_chamberi',
       'distrito_ciudad-lineal', 'distrito_fuencarral',
       'distrito_hortaleza', 'distrito_latina', 'distrito_moncloa',
       'distrito_moratalaz', 'distrito_puente-de-vallecas',
       'distrito_retiro', 'distrito_salamanca', 'distrito_san-blas',
       'distrito_tetuan', 'distrito_usera', 'distrito_vicalvaro',
       'distrito_villa-de-vallecas', 'distrito_villaverde',
       'ciudad_madrid-capital', 'eficienciaEnergetica_A',
       'eficienciaEnergetica_B', 'eficienciaEnergetica_C']].values
    Y_columns = estandarizar.df['precio'].values
    X_train, X_test, y_train, y_test = prepare_dataset(X_columns,Y_columns)
    # regresion(X_train, X_test, y_train, y_test)
    # importante cuando se entrena el modelo final con todos los datos posibles
    modelo = GradientBoostingRegressor()
    modelo.fit(X_columns,Y_columns)

    dump(modelo,os.path.join(PATH4, "data/filename.joblib"))

    # clf = load('filename.joblib')
    #normalizar.plot_histograma()










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
