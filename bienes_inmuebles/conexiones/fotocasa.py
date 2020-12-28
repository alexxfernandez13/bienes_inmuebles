from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pymysql
import datetime
from bienes_inmuebles.conexiones.mysql import MYsql

def saveLog(text):
        fp = open("logScriptScraper.log", 'a')
        fp.writelines(text)

def add2BBDD(inmueble):
    instancia = MYsql()
    bbdd_server, bbdd_user, bbdd_pass, bbdd_name = instancia.intancias_bbdd()

    # Establecemos conexion con la BBDD
    db = pymysql.connect(bbdd_server, bbdd_user, bbdd_pass, bbdd_name)

    # Prepando el objeto de manipulacion de BBDD
    cursor = db.cursor()

    # Comprabacion datos facilitados
    for elemento in inmueble:
        if (elemento == None):
            elemento = ""

            # Añadimos elemento a la BBDD
    sql = "INSERT INTO Pisos VALUES (" + str(inmueble[0]) + "," + "'" + str(inmueble[1]) + "'" + "," + str(
        inmueble[2]) + "," + str(inmueble[3]) + "," + str(inmueble[4]) + "," + str(inmueble[5]) + "," + str(
        inmueble[6]) + "," + "'" + str(inmueble[7]) + "'" + "," + "'" + str(inmueble[8]) + "'" + "," + "'" + str(
        inmueble[9]) + "'" + "," + "'" + str(inmueble[10]) + "'" + ")"
    #   print(sql)

    try:
        # Ejecutamos comando SQL
        cursor.execute(sql)
        # COMMIT - Aplicar de forma persistente en la BBDD
        db.commit()
        print("Objeto Añadido")
    except:
        # Rollback en caso de error
        db.rollback()
        print("Error al añadir en BBDD")

    # Desconexion del servidor
    db.close()


def getDistrito(url):
    return (url.split("/")[7])


def getTipoOperacion(url):
    if (url.find("comprar")):
        operationType = 1
    elif (url.find("alquilar")):
        operationType = 2
    else:
        operationType = 0

    return (operationType)


def getTipoInmueble(url):
    if (url.find("viviendas")):
        tipoInmueble = 1
    elif (url.find("locales")):
        tipoInmueble = 2
    else:
        tipoInmueble = 0

    return (tipoInmueble)


def getPoblacion(url):
    x = url.split("/")
    return (x[-2])


def descargarInfo(url):
    # browser = webdriver.Firefox()
    browser = webdriver.Chrome()
    browser.get((url))
    time.sleep(5)

    for i in range(25):
        html_txt = browser.page_source
        soup = BeautifulSoup(html_txt)
        listaInmuebles = []

        productos = soup.find_all('div', class_="re-Card-secondary")
        for producto in productos:
            idInmueble = None
            numHab = 0
            tamano = 0
            planta = None

            # Obtenermos la referencia del inmueble
            idInmueble = producto.findChildren('a', attrs={'class': 're-Card-link'})[0].get('href')
            idInmueble = idInmueble.split("/")
            if (len(idInmueble) > 6):
                if (idInmueble[6].isnumeric()):
                    idInmueble = int(idInmueble[6])
                    #                    print(idInmueble)

                    # Obtenermos el precio del inmueble
                    precio = producto.findChildren('span', attrs={'class': 're-Card-price'})[0].get_text()
                    # Formateamos de string a float
                    precio = precio.replace(".", "")
                    precio = precio.replace("/mes", "")
                    precio = precio.replace("€", "")

                    # Obtenemos las caracteristicas del inmueble
                    caracteristicas = producto.findChildren('span', attrs={'class': 're-CardFeatures-feature'})
                    #                    print ("CARACTERISTICAS")

                    for caracteristica in caracteristicas:
                        texto = caracteristica.get_text()
                        #                        print(texto)
                        if (texto.find("habs.") > -1):
                            # Obtenermos el numero de habitaciones
                            numHab = texto.replace(" habs.", "")
                            numHab = int(numHab)
                        elif (texto.find("m²") > -1):
                            # Obtenemos el tamaño del inmueble
                            tamano = texto.replace(" m²", "")
                            tamano = tamano.replace(".", "")
                            tamano = int(tamano)

                        fuenteInfo = "fotocasa"
                        tipoInmueble = getTipoInmueble(url)
                        tipoOperacion = getTipoOperacion(url)

                        distrito = getDistrito(url)
                        ciudad = "Madrid"

                        fecha = datetime.datetime.now()
                        fecha = str(fecha.year) + "-" + str(fecha.month) + "-" + str(fecha.day)

                    objetoInmueble = [idInmueble, fuenteInfo, tipoInmueble, tipoOperacion, precio, numHab, tamano,
                                      planta, distrito, ciudad, fecha]
                    listaInmuebles.append(objetoInmueble)
                    print("Añadido inmueble")

        print(i)
        ActionChains(browser).send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(0.5)

    browser.quit()

    return (listaInmuebles)


###### APLICACION PRINCIPAL ########

if __name__ == "__main__":

    direcciones = [
        #    "https://www.fotocasa.es/es/comprar/viviendas/madrid-capital/arganzuela/l?combinedLocationIds=724%2C14%2C28%2C173%2C0%2C28079%2C0%2C671%2C0&gridType=3&latitude=40.4096&longitude=-3.68624",
        #    "https://www.fotocasa.es/es/comprar/viviendas/madrid-capital/barajas/l?latitude=40.40099999447889&longitude=-3.7040766977717645&combinedLocationIds=724,14,28,173,0,28079,0,668,0&gridType=3",
        #    "https://www.fotocasa.es/es/comprar/viviendas/madrid-capital/carabanchel/l?latitude=40.468037022265854&longitude=-3.582424716280453&combinedLocationIds=724,14,28,173,0,28079,0,171,0&gridType=3",
        #    "https://www.fotocasa.es/es/comprar/viviendas/madrid-capital/centro/l?latitude=40.37959392136568&longitude=-3.739877001407099&combinedLocationIds=724,14,28,173,0,28079,0,672,0&gridType=3",
        #    "https://www.fotocasa.es/es/comprar/viviendas/madrid-capital/chamartin/l?latitude=40.416861199611624&longitude=-3.7028325693424122&combinedLocationIds=724,14,28,173,0,28079,0,176,0&gridType=3",
        #    "https://www.fotocasa.es/es/comprar/viviendas/madrid-capital/chamberi/l?latitude=40.4553103039952&longitude=-3.6790275377675594&combinedLocationIds=724,14,28,173,0,28079,0,177,0&gridType=3",
        #    "https://www.fotocasa.es/es/comprar/viviendas/madrid-capital/ciudad-lineal/l?latitude=40.438617543919925&longitude=-3.7023556174435788&combinedLocationIds=724,14,28,173,0,28079,0,685,0&gridType=3",
        #    "https://www.fotocasa.es/es/comprar/viviendas/madrid-capital/fuencarral/l?latitude=40.4441705854059&longitude=-3.6525802484224394&combinedLocationIds=724,14,28,173,0,28079,0,187,0&gridType=3",
        #    "https://www.fotocasa.es/es/comprar/viviendas/madrid-capital/hortaleza/l?latitude=40.49446606429687&longitude=-3.7136771420672146&combinedLocationIds=724,14,28,173,0,28079,0,678,0&gridType=3",
        #    "https://www.fotocasa.es/es/comprar/viviendas/madrid-capital/latina/l?latitude=40.46881501855609&longitude=-3.641945499708502&combinedLocationIds=724,14,28,173,0,28079,0,675,0&gridType=3",
        #    "https://www.fotocasa.es/es/comprar/viviendas/madrid-capital/moncloa/l?latitude=40.39225632660759&longitude=-3.7579024169335757&combinedLocationIds=724,14,28,173,0,28079,0,669,0&gridType=3",
        #    "https://www.fotocasa.es/es/comprar/viviendas/madrid-capital/moratalaz/l?latitude=40.449174073700895&longitude=-3.7395741953059853&combinedLocationIds=724,14,28,173,0,28079,0,191,0&gridType=3",
        #    "https://www.fotocasa.es/es/comprar/viviendas/madrid-capital/puente-de-vallecas/l?latitude=40.407259583898416&longitude=-3.6443908162015353&combinedLocationIds=724,14,28,173,0,28079,0,677,0&gridType=3",
        #    "https://www.fotocasa.es/es/comprar/viviendas/madrid-capital/retiro/l?latitude=40.39272222236246&longitude=-3.659177255581731&combinedLocationIds=724,14,28,173,0,28079,0,199,0&gridType=3",
        #    "https://www.fotocasa.es/es/comprar/viviendas/madrid-capital/salamanca/l?latitude=40.411591900855164&longitude=-3.67337318656686&combinedLocationIds=724,14,28,173,0,28079,0,667,0&gridType=3",
        #    "https://www.fotocasa.es/es/comprar/viviendas/madrid-capital/san-blas/l?latitude=40.428670212130825&longitude=-3.676313801748082&combinedLocationIds=724,14,28,173,0,28079,0,676,0&gridType=3",
        #    "https://www.fotocasa.es/es/comprar/viviendas/madrid-capital/tetuan/l?latitude=40.43455248864532&longitude=-3.6117328944176728&combinedLocationIds=724,14,28,173,0,28079,0,681,0&gridType=3",
        #    "https://www.fotocasa.es/es/comprar/viviendas/madrid-capital/usera/l?latitude=40.459750181899&longitude=-3.698760133898529&combinedLocationIds=724,14,28,173,0,28079,0,205,0&gridType=3",
        #    "https://www.fotocasa.es/es/comprar/viviendas/madrid-capital/vicalvaro/l?latitude=40.379623008087385&longitude=-3.704375194087928&combinedLocationIds=724,14,28,173,0,28079,0,209,0&gridType=3",
        #    "https://www.fotocasa.es/es/comprar/viviendas/madrid-capital/villa-de-vallecas/l?latitude=40.401199408868656&longitude=-3.606278537506303&combinedLocationIds=724,14,28,173,0,28079,0,680,0&gridType=3",
        #    "https://www.fotocasa.es/es/comprar/viviendas/madrid-capital/villaverde/l?latitude=40.36808128794791&longitude=-3.6216737278917877&combinedLocationIds=724,14,28,173,0,28079,0,670,0&gridType=3",
        #    "https://www.fotocasa.es/es/comprar/viviendas/madrid-capital/vicalvaro/l?latitude=40.379623008087385&longitude=-3.704375194087928&combinedLocationIds=724,14,28,173,0,28079,0,209,0&gridType=3",
        "https://www.fotocasa.es/es/alquiler/viviendas/madrid-capital/arganzuela/l?combinedLocationIds=724%2C14%2C28%2C173%2C0%2C28079%2C0%2C671%2C0&gridType=3&latitude=40.4096&longitude=-3.68624",
        "https://www.fotocasa.es/es/alquiler/viviendas/madrid-capital/barajas/l?latitude=40.40099999447889&longitude=-3.7040766977717645&combinedLocationIds=724,14,28,173,0,28079,0,668,0&gridType=3",
        "https://www.fotocasa.es/es/alquiler/viviendas/madrid-capital/carabanchel/l?latitude=40.468037022265854&longitude=-3.582424716280453&combinedLocationIds=724,14,28,173,0,28079,0,171,0&gridType=3",
        "https://www.fotocasa.es/es/alquiler/viviendas/madrid-capital/centro/l?latitude=40.37959392136568&longitude=-3.739877001407099&combinedLocationIds=724,14,28,173,0,28079,0,672,0&gridType=3",
        "https://www.fotocasa.es/es/alquiler/viviendas/madrid-capital/chamartin/l?latitude=40.416861199611624&longitude=-3.7028325693424122&combinedLocationIds=724,14,28,173,0,28079,0,176,0&gridType=3",
        "https://www.fotocasa.es/es/alquiler/viviendas/madrid-capital/chamberi/l?latitude=40.4553103039952&longitude=-3.6790275377675594&combinedLocationIds=724,14,28,173,0,28079,0,177,0&gridType=3",
        "https://www.fotocasa.es/es/alquiler/viviendas/madrid-capital/ciudad-lineal/l?latitude=40.438617543919925&longitude=-3.7023556174435788&combinedLocationIds=724,14,28,173,0,28079,0,685,0&gridType=3",
        "https://www.fotocasa.es/es/alquiler/viviendas/madrid-capital/fuencarral/l?latitude=40.4441705854059&longitude=-3.6525802484224394&combinedLocationIds=724,14,28,173,0,28079,0,187,0&gridType=3",
        "https://www.fotocasa.es/es/alquiler/viviendas/madrid-capital/hortaleza/l?latitude=40.49446606429687&longitude=-3.7136771420672146&combinedLocationIds=724,14,28,173,0,28079,0,678,0&gridType=3",
        "https://www.fotocasa.es/es/alquiler/viviendas/madrid-capital/latina/l?latitude=40.46881501855609&longitude=-3.641945499708502&combinedLocationIds=724,14,28,173,0,28079,0,675,0&gridType=3",
        "https://www.fotocasa.es/es/alquiler/viviendas/madrid-capital/moncloa/l?latitude=40.39225632660759&longitude=-3.7579024169335757&combinedLocationIds=724,14,28,173,0,28079,0,669,0&gridType=3",
        "https://www.fotocasa.es/es/alquiler/viviendas/madrid-capital/moratalaz/l?latitude=40.449174073700895&longitude=-3.7395741953059853&combinedLocationIds=724,14,28,173,0,28079,0,191,0&gridType=3",
        "https://www.fotocasa.es/es/alquiler/viviendas/madrid-capital/puente-de-vallecas/l?latitude=40.407259583898416&longitude=-3.6443908162015353&combinedLocationIds=724,14,28,173,0,28079,0,677,0&gridType=3",
        "https://www.fotocasa.es/es/alquiler/viviendas/madrid-capital/retiro/l?latitude=40.39272222236246&longitude=-3.659177255581731&combinedLocationIds=724,14,28,173,0,28079,0,199,0&gridType=3",
        "https://www.fotocasa.es/es/alquiler/viviendas/madrid-capital/salamanca/l?latitude=40.411591900855164&longitude=-3.67337318656686&combinedLocationIds=724,14,28,173,0,28079,0,667,0&gridType=3",
        "https://www.fotocasa.es/es/alquiler/viviendas/madrid-capital/san-blas/l?latitude=40.428670212130825&longitude=-3.676313801748082&combinedLocationIds=724,14,28,173,0,28079,0,676,0&gridType=3",
        "https://www.fotocasa.es/es/alquiler/viviendas/madrid-capital/tetuan/l?latitude=40.43455248864532&longitude=-3.6117328944176728&combinedLocationIds=724,14,28,173,0,28079,0,681,0&gridType=3",
        "https://www.fotocasa.es/es/alquiler/viviendas/madrid-capital/usera/l?latitude=40.459750181899&longitude=-3.698760133898529&combinedLocationIds=724,14,28,173,0,28079,0,205,0&gridType=3",
        "https://www.fotocasa.es/es/alquiler/viviendas/madrid-capital/vicalvaro/l?latitude=40.379623008087385&longitude=-3.704375194087928&combinedLocationIds=724,14,28,173,0,28079,0,209,0&gridType=3",
        "https://www.fotocasa.es/es/alquiler/viviendas/madrid-capital/villaverde/l?latitude=40.3472523466546&longitude=-3.6934487165321173&combinedLocationIds=724,14,28,173,0,28079,0,670,0&gridType=3",
        "https://www.fotocasa.es/es/alquiler/viviendas/madrid-capital/vicalvaro/l?latitude=40.379623008087385&longitude=-3.704375194087928&combinedLocationIds=724,14,28,173,0,28079,0,209,0&gridType=3",
        "https://www.fotocasa.es/es/alquiler/viviendas/madrid-capital/villa-de-vallecas/l?latitude=40.401199408868656&longitude=-3.606278537506303&combinedLocationIds=724,14,28,173,0,28079,0,680,0&gridType=3"
    ]

    for url in direcciones:
        for pagina in range(1, 100):
            pestana = "/l/" + str(pagina) + "/?"
            urlConsulta = url.replace("/l?", pestana)
            print(urlConsulta)

            objetos = descargarInfo(urlConsulta)

            #for inmueble in objetos:
                #add2BBDD(inmueble)
            print(objetos)
            if (len(objetos) < 30):
                break

            time.sleep(20)
