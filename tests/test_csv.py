import os
from bienes_inmuebles.dataset.csv_preprocesamiento import CSV, PATH4


def test_cvs_to_dataframe():
    objeto_csv = CSV(os.path.join(PATH4, "data/csv_barcelona.csv"))
    assert objeto_csv.df.columns[1] == "listing_url"#funcion de comprobacion -> como un if para test

"""test de que plot sale bien, guardar grafico en png, ver que la file existe 

def test_plot():
    csv.plot(save=True)
    assert file_existe? """

def test_plot():
    csv = CSV(os.path.join(PATH4, "data/csv_barcelona.csv"))
    csv.guardar_plot(save=True)
    assert os.path.exists(os.path.join(PATH4, "data/bathrooms.png"))# convierte path relativo en absoluto
"""test funciones nuevas"""

def test_vistazo():
    csv = CSV(os.path.join(PATH4, "data/csv_barcelona.csv"))
    cabecera, final, columnas, faltantes, forma = csv.vistazo()
    assert "neighborhood_overview" in columnas
    assert  "https://www.airbnb.com/rooms/21974"  in cabecera.values[0]