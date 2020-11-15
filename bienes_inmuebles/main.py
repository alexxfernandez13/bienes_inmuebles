import os
from bienes_inmuebles.dataset.csv_utilities import CSV, PATH4  # Importa clase csv y variable (CONSTANTE) PATH4
import pandas as pd

"""FUNCIONES --> API"""


def main():
    csv = CSV(os.path.join(PATH4, "data/csv_barcelona.csv"))
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
    df=csv.mvs()
    print(df.isnull().sum())
    outliers = csv.outliers()
    print(outliers)
    csv.guardar_plot()
    pd.set_option('max_rows', None)
    #set_printoptions(precision=3)
    binar = csv.normalizada()
    print(binar[0:5,0:5])
    binar1 = csv.estandarizar()
    print(binar1[0:5,0:5])


""" COMMAND LINE / EJECUTAS LA FILE DIRECTO"""
if __name__ == "__main__":
    main()
