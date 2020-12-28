# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 20:07:09 2020

@author: xxxxxxxx
"""

from bs4 import BeautifulSoup
import requests
import pymysql
import time
import random
import datetime


def aadd2BBDD(inmueble):
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

    print(sql)

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


def descargarInfo(url):
    # Parametros peticion HTTPS para simular ser un navegador
    # En caso de no añadirlo la web detecta que es un scaneo y bloquea
    headersFakeBrowser = [
        {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Dnt": "1",
            "Host": "www.idealista.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        },
        {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Dnt": "1",
            "Host": "www.idealista.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15",
        },
        {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Dnt": "1",
            "Host": "www.idealista.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
        },
        {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Dnt": "1",
            "Host": "www.idealista.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        },
        {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Dnt": "1",
            "Host": "www.idealista.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0",
        },
        {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Dnt": "1",
            "Host": "www.idealista.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        }
    ]

    # Elegimos datos cabecera al azar
    headers = random.choice(headersFakeBrowser)
    print(headers)

    # Realizamos peticion HTTPS para obtener la informacion del web
    req = requests.get(url, headers=headersFakeBrowser[0])

    # Inicializamos la lista de objetos que se extraeran
    listaInmuebles = []

    # Comprobamos que la petición nos devuelve un Status Code = 200
    status_code = req.status_code
    if status_code == 200:

        # Pasamos el contenido HTML de la web a un objeto BeautifulSoup() para su analisis
        html = BeautifulSoup(req.text, "html.parser")
        print("Recibido Codigo 200. Comenzando analisis")

        # Analizo contenido de la web para sacar la informacion
        enlaces = html.find_all('div', class_="item-info-container")
        for enlace in enlaces:

            idInmueble = None
            numHab = None
            tamano = None
            planta = None

            # Obtenermos la referencia del inmueble
            idInmueble = enlace.findChildren('a', attrs={'class': 'item-link'})[0].get('href')
            idInmueble = int(idInmueble.split("/")[2])

            # Obtenermos el precio del inmueble
            precio = enlace.findChildren('span', attrs={'class': 'item-price h2-simulated'})[0].get_text()
            # Formateamos de string a float
            precio = precio.replace(".", "")
            precio = precio.replace("€", "")

            # Obtenemos las caracteristicas del inmueble
            caracteristicas = enlace.findChildren('span', attrs={'class': 'item-detail'})

            for caracteristica in caracteristicas:
                texto = caracteristica.get_text()
                if (texto.find("hab.") > -1):
                    # Obtenermos el numero de habitaciones
                    numHab = texto.replace(" hab.", "")
                    numHab = int(numHab)
                elif (texto.find("m²") > -1):
                    # Obtenemos el tamaño del inmueble
                    tamano = texto.replace(" m²", "")
                    tamano = tamano.replace(".", "")
                    tamano = int(tamano)
                else:
                    planta = texto

            if (url.find("viviendas")):
                tipoInmueble = 1
            elif (url.find("locales")):
                tipoInmueble = 2
            else:
                tipoInmueble = None

            tipoOperacion = 1
            poblacion = "TEST"
            ciudad = "barcelona"
            fuenteInfo = "idealista"

            fecha = datetime.datetime.now()
            fecha = str(fecha.year) + "-" + str(fecha.month) + "-" + str(fecha.day)

            objetoInmueble = [idInmueble, fuenteInfo, tipoInmueble, tipoOperacion, precio, numHab, tamano, planta,
                              poblacion, ciudad, fecha]
            listaInmuebles.append(objetoInmueble)
    else:
        print("Status Code %d" % status_code)

    return (listaInmuebles)


###### Aplicacion principal

fichero = open("venta.txt", "r")

for url in fichero:
    print("Accediendo a: " + url)

    for pagina in range(1, 60):
        print("Durmiendo 10 seg.")
        time.sleep(10)
        url_pagina = url + "/pagina-" + str(pagina) + ".htm"
        print(url_pagina)
        objetos = descargarInfo(url_pagina)
        while (len(objetos) < 1):
            print("Dormir otros 10 seg y reintentar")
            time.sleep(10)

        for inmueble in objetos:
            print(inmueble)
            aadd2BBDD(inmueble)

fichero.close()