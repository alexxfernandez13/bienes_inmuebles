import os
import pandas as pd
import numpy as np
from joblib import dump
from copy import copy
import  matplotlib.pyplot as plt

from bienes_inmuebles.preprocesar.csv_abrir import CSV
from bienes_inmuebles.preprocesar.csv_preprocesamiento import PATH4
from bienes_inmuebles.machine_learning.supervisado import prepare_dataset, regresion
from sklearn.ensemble import GradientBoostingRegressor
from bienes_inmuebles.utilidades.urlPath import UrlPath
from sklearn.ensemble import ExtraTreesRegressor


def main():
    """Carga de CSV y configura la informacion por pantalla de Pandas mostrando TODOS los atributos"""
    csv = CSV(os.path.join(PATH4, "data/datos_fotocasa_final.csv"))
    pd.set_option('display.max_columns', None)

    casteo_variables = {'precio': np.float64,
                        'tamano': np.float64,
                        'trastero': np.int64,
                        'balcon': np.int64,
                        'aireAcondicinado': np.int64,
                        'piscina': np.int64,
                        'ascensor': np.int64,
                        'terraza': np.int64,
                        'planta': np.int64}
    csv_compra_casteados = csv.casteo_columnas(casteo_variables)
    """One Hot Encoding de Atributos Categoricos"""
    csv_oneHotEncoding = csv.one_hot_encoding("garaje")
    csv_oneHotEncoding = csv_oneHotEncoding.one_hot_encoding("distrito")
    csv_oneHotEncoding = csv_oneHotEncoding.one_hot_encoding("ciudad")
    csv = csv_oneHotEncoding.one_hot_encoding("eficienciaEnergetica")

    casteo_variables = {'tipoInmueble': np.int64,
                        'tipoOperacion': np.int64,
                        'habitaciones': np.int64,
                        'tamano': np.int64,
                        'planta': np.int64,
                        'ascensor': np.int64,
                        'terraza': np.int64,
                        'trastero': np.int64,
                        'balcon': np.int64,
                        'aireAcondicinado': np.int64,
                        'piscina': np.int64,
                        'banos': np.int64,
                        'garaje_Comunitario': np.int64,
                        'garaje_No-detallado': np.int64,
                        'garaje_Privado': np.int64,
                        'distrito_arganzuela': np.int64,
                        'distrito_barajas': np.int64,
                        'distrito_carabanchel': np.int64,
                        'distrito_centro': np.int64,
                        'distrito_chamartin': np.int64,
                        'distrito_chamberi': np.int64,
                        'distrito_ciudad-lineal': np.int64,
                        'distrito_fuencarral': np.int64,
                        'distrito_hortaleza': np.int64,
                        'distrito_latina': np.int64,
                        'distrito_moncloa': np.int64,
                        'distrito_moratalaz': np.int64,
                        'distrito_puente-de-vallecas': np.int64,
                        'distrito_retiro': np.int64,
                        'distrito_salamanca': np.int64,
                        'distrito_san-blas': np.int64,
                        'distrito_tetuan': np.int64,
                        'distrito_usera': np.int64,
                        'distrito_vicalvaro': np.int64,
                        'distrito_villa-de-vallecas': np.int64,
                        'distrito_villaverde': np.int64,
                        'ciudad_madrid-capital': np.int64,
                        'eficienciaEnergetica_A': np.int64,
                        'eficienciaEnergetica_B': np.int64,
                        'eficienciaEnergetica_C': np.int64,
                        'precio': np.int64}


    csv_casteados_2_vez = csv_mvs.casteo_columnas(casteo_variables)

    csv_casteados_2_vez.vistazo()
    """Analitica Descriptiva"""
    print("\n------------------------ Analisis Dataset ------------------------")
    csv_mvs.vistazo()
    print("\n------------------------ Estadistica Dataset ------------------------")
    csv_mvs.estadistica()

    """Plots"""
    csv_mvs.borrar_output()
    csv_mvs.plot_histograma()
    csv_mvs.plot_densidad()
    csv_mvs.plot_bigotes(plot_columnas=["precio",'distrito_centro'])
    csv_mvs.plot_correlacion()
    csv_mvs.plot_dispersion()

    """Separar datos en 2 Dataframe, uno para compra y otro para alquiler"""
    csv_compra = copy(csv_mvs)
    csv_alquiler = copy(csv_mvs)

    csv_compra.df = csv_mvs.df.loc[
        (csv_mvs.df['tipoOperacion'] == 1) & (csv_mvs.df['precio'] >= 50000) & (csv_mvs.df["tamano"] >= 10)]
    csv_alquiler.df = csv_mvs.df.loc[
        (csv_mvs.df["tipoOperacion"] == 2) & (csv_mvs.df["precio"] <= 9000) & (csv_mvs.df["precio"] >= 100) & (
                csv_mvs.df["tamano"] >= 10)]

    csv = csv.casteo_columnas(casteo_variables)
    csv_dup = csv.duplicados()
    csv_na = csv_dup.dropna(number=10, axis=0)
    csv_mvs = csv_na.mvs()

# --------------------- COMPRA ---------------------
    csv_compra = copy(csv)
    csv_compra.df = csv.df.loc[(csv.df['tipoOperacion'] == 1)]

    print(csv_compra.df.shape)

    """csv_compra.plot_bigotes(plot_columnas=['banos'])
    csv_compra.plot_bigotes(plot_columnas=['habitaciones'])
    csv_compra.plot_bigotes(plot_columnas=['planta'])
    csv_compra.plot_bigotes(plot_columnas=['tamano'])
    csv_compra.plot_bigotes(plot_columnas=['precio'])"""

    csv_compra__out = copy(csv_compra)
    csv_compra__out.outliers_nuevo(q1=0.25, q2=0.75)

    print(csv_compra__out.df.shape)

    """csv_compra__out.plot_bigotes(plot_columnas=['banos'])
    csv_compra__out.plot_bigotes(plot_columnas=['habitaciones'])
    csv_compra__out.plot_bigotes(plot_columnas=['planta'])
    csv_compra__out.plot_bigotes(plot_columnas=['tamano'])
    csv_compra__out.plot_bigotes(plot_columnas=['precio'])"""

    #csv_compra__out.scatter_2variables(var1='tamano', var2='precio')


    # creacion de csv a partir de dataframe de compra
    if os.path.exists(str(UrlPath.getPath(__file__, 2)) + "\data\csv_compra.csv"):
        os.remove(str(UrlPath.getPath(__file__, 2)) + "\data\csv_compra.csv")
    csv_compra__out.df.to_csv(str(UrlPath.getPath(__file__, 2)) + "\data\csv_compra.csv", index=False)

    """COMPRA - Separar X e Y"""
    # Estandarizar Columna X --> Optimiza el Modelado
    X_columns_df_compra = csv_compra__out.df[['tipoInmueble', 'tipoOperacion', 'habitaciones',
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
                                              'eficienciaEnergetica_B', 'eficienciaEnergetica_C']]
    csv_Compra_X = CSV(df=X_columns_df_compra)
    csv_Compra_X_estandarizada = csv_Compra_X.estandarizar(os.path.join(PATH4, "data/scaler_compra.pkl"))
    X_columns_Compra = csv_Compra_X_estandarizada.df.values

    # Columna Y NO Estandarizada
    Y_columns_Compra = csv_compra__out.df['precio'].values

    """COMPRA - Evaluacion Modelos"""
    X_train, X_test, y_train, y_test = prepare_dataset(X_columns_Compra, Y_columns_Compra)
    print("\n------------------------ Scoring Modelos - Compra ------------------------")
    regresion(X_train, X_test, y_train, y_test)
    print("------------------------ Scoring Modelos - Compra ------------------------")
    """Seleccionar fila del Dataset para comprobar Funcionamiento del Modelo"""
    print("\n------------------------ Comprobacion Funcionamiento Modelo ------------------------")

    print("-> 1ª fila Compra - Columna X Estandarizada:\n", X_columns_Compra[0, :])
    print("-> Precio 1ª fila Compra: ", Y_columns_Compra[0])
    print("\n-> 1ª fila Alquiler - Columna X Estandarizada:\n", X_columns_Compra[0, :])
    print("-> Precio 1ª fila Compra: ", Y_columns_Compra[0])

    """COMPRA - Guardar Modelo Seleccionado"""
    modelo_compra = ExtraTreesRegressor()
    modelo_compra.fit(X_columns_Compra, Y_columns_Compra)  # Entrenar el modelo final con TODOS los datos posibles
    dump(modelo_compra, os.path.join(PATH4, "data/model_compra.joblib"))

    csv_compra__out.estadistica()
# --------------------- COMPRA ---------------------

#--------------------- ALQUILER ---------------------
    csv_alquiler = copy(csv)
    csv_alquiler.df = csv.df.loc[(csv.df['tipoOperacion'] == 2)]

    print(csv_alquiler.df.shape)

    """csv_alquiler.plot_bigotes(plot_columnas=['banos'])
    csv_alquiler.plot_bigotes(plot_columnas=['habitaciones'])
    csv_alquiler.plot_bigotes(plot_columnas=['planta'])
    csv_alquiler.plot_bigotes(plot_columnas=['tamano'])
    csv_alquiler.plot_bigotes(plot_columnas=['precio'])"""

    csv_alquiler__out = copy(csv_alquiler)
    csv_alquiler__out.outliers_nuevo(q1=0.1, q2=0.9)

    print(csv_alquiler__out.df.shape)

    """csv_alquiler__out.plot_bigotes(plot_columnas=['banos'])
    csv_alquiler__out.plot_bigotes(plot_columnas=['habitaciones'])
    csv_alquiler__out.plot_bigotes(plot_columnas=['planta'])
    csv_alquiler__out.plot_bigotes(plot_columnas=['tamano'])
    csv_alquiler__out.plot_bigotes(plot_columnas=['precio'])"""

    #csv_alquiler__out.scatter_2variables(var1='tamano', var2='precio')

    # creacion de csv a partir de dataframe de alquiler
    if os.path.exists(str(UrlPath.getPath(__file__, 2)) + "\data\csv_alquiler.csv"):
        os.remove(str(UrlPath.getPath(__file__, 2)) + "\data\csv_alquiler.csv")
    csv_alquiler__out.df.to_csv(str(UrlPath.getPath(__file__, 2)) + "\data\csv_alquiler.csv", index=False)

    """ALQUILER - Separar X e Y"""
    # Estandarizar Columna X --> Optimiza el Modelado
    X_columns_df_alquier = csv_alquiler__out.df[['tipoInmueble', 'tipoOperacion', 'habitaciones',
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
                                                 'eficienciaEnergetica_B', 'eficienciaEnergetica_C']]
    csv_Alquiler_X = CSV(df=X_columns_df_alquier)
    csv_Alquiler_X_estandarizada = csv_Alquiler_X.estandarizar(os.path.join(PATH4, "data/scaler_alquiler.pkl"))
    X_columns_Alquiler = csv_Alquiler_X_estandarizada.df.values

    # Columna Y NO Estandarizada
    Y_columns_Alquiler = csv_alquiler__out.df['precio'].values

    """ALQUILER - Evaluacion Modelos"""
    X_train, X_test, y_train, y_test = prepare_dataset(X_columns_Alquiler, Y_columns_Alquiler)
    print("\n------------------------ Scoring Modelos - Alquiler ------------------------")
    regresion(X_train, X_test, y_train, y_test)
    print("------------------------ Scoring Modelos - Alquiler ------------------------")
    """Seleccionar fila del Dataset para comprobar Funcionamiento del Modelo"""
    print("\n------------------------ Comprobacion Funcionamiento Modelo ------------------------")

    print("-> 1ª fila Compra - Columna X Estandarizada:\n", X_columns_Compra[0, :])
    print("-> Precio 1ª fila Compra: ", Y_columns_Compra[0])
    print("\n-> 1ª fila Alquiler - Columna X Estandarizada:\n", X_columns_Alquiler[0, :])
    print("-> Precio 1ª fila Compra: ", Y_columns_Alquiler[0])

    """Alquiler - Guardar Modelo Seleccionado"""
    modelo_alquiler = GradientBoostingRegressor()
    modelo_alquiler.fit(X_columns_Alquiler, Y_columns_Alquiler)  # Entrenar el modelo final con TODOS los datos posibles
    dump(modelo_alquiler, os.path.join(PATH4, "data/model_alquiler.joblib"))

    csv_alquiler__out.estadistica()

#--------------------- ALQUILER ---------------------

#--------------------- creacion de csv a partir de dataframe total (comprar y alquilar) ---------------------
    df_preprocesado = pd.concat([csv_compra__out.df, csv_alquiler__out.df])

    if os.path.exists(str(UrlPath.getPath(__file__, 2)) + "\data\csv_preprocesado.csv"):
        os.remove(str(UrlPath.getPath(__file__, 2)) + "\data\csv_preprocesado.csv")
    df_preprocesado.to_csv(str(UrlPath.getPath(__file__, 2)) + "\data\csv_preprocesado.csv", index=False)
#--------------------- creacion de csv a partir de dataframe total (comprar y alquilar) ---------------------





""" COMMAND LINE / EJECUTAS LA FILE DIRECTO"""
if __name__ == "__main__":
    main()
