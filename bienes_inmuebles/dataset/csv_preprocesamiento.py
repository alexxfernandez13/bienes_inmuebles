from numpy import *
import pandas as pd
from scipy import stats
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import Binarizer
from bienes_inmuebles.dataset.helpers import _inplace


class CSVPreprocesamiento():
    def __init__(self, csv):
        self.csv = csv
        self.df = pd.read_csv(self.csv)

    def duplicados(self, inplace=False):
        df_resultado = self.df.drop_duplicates()
        return _inplace(self,"df", df_resultado, inplace)  # se le puede el csv antes de leerlo o el dataframe df

    def dropna(self, number=10000, axis=1, inplace=False):
        """Elimina filas/registros axis=0 o columnas/atributos si axis=1. El limite de NaN lo marca number"""
        length = self.df.shape[axis - 1]  # -1 ¿porque era esto?
        df_resultado = self.df.dropna(thresh=length - number, axis=axis)
        return _inplace(self,"df", df_resultado, inplace)

    def ints(self, inplace=False):
        df_resultado = self.df.select_dtypes(include=["int64", "float64"])
        return _inplace(self,"df", df_resultado, inplace)

    def mvs(self, columns=None, strategy="mean", inplace=False):
        imp_mean = SimpleImputer(missing_values=np.nan, strategy=strategy)
        aux = imp_mean.fit_transform(self.df)
        try:
            df_resultado = pd.DataFrame(data=aux, columns=self.df.columns)
        except ValueError:
            raise ValueError("Necesitas borrar columnas con NANs y columnas con Strings primero. "
                             "Ejecutar self.dropna() y self.ints() antes de self.mvs()")
        return _inplace(self,"df", df_resultado, inplace)

    def outliers(self, grado=3, inplace=False):  # Eliminar filas con outlier y escoger grado de eliminacion)
        z_scores = stats.zscore(self.df)  # self.df.values ????
        where_are_NaNs = isnan(z_scores)
        z_scores[where_are_NaNs] = 0
        abs_z_scores = np.abs(z_scores)
        filtered_entries = (abs_z_scores < grado).all(axis=1)  # solucion para sustituir NaN x 0 en la lista de listas??
        df_resultado = self.df[filtered_entries]
        return _inplace(self,"df", df_resultado, inplace)

    def reescalar(self, inplace=False):
        scaler = MinMaxScaler(feature_range=(0, 1))
        df_resultado = scaler.fit_transform(self.df)
        return _inplace(self,"df", df_resultado, inplace)

    def estandarizar(self, inplace=False):
        scaler = StandardScaler().fit(self.df)
        df_resultado = scaler.transform(self.df)
        return _inplace(self,"df", df_resultado, inplace)

    def normalizada(self, inplace=False):
        scaler = Normalizer().fit(self.df)
        df_resultado = scaler.transform(self.df)
        return _inplace(self,"df", df_resultado, inplace)

    def binarizar(self, inplace=False):
        binarizer = Binarizer(threshold=0.0).fit(self.df)
        df_resultado = binarizer.transform(self.df)
        return _inplace(self,"df", df_resultado, inplace)


if __name__ == "__main__":
    preprocesamiento = CSVPreprocesamiento("../../data/csv_barcelona.csv")
    prueba = preprocesamiento.dropna()
    print(prueba.df.info())
