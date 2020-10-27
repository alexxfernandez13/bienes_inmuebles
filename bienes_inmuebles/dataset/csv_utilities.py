#####IMPORTS
import os
import pandas as pd
from pathlib import Path

######CONSTANTES (se ponen en mayuscula)
path = Path(__file__) #### PATH A LA FILE EN CUALQUIER ORDENADOR
path2 = Path(path.parent)
path3 = Path(path2.parent)
PATH4 = str(Path(path3.parent))

######DEF CLASES FUNCT
class CSV():
    def __init__(self, csv):
        self.csv = csv
        self.df = pd.read_csv(self.csv)

#EJECUCION
#### ABSOLUTO: SOLO FUNCIONA EN MI ORDENADOR
####RELATIVO: SOLO FUNCIONA SI ESTAN EN EL MISMO WORKING DIRECTORY
objeto_csv = CSV (os.path.join(PATH4, "data/e05024001-estadisticas-impuesto-de-bienes-inmuebles.csv"))
print(objeto_csv.df)
#va a buscarlo uno para atras y luego busca el data
