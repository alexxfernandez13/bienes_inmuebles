import os
import pandas as pd
from bienes_inmuebles.dataset.csv_utilities import CSV, PATH4  # Importa clase csv y variable (CONSTANTE) PATH4

"""FUNCIONES --> API"""


def main():
    csv = CSV(os.path.join(PATH4, "data/csv_barcelona.csv"))
    # pd.set_option('max_rows', None)
    # pd.reset_option("max_rows")
    cabecera, final, columnas, faltantes, forma = csv.vistazo()
    print(cabecera, final, columnas, faltantes, forma)
    agrupar, describir, correlaciones, sesgo = csv.estadistica()
    print(agrupar)
    #csv.plot()
    csv_dup = csv.duplicados()
    breakpoint()
    csv.vistazo(csv_dup) #porque pone a show=1 #¿para mostrar cabecera?
    csv_na =csv_dup.dropna(number=1000, axis=1)
    print(csv_na.vistazo())
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

"""
csv = CSV("datos.csv")
csv_dupl = csv.duplicados()
csv_na = csv_dupl.dropna()

ml = ML(csv_na.df)
"""