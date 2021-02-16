from joblib import load
import os
import numpy as np
from bienes_inmuebles.preprocesar.csv_preprocesamiento import PATH4
from bienes_inmuebles.formulario.metodosFormulario import MetodosFormulario

def main():
    modelo = load(os.path.join(PATH4, "data/filename.joblib"))

    #form = MetodosFormulario()
    #objetoPred = form.formulario()


    datos = []
    # rea
    fichero_path = os.path.join(PATH4, "data/scaler.pkl")
    scaler = load(open(fichero_path, 'rb'))
    predecir=np.array([1, 1, 1, 69, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1])
    """predecir = np.array([1,
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
                         objetoPred.getEficienciaEnergetica_C()])"""
    #print(predecir)

    escalado=scaler.transform(predecir.reshape(1,-1))
    print(escalado)
    resultado_final= modelo.predict(escalado)[0] # Get out of the array
    print(round(resultado_final,2))
    """Comprobacion con los mismos datos del train"""
    predecir_comprobacion = np.array([0, - 1.95449518, - 0.75529407,  0.01537159, - 0.9277343, - 1.4858903,
                             - 0.41280987, - 0.31011403, - 0.50665808, - 1.31425748, - 0.18103409, - 0.64527728,
                             0,          0.2638086, - 0.2638086,   0,          0,          0,
                             0.90672898,  0, - 0.90672898,  0,          0,          0,
                             0,          0,          0,          0,          0,          0,
                             0,          0,          0,          0,          0,          0,
                             0,          0,          0,          0]) # set de datos del main
    escalado=predecir_comprobacion.reshape(1,-1)
    resultado_final= modelo.predict(escalado)[0] #get out of the array
    print(round(resultado_final,2))
    """print(modelo.predict([[objetoPred.getTipoInmueble(),
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
                         objetoPred.getEficienciaEnergetica_C()]]))"""


    #print(modelo.predict([[1,1,3,66,5,1,1,0,1,0,0,2,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0]]))
if __name__ == "__main__":
    main()
