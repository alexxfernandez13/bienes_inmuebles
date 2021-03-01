import os
import pandas as pd
import numpy as np
from joblib import dump, load
from copy import copy

from bienes_inmuebles.preprocesar.csv_exploracion import CSVExploracion
from bienes_inmuebles.preprocesar.csv_plot import CSVPlot
from bienes_inmuebles.preprocesar.csv_abrir import CSV
from bienes_inmuebles.preprocesar.csv_preprocesamiento import PATH4
from bienes_inmuebles.machine_learning.supervisado import prepare_dataset, regresion
from sklearn.ensemble import GradientBoostingRegressor
from bienes_inmuebles.utilidades.urlPath import UrlPath

"""FUNCIONES --> API"""
def main():
    """Carga de CSV y configura la informacion por pantalla de Pandas mostrando TODOS los atributos"""
    csv = CSV(os.path.join(PATH4, "data/datos_fotocasa_final.csv"))
    pd.set_option('display.max_columns', None)

    """Casteo Atributos en Enteros"""
    casteo_variables = {'precio': np.float64,
                        'tamano': np.float64,
                        'trastero': np.int64,
                        'balcon': np.int64,
                        'aireAcondicinado': np.int64,
                        'piscina': np.int64,
                        'ascensor': np.int64,
                        'terraza': np.int64,
                        'planta': np.int64}
    csv_casteados = csv.casteo_columnas(casteo_variables)

    """One Hot Encoding de Atributos Categoricos"""
    csv_oneHotEncoding = csv_casteados.one_hot_encoding("garaje")
    csv_oneHotEncoding = csv_oneHotEncoding.one_hot_encoding("distrito")
    csv_oneHotEncoding = csv_oneHotEncoding.one_hot_encoding("ciudad")
    csv = csv_oneHotEncoding.one_hot_encoding("eficienciaEnergetica")

    """Preprocesamiento"""
    csv_dup = csv.duplicados()
    csv_na = csv_dup.dropna(number=10, axis=0)
    csv_int = csv_na.ints()
    csv_mvs = csv_int.mvs()
    # csv_outlier = csv_int.outliers()

    """Analitica Descriptiva"""
    print("\n------------------------ Analisis Dataset ------------------------")
    csv_mvs.vistazo()
    print("\n------------------------ Estadistica Dataset ------------------------")
    csv_mvs.estadistica()

    """Plots"""
    csv_mvs.borrar_output()
    csv_mvs.plot_histograma()
    csv_mvs.plot_densidad()
    csv_mvs.plot_bigotes()
    csv_mvs.plot_correlacion()
    # csv_mvs.plot_dispersion()

    """Separar datos en 2 Dataframe, uno para compra y otro para alquiler"""
    csv_compra = copy(csv_mvs)
    csv_alquiler = copy(csv_mvs)

    csv_compra.df = csv_mvs.df.loc[
        (csv_mvs.df['tipoOperacion'] == 1) & (csv_mvs.df['precio'] >= 50000) & (csv_mvs.df["tamano"] >= 10)]
    csv_alquiler.df = csv_mvs.df.loc[
        (csv_mvs.df["tipoOperacion"] == 2) & (csv_mvs.df["precio"] <= 9000) & (csv_mvs.df["precio"] >= 100) & (
                csv_mvs.df["tamano"] >= 10)]

    # creacion de csv a partir de dataframe de compra
    if os.path.exists(str(UrlPath.getPath(__file__, 2)) + "\data\csv_compra.csv"):
        os.remove(str(UrlPath.getPath(__file__, 2)) + "\data\csv_compra.csv")
    csv_compra.df.to_csv(str(UrlPath.getPath(__file__, 2)) + "\data\csv_compra.csv", index=False)

    # creacion de csv a partir de dataframe de alquiler
    if os.path.exists(str(UrlPath.getPath(__file__, 2)) + "\data\csv_alquiler.csv"):
        os.remove(str(UrlPath.getPath(__file__, 2)) + "\data\csv_alquiler.csv")
    csv_alquiler.df.to_csv(str(UrlPath.getPath(__file__, 2)) + "\data\csv_alquiler.csv", index=False)

    """COMPRA - Separar X e Y"""
    # Estandarizar Columna X --> Optimiza el Modelado
    X_columns_df_compra = csv_compra.df[['tipoInmueble', 'tipoOperacion', 'habitaciones',
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
    Y_columns_Compra = csv_compra.df['precio'].values

    """COMPRA - Evaluacion Modelos"""
    X_train, X_test, y_train, y_test = prepare_dataset(X_columns_Compra, Y_columns_Compra)
    print("\n------------------------ Scoring Modelos - Compra ------------------------")
    #regresion(X_train, X_test, y_train, y_test)
    print("------------------------ Scoring Modelos - Compra ------------------------")

    """COMPRA - Guardar Modelo Seleccionado"""
    modelo_compra = GradientBoostingRegressor()
    modelo_compra.fit(X_columns_Compra, Y_columns_Compra) # Entrenar el modelo final con TODOS los datos posibles
    dump(modelo_compra, os.path.join(PATH4, "data/model_compra.joblib"))


    """ALQUILER - Separar X e Y"""
    # Estandarizar Columna X --> Optimiza el Modelado
    X_columns_df_alquier = csv_alquiler.df[['tipoInmueble', 'tipoOperacion', 'habitaciones',
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
    Y_columns_Alquiler = csv_alquiler.df['precio'].values

    """ALQUILER - Evaluacion Modelos"""
    X_train, X_test, y_train, y_test = prepare_dataset(X_columns_Alquiler, Y_columns_Alquiler)
    print("\n------------------------ Scoring Modelos - Alquiler ------------------------")
    #regresion(X_train, X_test, y_train, y_test)
    print("------------------------ Scoring Modelos - Alquiler ------------------------")

    """Alquiler - Guardar Modelo Seleccionado"""
    modelo_alquiler = GradientBoostingRegressor()
    modelo_alquiler.fit(X_columns_Alquiler, Y_columns_Alquiler) # Entrenar el modelo final con TODOS los datos posibles
    dump(modelo_alquiler, os.path.join(PATH4, "data/model_alquiler.joblib"))

    """Seleccionar fila del Dataset para comprobar Funcionamiento del Modelo"""
    print("\n------------------------ Comprobacion Funcionamiento Modelo ------------------------")

    print("-> 1ª fila Compra - Columna X Estandarizada:\n", X_columns_Compra[0, :])
    print("-> Precio 1ª fila Compra: ", Y_columns_Compra[0])
    print("\n-> 1ª fila Alquiler - Columna X Estandarizada:\n", X_columns_Alquiler[0, :])
    print("-> Precio 1ª fila Compra: ",Y_columns_Alquiler[0])

    """
    0) Separar el dataset:
        En X y Y
        Estandarizar X y guardar escaler
        No tocar las Y ya que queremos aprender como son
        Entrenar con X estandarizadas y Y normales
        Guardar Modelo

    1) Entrenado modelo:
        CV score : 0.95 (: --> Esta aprendiendo algo
        Test score: 0.95 (: --> Funciona en datos que no ha visto hasta ahora

    2) Prediccion modelo: 
        Saca datos consistentes (: --> Funcion

    3) Asegurarte que funciona:
        Datos de fotocasa --> Coger un edificio --> Coger sus features X --> Hacer la predicion y comparar con su precio real
    """


""" COMMAND LINE / EJECUTAS LA FILE DIRECTO"""
if __name__ == "__main__":
    main()
