from joblib import dump, load
import os
from bienes_inmuebles.dataset.csv_preprocesamiento import PATH4
from bienes_inmuebles.formulario.metodosFormulario import MetodosFormulario

def main():
    modelo = load(os.path.join(PATH4, "data/filename.joblib"))
    print(modelo)

    form = MetodosFormulario()
    objetoPred = form.formulario()

    print(modelo.predict([[objetoPred.getTipoInmueble(),
                         objetoPred.getTipoOperacion(),
                         objetoPred.getHabitaciones(),
                         objetoPred.getTamano(),
                         objetoPred.getPlanta(),
                         objetoPred.getAscensor(),
                         objetoPred.getTerraza(),
                         objetoPred.getTrastero(),
                         objetoPred.getBalcon(),
                         objetoPred.getAireAcondicionado(),
                         objetoPred.getPiscina(),
                         objetoPred.getBanos(),
                         objetoPred.getGaraje_Comunitario(),
                         objetoPred.getGaraje_No_detallado(),
                         objetoPred.getGaraje_Privado(),
                         objetoPred.getDistrito_arganzuela(),
                         objetoPred.getDistrito_barajas(),
                         objetoPred.getDistrito_carabanchel(),
                         objetoPred.getDistrito_centro(),
                         objetoPred.getDistrito_chamartin(),
                         objetoPred.getDistrito_chamberi(),
                         objetoPred.getDistrito_ciudad_lineal(),
                         objetoPred.getDistrito_fuencarral(),
                         objetoPred.getDistrito_hortaleza(),
                         objetoPred.getDistrito_latina(),
                         objetoPred.getDistrito_moncloa(),
                         objetoPred.getDistrito_moratalaz(),
                         objetoPred.getDistrito_puente_de_vallecas(),
                         objetoPred.getDistrito_retiro(),
                         objetoPred.getDistrito_salamanca(),
                         objetoPred.getDistrito_san_blas(),
                         objetoPred.getDistrito_tetuan(),
                         objetoPred.getDistrito_usera(),
                         objetoPred.getDistrito_vicalvaro(),
                         objetoPred.getDistrito_villa_de_vallecas(),
                         objetoPred.getDistrito_villaverde(),
                         objetoPred.getCiudad(),
                         objetoPred.getEficienciaEnergetica_A(),
                         objetoPred.getEficienciaEnergetica_B(),
                         objetoPred.getEficienciaEnergetica_C()]]))


    #print(modelo.predict([[1,1,3,66,5,1,1,0,1,0,0,2,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0]]))
if __name__ == "__main__":
    main()
