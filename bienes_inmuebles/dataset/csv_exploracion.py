import pandas as pd
from bienes_inmuebles.dataset.csv_plot import CSVPlot


class CSVExploracion(CSVPlot):

    def __init__(self, df):
        self.df = df
    """Muestra informacion general del dataset con show_info=True o especifica con show_info=False"""
    def vistazo(self, show_info=False):  # ¿Pasar lineas predeterminadas?
        if show_info:
            self.df.info()
        else:
            pass
        cabecera = self.df.head()
        final = self.df.tail()
        columnas = self.df.columns.values
        faltantes = self.df.isnull().sum()
        forma = self.df.shape
        print(cabecera, final, columnas, faltantes, forma)
        return cabecera, final, columnas, faltantes, forma

    """Muestra informacion estadistica del dataset. Se le puede indicar columnas especificas pasandolas por una lista"""
    def estadistica(self, columnas=[], agrupar=None, method="pearson"):
        if columnas:
            df = self.df[columnas]
        else:
            df = self.df
        try:
            agrupar = df.groupby(agrupar).size()
        except TypeError:
            agrupar = None
        describir = df.describe()
        correlaciones = df.corr(method=method)
        sesgo = df.skew()
        print(agrupar, describir, correlaciones, sesgo)
        return agrupar, describir, correlaciones, sesgo


if __name__ == "__main__":
    df = pd.read_csv("../../data/csv_barcelona.csv")
    exploracion = CSVExploracion(df)
    exploracion.vistazo(show=True)
