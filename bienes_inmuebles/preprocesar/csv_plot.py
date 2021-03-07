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


    def plot_histograma(self, plot_columnas=[], guardar_x_columnas=False):
        if plot_columnas:
            self.df[plot_columnas].hist()
            plt.show()
        if guardar_x_columnas:
            columns = self.df.columns.values
            for column in columns:
                self.df.hist(column=column)
                my_file = f"data/{column}.png"
                plt.savefig(os.path.join(PATH4, my_file))
        else:
            self.df.hist()
            plt.show()

    """Grafico Densidad"""
    def plot_densidad(self, plot_columnas=[], guardar_x_columnas=False):
        if plot_columnas:
            self.df[plot_columnas].plot()
            plt.show()
        if guardar_x_columnas:
            columns = self.df.columns.values
            for column in columns:
                self.df[column].plot()
                my_file = f"data/{column}.png"
                plt.savefig(os.path.join(PATH4, my_file))
        else:
            self.df.plot(subplots=True)
            plt.show()

    """Grafico Box & Whisker"""
    def plot_bigotes(self, plot_columnas=[], guardar_x_columnas=False):
        if plot_columnas:
            self.df[plot_columnas].plot(kind='box', layout=(10, 5), sharex=False, sharey=False)
            plt.show()
        if guardar_x_columnas:
            columns = self.df.columns.values
            for column in columns:
                fig1, ax1 = plt.subplots()
                ax1.set_title(column)
                ax1.boxplot(self.df[column])
                my_file = f"data/{column}.png"
                plt.savefig(os.path.join(PATH4, my_file))
        else:
            self.df.plot(kind='box', subplots=True, layout=(10, 5), sharex=False, sharey=False)
            plt.show()

    """Matriz Correlacion"""
    def plot_correlacion(self, plot_columnas = []):
        if plot_columnas:
            correlaciones = self.df.iloc[:,plot_columnas].corr()
            fig = plt.figure()
            ax = fig.add_subplot(111)
            cax = ax.matshow(correlaciones, vmin=-1, vmax=1)
            fig.colorbar(cax)
            plt.show()
        else:
            correlaciones = self.df.corr()
            fig = plt.figure()
            ax = fig.add_subplot(111)
            cax = ax.matshow(correlaciones, vmin=-1, vmax=1)
            fig.colorbar(cax)
            plt.show()

    """Matriz Dispersion"""
    def plot_dispersion(self, plot_columnas=[]):
        if plot_columnas:
            scatter_matrix(self.df.iloc[:,plot_columnas])
            plt.show()
        else:
            scatter_matrix(self.df)
            plt.show()

    def scatter_2variables(self, var1, var2):
        my_plot = self.df.plot("tamano", "precio", kind="scatter")
        plt.show()

    def plot_scatter(self):
        dfCompra = pd.read_csv("prueba__.csv", sep=',')
        my_plot = dfCompra.plot("tamano", "precio", kind="scatter")
        plt.show()

    """Elimina imagenes generadas en carpeta /data"""
    def borrar_output(self):
        columns = self.df.columns.values
        for column in columns:
            try:
                my_file = f"data/{column}.png"
                os.remove(os.path.join(PATH4, my_file))
            except ValueError and FileNotFoundError:
                pass


if __name__ == "__main__":
    df = pd.read_csv("../data/csv_barcelona.csv")
    # df = pd.DataFrame(np.random.randn(1000, 4), columns=['A', 'B', 'C', 'D'])
    plot = CSVPlot(df)
    plot.plot_bigotes()