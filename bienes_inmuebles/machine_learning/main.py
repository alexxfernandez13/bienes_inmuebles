from joblib import load
import os
import numpy as np
from bienes_inmuebles.preprocesar.csv_preprocesamiento import PATH4
from bienes_inmuebles.formulario.metodosFormulario import MetodosFormulario
from bienes_inmuebles.base_datos.metodosDb import MetodosDb
from bienes_inmuebles.utilidades.urlPath import UrlPath
import csv
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
    resultado_final = float(resultado_final)
    print(round(resultado_final,2))

    # exporta csv con los datos de la prediccion
    csvPrediccion = open(str(UrlPath.getPath(__file__, 2)) + '\data\datos_usuario_prediccion.csv', 'w', newline='')
    salida = csv.writer(csvPrediccion)
    salida.writerow(['tipoInmueble','tipoOperacion','Habitaciones','Tamano','Planta','Ascensor','Terraza','Trastero',
                     'Balcon','AireAcondicionado','Piscina','Banos','Garaje_Comunitario','Garaje_No_detallado','Garaje_Privado',
                     'Distrito_arganzuela','Distrito_barajas','Distrito_carabanche','Distrito_centro','Distrito_chamartin',
                     'Distrito_chamberi','Distrito_ciudad_lineal','Distrito_fuencarral','Distrito_hortaleza','Distrito_latina',
                     'Distrito_moncloa','Distrito_moratalaz','Distrito_puente_de_vallecas','Distrito_retiro','Distrito_salamanca',
                     'Distrito_san_blas','Distrito_tetuan','Distrito_usera','Distrito_vicalvaro','Distrito_villa_de_vallecas',
                     'Distrito_villaverde','Ciudad','EficienciaEnergetica_A','EficienciaEnergetica_B','EficienciaEnergetica_C', 'Prediccion'])
    salida.writerow([1,
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
                         objetoPred.getEficienciaEnergetica_C(),
                            round(resultado_final,2)])
    del salida
    csvPrediccion.close()
    # exporta csv con los datos de la prediccion



    print("aqui acabaaaaaaaaa --------------------------------------")
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
