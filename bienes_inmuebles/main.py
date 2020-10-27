import os
from bienes_inmuebles.dataset.csv_utilities import CSV, PATH4 #importo clase csv y variable PATH3


def main():
    objeto_csv = CSV(os.path.join(PATH4, "data/e05024001-estadisticas-impuesto-de-bienes-inmuebles.csv"))
    print(objeto_csv.df)



#### NUeva carpeta (dataset), nuevo archivo pytho donde definas la funcion, tienes que importarlo en el main
## y ejecutarlo


main()