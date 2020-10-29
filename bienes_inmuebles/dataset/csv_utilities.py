"""IMPORTS"""
import os
import pandas as pd
from pathlib import Path

"""CONSTANTES (se ponen en mayuscula)"""
path = Path(__file__)  # PATH A LA FILE EN CUALQUIER ORDENADOR
path2 = Path(path.parent)  # La funcion path.parent va un directorio hacia atras
path3 = Path(path2.parent)
PATH4 = str(Path(path3.parent))

"""DEF CLASES FUNCT"""


class CSV():
    def __init__(self, csv):
        self.csv = csv
        self.df = pd.read_csv(self.csv)


"""EJECUCION"""
# PATH ABSOLUTO: SOLO FUNCIONA EN MI ORDENADOR
# PATH RELATIVO: SOLO FUNCIONA SI ESTAN EN EL MISMO WORKING DIRECTORY

#Te deja escoger si correr eso cuando la ejetucas directamente pero no correrlo cuando lo importas desde otra
if __name__ == "__main__":
    objeto_csv = CSV(os.path.join(PATH4, "data/csv_barcelona.csv"))
    print(objeto_csv)
