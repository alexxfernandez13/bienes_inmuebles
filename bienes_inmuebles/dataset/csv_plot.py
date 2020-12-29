import os
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from pathlib import Path

"""CONSTANTES (en mayuscula)"""
path = Path(__file__)  # PATH A LA FILE EN CUALQUIER ORDENADOR
path2 = Path(path.parent)  # Un directorio hacia atras
path3 = Path(path2.parent)
PATH4 = str(Path(path3.parent))

class CSVPlot():
    def __init__(self, df):
        self.df = df

    def show(self, output=False):
        if not output:
            plt.show()
        else:
            columns=self.df.columns.values
            for column in columns:
                try:
                    self.df.hist(column=column)
                    my_file = f"data/{column}.png"
                    plt.savefig(os.path.join(PATH4,my_file))
                except ValueError:
                    pass

    def plot_histograma(self, output=False):
        self.df.hist()
        self.show(output)

    def plot_densidad(self, output=False):
        self.df.plot(subplots=True, layout=(10, 4), sharex = False)  # kind="density" ¿No funciona?
        self.show(output)

    def plot_bigotes(self,output=False):
        self.df.plot(kind='box', subplots=True, layout=(10, 4), sharex=False, sharey=False)
        self.show(output)

    def plot_correlacion(self, output=False):
        correlaciones = self.df.corr()
        fig = plt.figure()
        ax = fig.add_subplot(111)
        cax = ax.matshow(correlaciones, vmin=-1, vmax=1)
        fig.colorbar(cax)
        self.show(output)

    def plot_dispersion(self, output=False):
        scatter_matrix(self.df)
        self.show(output)

    """Opcion a eliminar el plot"""

if __name__ == "__main__":
    df = pd.read_csv("../../data/csv_barcelona.csv")
    plot = CSVPlot(df)
    plot.plot_dispersion()