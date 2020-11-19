from bienes_inmuebles.dataset.csv_utilities import CSV


def _inplace(objeto, atributo, valor_atributo, inplace=False):  # funcion para sobrescribir ojbetos o realizar copias
    if inplace:
        setattr(atributo, valor_atributo)
    else:
        nuevo_objeto = CSV(objeto.csv)
        setattr(nuevo_objeto, atributo, valor_atributo)
        # self.atributo = valor_atributo
        # self.df = resultado_df
        return nuevo_objeto