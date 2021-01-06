import os
from bienes_inmuebles.dataset.csv_plot import CSVPlot
from pathlib import Path
import numpy
import numpy as np

import pandas as pd
from pandas import set_option
from pandas.plotting import scatter_matrix

from matplotlib import pyplot

from sklearn.preprocessing import StandardScaler

from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.pipeline import Pipeline

from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import VotingClassifier

from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score

from pickle import dump
from pickle import load

from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold

import warnings

class Supervisado(CSVPlot):

    def __init__(self, csv, size=0.33,seed=42,num_folds=10, scoring = 'accuracy'):
        self.csv = csv
        self.df = pd.read_csv(self.csv)
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

    def pipeline_clasificacion(self):
        # Usaremos 6 tipos:
        models = []
        models.append(('LR', LogisticRegression(solver='lbfgs', random_state=self.seed)))
        models.append(('LDA', LinearDiscriminantAnalysis()))
        models.append(('KNN', KNeighborsClassifier()))
        models.append(('CART', DecisionTreeClassifier(random_state=self.seed)))
        models.append(('NB', GaussianNB()))
        models.append(('SVM', SVC(gamma='scale', random_state=self.seed)))
        return models

    def pipeline_evaluacion(self,models, X_train, Y_train):
        # Evaluamos cada modelo por turnos
        results = []
        names = []
        for name, model in models:
            kfold = KFold(n_splits=self.num_folds, random_state=self.seed)
            cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring=self.scoring)
            results.append(cv_results)
            names.append(name)
            print(f"{name}: {round(cv_results.mean(),2)} ({round(cv_results.std(),2)})")
        return results, names

    def comparar_plot (self, results, names):
        # Escogemos el más preciso, que en este caso será SVM
        fig = pyplot.figure()
        fig.suptitle('Comparación de Algoritmos')
        ax = fig.add_subplot(111)
        pyplot.boxplot(results)
        ax.set_xticklabels(names)
        pyplot.show()


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    dataset = Supervisado('../../data/18. visitasUsuarios.csv')
    X_train, X_validation, Y_train, Y_validation = dataset.split_out()
    modelos = dataset.pipeline_clasificacion()
    resultado, nombre = dataset.pipeline_evaluacion(modelos, X_train,Y_train)
    dataset.comparar_plot(resultado, nombre)