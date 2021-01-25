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
from bienes_inmuebles.machine_learning.modelos import Modelo
from sklearn.model_selection import cross_val_score

class Supervisado():

    def __init__(self, clf, X, Y):
        self.clf = clf
        self.X = X
        self.Y = Y
        self.clf_optimizado = None
        self.best_score = None

    ###DED DONDE VIENEN LOS DATOS?? CSV --> PREPROCES --> TrainTestSplitter

    # argumentos posicionales y argunmentos no posicionales
    def optimizacion(self, clave, parametros, cv=10, scoring='f1_weighted'):

        if self.X.tolist() and self.Y.tolist() and parametros:

            grid = GridSearchCV(self.clf, parametros, scoring=scoring, cv=cv)
            grid.fit(self.X, self.Y)
            self.clf_optimizado = grid.best_estimator_
            self.best_score = grid.best_score_
            return self.clf_optimizado, self.best_score
        else:
            print("No ha corrido la optimizacion")
            self.clf = cross_val_score(clave, self.X, self.Y, cv=cv, scoring=scoring)
            return self.clf, self.clf.mean()

    def predict(self, X_test): #error en predict cuando no recibe modelo optimizado
        if self.clf_optimizado:
            pred = self.clf_optimizado.predict(X_test)
            return pred
        else:
            print("Run optimizacion method first")
            pred = self.clf.predict(X_test)
            return pred


if __name__ == "__main__":
    df = pd.read_csv('./18. visitasUsuarios.csv')
    X_columns = df[['PeriodA', 'PeriodB']].values
    Y_columns = df["Equipo"].values
    X_train, X_test, y_train, y_test = train_test_split(X_columns, Y_columns, test_size=0.3, random_state=42)

    obj_eva = Modelo()

    for classificador, parametros in obj_eva.modelos_clasificacion().items():
        modelo = Supervisado(classificador, X_train, y_train)
        model, score = modelo.optimizacion(classificador, parametros)  # train -> train/validation -> score
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