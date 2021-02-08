from joblib import dump, load
import os
from bienes_inmuebles.dataset.csv_preprocesamiento import PATH4

def main():
    modelo = load(os.path.join(PATH4, "data/filename.joblib"))
    print(modelo)
if __name__ == "__main__":
    main()
