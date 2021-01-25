from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

class Modelo():


    def modelos_clasificacion(self):
        modelos_parametros = {KNeighborsClassifier(): {
            'n_neighbors': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                            26,
                            27, 28, 29, 30]},
            SVC(): {'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],
                    'C': [1, 10, 100, 1000]},
            LogisticRegression():None}
        return modelos_parametros