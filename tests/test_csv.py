import os
from bienes_inmuebles.dataset.csv_utilities import CSV, PATH4


def test_cvs_to_dataframe():
    objeto_csv = CSV(os.path.join(PATH4, "data/csv_barcelona.csv"))
    assert objeto_csv.df.columns[1] == "listing_url"