from joblib import load
import os
import numpy as np
from bienes_inmuebles.preprocesar.csv_preprocesamiento import PATH4
from bienes_inmuebles.formulario.metodosFormulario import MetodosFormulario

def main():


    form = MetodosFormulario()
    objetoPred = form.formulario()

    # se filtra el dataframe para que segun que tipo operacion introduzca el usuario (1: Comprar; 2:Alquilar), se quede solo con los que necesita
    if objetoPred.getTipoOperacion() == 1:
        modelo = load(os.path.join(PATH4, "data/model_compra.joblib"))
        fichero_path = os.path.join(PATH4, "data/scaler_compra.pkl")
        scaler = load(open(fichero_path, 'rb'))

    elif  objetoPred.getTipoOperacion() == 2:
        modelo = load(os.path.join(PATH4, "data/model_alquiler.joblib"))
        fichero_path = os.path.join(PATH4, "data/scaler_alquiler.pkl")
        scaler = load(open(fichero_path, 'rb'))

    datos = []
    # rea


    #predecir=np.array([1, 1, 1, 69, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1]) #comprar
    predecir = np.array([1,
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
                         objetoPred.getEficienciaEnergetica_C()])
    #print(predecir)

    escalado=scaler.transform(predecir.reshape(1,-1))
    print(escalado)
    resultado_final= modelo.predict(escalado)[0] # Get out of the array
    print(round(resultado_final,2))

    print("aqui acabaaaaaaaaa --------------------------------------")
    """Comprobacion con los mismos datos del train"""
    predecir_comprobacion = np.array([ 0,0,-1.27043022, -0.03037415, -0.80451695,  0.73192505,
 -0.74086779, -0.61304591, -0.3902251,  -0.97053361 -0.41926275 -0.78156767
 -0.26599058,  0.59710535, -0.49491904,  7.29246186, -0.31603512, -0.14791395,
 -0.15177699, -0.15430335, -0.75828754, -0.14791395, -0.14261481, -0.1371279,
 -0.14921177, -0.14528654, -0.26118512, -0.14791395, -0.14261481, -0.21622731,
 -0.14261481, -0.14921177, -0.36208628, -0.10219523, -0.14126153, -0.13851844,
  0, -0.11440719, -0.14660564,  0.18749602]) # set de datos del main
    escalado=predecir_comprobacion.reshape(1,-1)
    resultado_final= modelo.predict(escalado)[0] #get out of the array
    print(round(resultado_final,2))



    #print(modelo.predict([[1,1,3,66,5,1,1,0,1,0,0,2,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0]]))
if __name__ == "__main__":
    main()
