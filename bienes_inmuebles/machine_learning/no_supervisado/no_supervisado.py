from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

from bienes_inmuebles.dataset.csv_plot import CSVPlot

class NO_Supervisado(CSVPlot):
    def __init__(self, df):
        self.df = df

    def pca(self, n=2):
        pca = PCA(n_components=n)
        pca.fit(self.df)
        return pca.transform(self.df)

    def tsne(self,n=2):
        X_embedded = TSNE(n_components=n).fit_transform(self.df)
        return X_embedded

    def unam(self):
        pass

if __name__ == "__main__":
    no_supervisado = NO_Supervisado("../../data/csv_barcelona.csv")

