import warnings
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from bienes_inmuebles.machine_learning.evaluacion import Evaluation

class Model(Evaluation):

    def __init__(self, clf, X, Y):
        self.clf = clf
        self.X = X
        self.Y = Y
        self.clf_optimizado = None
        self.best_score= None

    ###DED DONDE VIENEN LOS DATOS?? CSV --> PREPROCES --> TrainTestSplitter

    #argumentos posicionales y argunmentos no posicionales
    def optimizacion(self, parametros, cv=10, scoring='f1_weighted'):

        if self.X.tolist() and self.Y.tolist() and parametros:

            grid = GridSearchCV(self.clf, parametros, scoring=scoring, cv=cv)
            grid.fit(self.X, self.Y)
            self.clf_optimizado = grid.best_estimator_
            self.best_score = grid.best_score_
            return self.clf_optimizado, self.best_score
        else:
            print("No ha corrido la optimizacion")
            return self.clf, ""

    def predict(self, X_test):
        if self.clf_optimizado:
            pred = self.clf_optimizado.predict(X_test)
            return pred
        else:
            print("Run optimizacion method first")


if __name__ == "__main__":
    df = pd.read_csv('./18. visitasUsuarios.csv')
    X_columns = df[['PeriodA', 'PeriodB']].values
    Y_columns = df["Equipo"].values
    X_train, X_test, y_train, y_test = train_test_split(X_columns, Y_columns, test_size=0.3, random_state=42)

    modelos_parametros = {KNeighborsClassifier(): {'n_neighbors': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]},
                          SVC(): {'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],
                         'C': [1, 10, 100, 1000]}}

    for classificador, parametros in modelos_parametros.items():
        modelo = Model(classificador, X_train, y_train)
        model, score =modelo.optimizacion(parametros) #train -> train/validation -> score
        y_pred = modelo.predict(X_test) #test -> pred(test) == y_test???
        print("Validation score", score) # scoring con los datos entrenados
        print("Test score", accuracy_score(y_test, y_pred))
        print("Test score", confusion_matrix(y_test, y_pred)) # scoring en situacion real

    #escoger 3 mejores modelos
"""
    #Voting 3 mejores
    voting = Voting(clf[0], clf[1], clf[2])
    Modelo(voting)"""

"""
1) Split datos
2) Modelo fittear
3) Modelo predecir (transform)
"""

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
"""
