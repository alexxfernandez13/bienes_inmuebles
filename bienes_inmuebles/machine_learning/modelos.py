import warnings
import pandas as pd
from sklearn.model_selection import train_test_split


class Model():

    def __init__(self, clf):
        self.clf = clf
        self.X = None
        self.Y = None
        self.clf_optimizado = None

    ###DED DONDE VIENEN LOS DATOS?? CSV --> PREPROCES --> TrainTestSplitter
    def inicializar(self, X, Y):
        self.X = X
        self.Y = Y

    def optimizacion(self, parametros):
        if self.X and self.Y:
            parametros = parametros
            grid = GridSearch()
            grid.fit(self.clf, self.X, self.Y)
            self.clf_optimizado = grid._best_parameters
            return self.clf.optimizado
        else:
            print("Run method fit first")

    def predict(self, X):
        if self.clf_optimizado:
            pred = self.clf_optimizado.predict(X)
            return pred
        else:
            print("Run optimizacion method first")


if __name__ == "__main__":
    df = preprocesamiento()
    X_train, y_train, X_test, y_test = TrainTestSplit.split_out(df, siz=0.3, score="accuracy")
    for modelo in []:
        modelo = Model(KNeighbours())
        molo.fit(X_train, y_train)
        modelo.optimizacion(parametro_kneighbours)
        modelo.predict(X_test)

"""
1) Split datos
2) Modelo fittear
3) Modelo predecir (transform)
"""



class Models():


    def __init__(self, df, size = 0.33, seed= 42, num_folds = 10 , scoring ="accuracy"):
        self.df = df
        self.array = self.df.values
        self.X = self.array[:, 0:2]
        self.Y = self.array[:, 2]
        self.validation_size = size  # Muestras pequeñas = 0.33 ; Muestras grandes = 0.20
        self.seed = seed  # Dato por convencion
        self.num_folds = num_folds  # Usar el valor más alto que permita la muestra
        self.scoring = scoring

    def split_out(self):
        X_train, X_validation, Y_train, Y_validation = train_test_split(self.X, self.Y, test_size=self.validation_size,
                                                                        random_state=self.seed)
        return X_train, X_validation, Y_train, Y_validation

    def modelos_simples(self):



if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    dataset = '../../data/18. visitasUsuarios.csv'
    df = pd.read_csv(dataset)
    modelo = Models(df)

