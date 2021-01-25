import warnings
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from bienes_inmuebles.machine_learning.evaluacion import Evaluation


class Model(Evaluation):

    def __init__(self, clf, X, Y):
        self.clf = clf
        self.X = X
        self.Y = Y
        self.clf_optimizado = None
        self.best_score = None

    ###DED DONDE VIENEN LOS DATOS?? CSV --> PREPROCES --> TrainTestSplitter

    # argumentos posicionales y argunmentos no posicionales
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

    def predict(self, X_test): #error en predict cuando no recibe modelo optimizado
        if self.clf_optimizado:
            pred = self.clf_optimizado.predict(X_test)
            return pred
        else:
            print("Run optimizacion method first")

    @staticmethod
    def añadir_modelos(nuevos_modelos={}):
        modelos = {SVC(): {'kernel': ['rbf'], 'gamma': [1e-3, 1e-4], 'C': [1, 10, 100, 1000]}}
        return modelos
        if nuevos_modelos:
            merge = modelos.copy()  # start with x's keys and values
            merge.update(nuevos_modelos)  # modifies z with y's keys and values & returns None
            return merge



    def modelos_regresion(self):
        pass

if __name__ == "__main__":
    df = pd.read_csv('./18. visitasUsuarios.csv')
    X_columns = df[['PeriodA', 'PeriodB']].values
    Y_columns = df["Equipo"].values
    X_train, X_test, y_train, y_test = train_test_split(X_columns, Y_columns, test_size=0.3, random_state=42)
    modelos_parametros = {KNeighborsClassifier(): {
        'n_neighbors': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                        27, 28, 29, 30]},
                          SVC(): {'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],
                                  'C': [1, 10, 100, 1000]}}
    # modelos_parametros = Model.añadir_modelos(nuevos_modelos)

    for classificador, parametros in modelos_parametros.items():
        modelo = Model(classificador, X_train, y_train)
        model, score = modelo.optimizacion(parametros)  # train -> train/validation -> score
        y_pred = modelo.predict(X_test)  # test -> pred(test) == y_test???
        print(f"-> Modelo: {classificador}\n Validation Score: {score}\n Test score: {accuracy_score(y_test,y_pred)}\n Matriz de confusion:\n{confusion_matrix(y_test,y_pred)}")

# acabar funcion añadir modelos
# corregir error predict = cuando no recibe modelo optimizado


    # escoger 3 mejores modelos
"""
    #Voting 3 mejores
    voting = Voting(clf[0], clf[1], clf[2])
    Modelo(voting)"""

"""
1) Split datos
2) Modelo fittear
3) Modelo predecir (transform)
"""
