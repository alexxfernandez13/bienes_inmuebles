import os
from bienes_inmuebles.dataset.csv_utilities import CSV, PATH4  # Importa clase csv y variable (CONSTANTE) PATH4



"""FUNCIONES --> API"""
def main():
    csv = CSV(os.path.join(PATH4, "data/csv_barcelona.csv"))
    print(csv.df)


""" COMMAND LINE / EJECUTAS LA FILE DIRECTO"""
if __name__ == "__main__":
    main()
