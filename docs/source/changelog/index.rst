ChangeLog
==========

v1.0.0
++++++++

PROGRAMA SUPERIOR EN BIG DATA
Edición septiembre 2020



REAL ESTATE PREDICTION







Alejandro Fernández Esteban
José Pablo Guerra Simancas
Ana Catarina Silva Matos
Francisco Jesús León Carrasco
CONTENIDO
IMAGENENES	3
TABLAS	6
1.- INTRODUCCIÓN	7
2.- COMPRENSIÓN DEL NEGOCIO	8
3.- ARQUITECTURA Y TECNOLOGÍAS UTILIZADAS	10
3.1.- ARQUITECTURA	10
3.1.1.- CAPA DE ALMACENAMIENTO	10
3.1.2.- CAPA DE PROCESAMIENTO	11
3.1.3.- CAPA DE INPUTS	11
3.1.4.- CAPA DE VISUALIZACIÓN	12
3.2.- TECNOLOGIAS	13
3.2.1.- PYTHON 3.8	13
3.2.2.-  BBDD MYSQL 8.0.22	14
3.2.3.- GITHUG	14
3.2.4.- DOCKER	14
3.2.5.- POWER BI	16
3.2.6.- PYCHARM COMUNITY EDITION 2020.2.1 64X	16
3.2.7.- GITHUB DESKTOP	16
3.2.8.-  TRELLO	17
3.2.9.-   ONEDRIVE	17
4.- COMPRENSIÓN DE LOS DATOS	18
4.1.- RECOLECTAR DATOS	18
4.2.- DESCRIBIR DATOS	24
4.3.- EXPLORACIÓN Y VERIFICACIÓN DE LOS DATOS	26
4.4.- OUTLIERS	34
5.-  PREPARACIÓN DE LOS DATOS	37
5.1.- ESTRUCTURAR LOS DATOS	37
5.2.- INTEGRAR LOS DATOS	41
5.3.- INFORMACIÓN DE LOS DATOS	42
5.4.- ANÁLISIS DE DATOS CON ESTADÍSTICA DESCRIPTIVA Y VISUALIZACIÓN	52
6.- MODELADO	57
6.1.- SELECCIONAR TÉCNICA DE MODELADO	59
6.2.- GENERAR PLAN DE PRUEBAS (CONJUNTOS DE ENTRENAMIENTO Y TEST)	59
6.3.- CONSTRUIR MODELO	60
6.4.- EVALUAR EL MODELO (COMPARACIÓN DE MODELOS)	62
6.5.- GUARDADO DEL MODELO.	64
7.- VISUALIZACIONES CON POWER BI	65
8.- CONCLUSIONES DEL MODELO PREDICTIVO	67
9.- TRABAJOS FUTUROS	71
ANEXO I: INSTALACIÓN, CONFIGURACIÓN Y VERIFICACIÓN DE DOCKER	72
ANEXO II: FUENTES DE INFORMACIÓN ANALIZADAS	76
ANEXO III: SCRIPT CREACIÓN BASE DE DATOS MYSQL	78


IMAGENENES
IMAGEN 1 DIAGRAMA METODOLOGÍA CRISP-DM	7
IMAGEN 2 FLUJO DE ALMACENAMIENTO	10
IMAGEN 3 FLUJO DE PROCESAMIENTO	11
IMAGEN 4 FLUJO DE ALMACENAMIENTO	11
IMAGEN 5 FLUJO DE VISUALIZACIÓN	12
IMAGEN 6 ICONO LENGUAJE PYTHON	13
IMAGEN 7 ICONO MYSQL Y WORKBENCH	14
IMAGEN 8 ESTRUCTURA MÁQUINA VIRTUAL VS VIRTUALIZACIÓN MEDIANTE CONTENEDORES	15
IMAGEN 9 ICONO POWER BI	16
IMAGEN 10 ICONO HERRAMIENTA PYCHARM	16
IMAGEN 11 ICONO GITHUB	16
IMAGEN 12 ICONO PLATAFORMA TRELLO (HTTPS://TRELLO.COM/)	17
IMAGEN 13 ICONO PLATAFORMA ONEDRIVE	17
IMAGEN 14 PORTAL IDEALISTA.COM	19
IMAGEN 15 WEB DE DESARROLLO DE IDEALISTA.COM	19
IMAGEN 16 PROCESO DE EXTRACCIÓN Y ESTRUCTURACIÓN DE DATOS DE UN SITE	20
IMAGEN 17 TÉRMINOS Y CONDICIONES IDEALISTA.COM	20
IMAGEN 18 MÓDULO DE EXTRACCIÓN DE INFORMACIÓN DE FOTOCASA.	22
IMAGEN 19 DIRECTORIO DEL MÓDULO DE EXTRACCIÓN DE INFORMACIÓN DE FOTOCASA, DONDE VAMOS A UBICAR EL CSV QUE UTILIZAREMOS PARA GENERAR EL MODELO DE PREDICCIÓN	23
IMAGEN 20 CÓDIGO EJECUTADO EN PYCHARM PARA OBTENER LOS TIPOS DE OBSERVACIONES DE LA VARIABLE TIPOOPERACION	24
IMAGEN 21 CARGA DE ALGUNAS LIBRERÍAS	26
IMAGEN 22 DATOS DE LOS INMUEBLES EN ARCHIVO .CSV	26
IMAGEN 23 APERTURA DE CSV CON PANDAS	27
IMAGEN 24 MÉTODOS PARA ENTENDER EL DATAFRAME	27
IMAGEN 25 SALIDA DE DATOS DE LA FUNCIÓN .INFO()	28
IMAGEN 26 DATOS RECUPERADOS EN EL CSV	28
IMAGEN 27 ANÁLISIS ESTADÍSTICO BÁSICO	29
IMAGEN 28 CLASIFICACIÓN DE INMUEBLES SEGÚN SU TIPO DE OPERACIÓN.	29
IMAGEN 29 CLASIFICACIÓN DE INMUEBLES SEGÚN TENGA O NO TRASTERO.	30
IMAGEN 30 CLASIFICACIÓN DE INMUEBLES SEGÚN TENGA O NO BALCÓN.	30
IMAGEN 31 CLASIFICACIÓN DE INMUEBLES SEGÚN TENGA O NO AIRE ACONDICIONADO.	30
IMAGEN 32 CLASIFICACIÓN DE INMUEBLES SEGÚN SU EFICIENCIA ENERGÉTICA.	31
IMAGEN 33 CLASIFICACIÓN DE INMUEBLES SEGÚN TENGAN O NO TERRAZA.	31
IMAGEN 34 CLASIFICACIÓN DE INMUEBLES SEGÚN TENGAN O NO PISCINA.	31
IMAGEN 35 CLASIFICACIÓN DE INMUEBLES SEGÚN TENGAN O NO ASCENSOR.	31
IMAGEN 36 CLASIFICACIÓN DE INMUEBLES SEGÚN SU EFICIENCIA ENERGÉTICA.	32
IMAGEN 37 CLASIFICACIÓN DE INMUEBLES SEGÚN SU PLANTA.	32
IMAGEN 38 CLASIFICACIÓN DE INMUEBLES SEGÚN SU PLANTA.	33
IMAGEN 39 CLASIFICACIÓN DE INMUEBLES SEGÚN TIPO OPERACIÓN Y HABITACIONES	33
IMAGEN 40 DISTRIBUCIÓN DE LOS BIENES INMUEBLES POR DISTRITOS, AGRUPADOS POR ALQUILER Y VENTA.	33
IMAGEN 41 DISTRIBUCIÓN DE LOS DATOS SEGÚN VARIOS FEATURES.	34
IMAGEN 42 RELACIÓN ENTRE EL TAMAÑO Y EL PRECIO DE BIENES INMUEBLES DE COMPRA-VENTA.	35
IMAGEN 43 DISTRIBUCIÓN DE LOS DATOS SEGÚN VARIOS FEATURES.	35
IMAGEN 44 RELACIÓN ENTRE EL TAMAÑO Y EL PRECIO DE BIENES INMUEBLES DE ALQUILER.	36
IMAGEN 45 VISUALIZAR TIPO DE VARIABLE DE LOS ATRIBUTOS	37
IMAGEN 46 CASTEO DE VARIABLES	38
IMAGEN 47 ONE HOT ENCODING	38
IMAGEN 48 CÓDIGO FUENTE QUE REALIZA LA HERRAMIENTA ONE HOT ENCODING	41
IMAGEN 49 DATOS QUE DEVUELVE LA FUNCIÓN INFO()	42
IMAGEN 50 DATOS QUE DEVUELVE LA FUNCIÓN HEAD ()	43
IMAGEN 51 DATOS QUE DEVUELVE LA FUNCIÓN COLUMN.VALUES ()	43
IMAGEN 52 BÚSQUEDA DE VALORES NULOS O FALTANTES.	44
IMAGEN 53 CÓDIGO UTILIZADO PARA ELIMINAR REGISTROS DUPLICADOS.	45
IMAGEN 54 CÓDIGO QUE ELIMINA LOS OUTLIERS SEGÚN LOS PERCENTILES INTRODUCIDOS A ELIMINAR	45
IMAGEN 55 DISTRIBUCIÓN DE LOS DATOS SEGÚN VARIOS FEATURES.	46
IMAGEN 56 RELACIÓN ENTRE EL TAMAÑO Y EL PRECIO DE BIENES INMUEBLES DE COMPRA-VENTA.	46
IMAGEN 57 DISTRIBUCIÓN DE LOS DATOS SEGÚN VARIOS FEATURES.	47
IMAGEN 58 RELACIÓN ENTRE EL TAMAÑO Y EL PRECIO DE BIENES INMUEBLES DE ALQUILER.	47
IMAGEN 59 DISTRIBUCIÓN DE LOS DATOS DE COMPRA-VENTA SEGÚN EL DISTRITO AL QUE PERTENECEN.	48
IMAGEN 60 DISTRIBUCIÓN DE LOS DATOS DE ALQUILER SEGÚN EL DISTRITO AL QUE PERTENECEN.	49
IMAGEN 61 PARTE DEL CÓDIGO FUENTE QUE BORRA LOS POSIBLES OUTILERS.	50
IMAGEN 62 RELACIÓN ENTRE EL TAMAÑO Y EL PRECIO DE BIENES INMUEBLES DE COMPRA-VENTA.	51
IMAGEN 63 RELACIÓN ENTRE EL TAMAÑO Y EL PRECIO DE BIENES INMUEBLES DE ALQUILER.	51
IMAGEN 64 FUNCIONES PARA EL ESTUDIO DE LOS DATAFRAMES.	52
IMAGEN 65 PEARSON CORRELATIONAL MODEL	53
IMAGEN 66 PEARSON CORRELATIONAL MODEL	54
IMAGEN 67 CORRELACIÓN DEL DATAFRAME DE COMPRA-VENTA.	55
IMAGEN 68 CÁLCULO DE MEDIA Y SESGO DEL DATAFRAME DE ALQUILER	56
IMAGEN 69 REGISTROS TOTALES DE DATAFRAMES DE COMPRA-VENTA Y ALQUILER.	58
IMAGEN 70 DIVISIÓN DEL ALGORITMO DE ENTRENAMIENTO Y PRUEBAS	59
IMAGEN 71 TUNEADO DE LOS MODELOS	60
IMAGEN 72 FUNCIONES DE MODELADO	61
IMAGEN 73 EVALUACIÓN DE LOS MODELOS PARA COMPRA-VENTA	62
IMAGEN 74 VISUALIZACIÓN DE LOS MODELOS PARA COMPRA-VENTA	62
IMAGEN 75 EVALUACIÓN DE LOS MODELOS PARA ALQUILER	63
IMAGEN 76 VISUALIZACIÓN DE LOS MODELOS PARA ALQUILER	63
IMAGEN 77 MODELO GENERADO DE COMPRA-VENTA	64
IMAGEN 78 MODELO GENERADO DE ALQUILER	64
IMAGEN 79 DASHBOARD DATOS SIN PROCESAR	65
IMAGEN 80 DIFERENTES FILTROS DEL DASHBOARD	65
IMAGEN 81 DASHBOARD DATOS PROCESADOS	66
IMAGEN 82 DIFERENTES FILTROS DEL DASHBOARD	66
IMAGEN 83 RELACIÓN PRECIOS VENTA POR DISTRITOS DE MADRID DE DATOS SIN PROCESAR	67
IMAGEN 84 RELACIÓN PRECIOS VENTA POR DISTRITOS DE MADRID DE DATOS PROCESADOS	67
IMAGEN 85 RELACIÓN PRECIOS ALQUILER POR DISTRITOS DE MADRID DE DATOS SIN PROCESAR	68
IMAGEN 86 RELACIÓN PRECIOS ALQUILER POR DISTRITOS DE MADRID DE DATOS PROCESADOS	68
IMAGEN 87 RELACIÓN PRECIOS VENTA REAL VS PREDICCIÓN	70
IMAGEN 88 RELACIÓN PRECIOS ALQUILER REAL VS PREDICCIÓN	70
IMAGEN 89 WEB OFICINAL DOCKER	73
IMAGEN 90 ACCESO A BBDD MYSQL EN DOCKER	74
IMAGEN 91 VISUALIZACIÓN BBDD EN MYSQL	75
IMAGEN 92 VISUALIZACIÓN BBDD EN MYSQL	75


TABLAS
TABLA 1 TECNOLOGÍAS Y HERRAMIENTA UTILIZADAS	13
TABLA 2 DATOS INSERTADOS EN BASE DE DATOS	22
TABLA 3 DATOS CSV	25
TABLA 4 DATOS CSV	39
TABLA 5 ONE HOT ENCONDING DE GARAJE	40
TABLA 6 ONE HOT ENCONDING DE CIUDAD	40
TABLA 7 ONE HOT ENCONDING DE EFICIENCIA ENERGÉTICA	40
TABLA 8 LIMPIEZA DE OUTLIERS	45
TABLA 9 DATOS RESULTANTES	47
TABLA 10 LIMPIEZA DE DATOS SOSPECHOSOS	50
TABLA 11 FORMA DE LOS DATOS RESULTANTES	50

 
1.- INTRODUCCIÓN
El presente trabajo se trata del Proyecto Final del Programa Superior en Big Data impartido por el Instituto Tecnológico Telefónica. El objeto de dicho proyecto ha sido utilizar las herramientas y conocimientos adquiridos gracias a este curso y la investigación autónoma.
Para su realización hemos seguido la metodología CRISP-DM (Cross Industry Standard Process for Data Mining), el cual nos proporciona una descripción normalizada del ciclo de vida de un proyecto estándar de análisis de datos, de forma análoga a como se hace en la ingeniería del software con los modelos de ciclo de vida de desarrollo de software. El modelo CRISP-DM cubre las fases de un proyecto, sus tareas respectivas, y las relaciones entre estas tareas.

Imagen 1 Diagrama metodología CRISP-DM 
2.- COMPRENSIÓN DEL NEGOCIO
Ante la situación sanitaria que vivimos como consecuencia del COVID, en el que el confinamiento ha hecho pensar a muchos si el espacio donde vive realmente satisface sus necesidades, y la inevitable necesidad de tener un hogar en el que vivir, hemos utilizado la tecnología de Big Data para el entorno inmobiliario. Inicialmente se pensó en diversas variantes que podría tener el aplicativo:
1-	Conocer las viviendas de personas que tuvieran una edad superior a 70 años, cuyos propietarios no tuvieran descendientes, para realizar una oferta por debajo de mercado, pudiendo sacar rentabilidad a la hora de poder posteriormente poner en el mercado ese inmueble. Para ello se necesitaría saber los datos censales de Madrid y las propiedades de los ciudadanos.
2-	Poder predecir cuando el mercado inmobiliario subiría o bajaría dependiendo de los datos de paro, inmigración, emigración, porcentaje de jóvenes que se van a emancipar, salarios medios.
3-	Predecir la posible expansión geográfica de la ciudad hacia una determinada zona, para poder invertir en suelos rústicos, que posteriormente el ayuntamiento los recalificaría en suelos urbanizables, conllevando una sustancial revalorización económica de dichos suelos. Para ello necesitaríamos conocer los datos censales, datos de inmigración y emigración, estudiar a que zonas geográficas se está yendo la gente a vivir por la imposibilidad de comprar o alquilar inmuebles en zonas más céntricas.
4-	Predecir el precio de venta o alquiler de los bienes inmuebles, ya que pensamos que es un buen nicho de mercado, para que los usuarios no publiquen sus inmuebles ni fuera del mercado ni por debajo de él. Para ello, necesitaríamos conocer el precio de venta o alquiler de los inmuebles en el momento exacto de predicción. También necesitaríamos conocer las características de cada uno de los inmuebles.
Finalmente, y como toma de contacto con el sector Big data, hemos pensado en realizar inicialmente el punto 4, pudiendo dejar abierta las demás opciones para una posible evolución.
Nuestra motivación es poder utilizar la aplicación en un futuro para generar beneficios del sector inmobiliario, ya que dicho sector tiene un papel muy importante en la economía española tanto en términos de inversión, como a través del empleo.

 
3.- ARQUITECTURA Y TECNOLOGÍAS UTILIZADAS

3.1.- ARQUITECTURA
A continuación, se presenta una descripción de los diferentes flujos que sigue nuestra aplicación para realizar las siguientes acciones:
3.1.1.- CAPA DE ALMACENAMIENTO

Imagen 2 Flujo de almacenamiento
Flujo que sigue nuestra app en el módulo de almacenamiento de los datos, los cuales se almacenan en base de datos y en un archivo .csv.

3.1.2.- CAPA DE PROCESAMIENTO

Imagen 3 Flujo de procesamiento

Como se ve en la imagen 3, a partir de los datos contenidos en el csv, se realizan diversas acciones de aprendizaje para obtener los modelos de predicción, empleando para ello diferentes acciones.

3.1.3.- CAPA DE INPUTS

Imagen 4 Flujo de almacenamiento
Este el flujo de acciones que sigue la aplicación, cuando el usuario introduce los valores de su inmueble a predecir.
3.1.4.- CAPA DE VISUALIZACIÓN

Imagen 5 Flujo de visualización
Con los datos procesados y las coordenadas de los distritos de la ciudad de Madrid, generamos un dashboard final para una mejor compresión y visualización de los datos finales.


 
3.2.- TECNOLOGIAS
TECNOLOGIA	OBJETIVO	HERRAMIENTAS	OBJETIVO
Python 3.8	Desarrollo de código de cara a hacer web scrapping, preprocesar datos, modelar predecir…	Pycharm Community Edition 2020.2.1 64x	IDE de desarrollo para proyectos Python
Database MySql 8.0.22	Almacenamiento de datos	GitHub desktop	Control de versiones e integración continua
GitHub	Control de versiones e integración continua	MySQL Workbench 8.0 CE	Almacenamiento de datos
Docker	Contenedor	Trello	Seguimiento del Proyecto
PyPy	Repositorio de instalación utilizado por convención de manera estándar	OneDrive	Documentos compartidos
Anaconda	Proveedor de herramientas de Big Data y creador de entornos virtuales	Power BI	Analítica y visualización de datos
GoConqr	herramienta web que permite crear mapas y diagramas	www.goconqr.com	Realización de diagramas de flujo
Tabla 1 Tecnologías y Herramienta utilizadas

3.2.1.- PYTHON 3.8
Tratándose del lenguaje de programación enseñado durante el curso, se ha decidido utilizar éste como lenguaje para el desarrollo de todas las partes de código necesarias.

Imagen 6 Icono lenguaje Python
 
3.2.2.-  BBDD MYSQL 8.0.22
Con objeto de poder recopilar toda la información procedente de los diferentes portales web utilizados como fuentes de la información de una forma estructurada, dado estos se encuentran de forma semiestructurada codificados mediante lenguaje HTML en las mismas, en el presente proyecto hemos planteado el uso de una Base de Datos MySQL para su almacenamiento y estructuración y Workbench como herramienta de gestión de la misma.

Imagen 7 Icono MySql y Workbench

3.2.3.- GITHUG
Ante la necesidad de compartir código entre los diferentes integrantes del proyecto, hemos explorado y utilizado el uso de la plataforma GitHub (https://github.com) para subir a ella todo el código y posibilitar desde ahí una fácil distribución de la información y control de versiones.

3.2.4.- DOCKER
Mientras que la virtualización tradicional de hardware se basa en iniciar diferentes sistemas invitados en un mismo sistema anfitrión denominado “host”, la plataforma Docker de código abierto permite automatizar el despliegue de aplicaciones dentro de contenedores de software proporcionando una capa adicional de abstracción y automatización de virtualización de aplicaciones en múltiples sistemas operativos muy interesante sobre la que nos hemos decido intentar utilizar, con objeto de mejorar la agilidad de despliegue del código de nuestro proyecto, la Base de Datos MySQL en la que se apoya la recopilación de la información del proyecto.

Imagen 8 Estructura Máquina Virtual vs Virtualización mediante contenedores
Aunque al igual que sucede con la virtualización hardware tradicional, ambas tecnologías permiten instalar diferentes aplicaciones con distintos requisitos en paralelo en un mismo sistema físico
Sus diferencias más notables se basan en el empleo de los recursos y la portabilidad, las cuales evitan la gran sobrecarga en el uso de recursos de la maquina (memoria, CPU, disco…) derivada de tener que implementar todo un sistema completo y es por ello que nos ha parecido interesante explorar esta posibilidad en la instalación de software orientado al SaaS tan de moda en estos tiempos de computación en la nube.
Sin embargo, y pese a todas las bondades que presenta esta plataforma, durante la realización de implementación y pese a que teóricamente Docker se trata de una herramienta multiplataforma de virtualización hemos tenido que desistir en su uso ante los problemas sufridos para utilizarla en sistemas Windows y teniendo que optar finalmente por implementar un escenario en el que todo se integre dentro de la misma máquina con un escenario tradicional en el que la BBDD sea instalada como un aplicativo más de la misma.
La opción de crear un servidor expresamente para esta función en entorno LINUX con DOCKER nos ha parecido poca práctica dado que al fin y al cabo sería como montar una máquina virtual (con todos sus requisitos) con una Base de Datos publicada.
No obstante, en el ANEXO I: Instalación, configuración y verificación de Docker, se indican los pasos necesarios para poderla tener operativa.


3.2.5.- POWER BI
Herramienta para la visualización de los resultados obtenidos de una forma sencilla e intuitiva sobre la que se ha decidido implementar algunos Dashboard para facilitar la comprensión de los resultados y tendencias tanto para los analistas como para usuarios finales de la aplicación.

Imagen 9 Icono Power BI

3.2.6.- PYCHARM COMUNITY EDITION 2020.2.1 64X
Esta herramienta ha sido la utilizada, entre las que nos podemos encontrar en el mercado, como IDE para la realización de todo el código necesario para realización del proyecto.

Imagen 10 Icono herramienta PyCharm

3.2.7.- GITHUB DESKTOP
GitHub Desktop ha sido la herramienta utilizada, junto a GitHub (https://desktop.github.com/), para la gestión del código del proyecto desde los equipos Windows con los que se ha trabajado.

Imagen 11 Icono GitHub
3.2.8.-  TRELLO
Plataforma colaborativa mediante la cual hemos intentado coordinarnos durante la realización del proyecto de una forma ágil, visual e intuitiva. Aunque no siempre ha sido posible posiblemente porque ninguno estábamos familiarizado con ella y la curva de aprendizaje/gestión de proyecto se ha complicado enormemente.

Imagen 12 Icono Plataforma Trello (https://trello.com/)

3.2.9.-   ONEDRIVE
Como consecuencia de la necesidad de intercambiarnos información de diferentes tipos también hemos recurrido a OneDrive como herramienta en la nube de intercambio de información, que dada su conocido uso y funcionamiento poco hay que explicar de ella.

Imagen 13 Icono Plataforma OneDrive
 
4.- COMPRENSIÓN DE LOS DATOS

4.1.- RECOLECTAR DATOS

En esta fase deberemos ser capaces de:
•	Ejecutar procesos de captura de datos.
•	Proporcionar una descripción del juego de datos.
•	Realizar tareas de exploración de datos.
•	Gestionar la calidad de los datos, identificando problemas y proporcionando soluciones.
Antes de llegar a la conclusión de que realizaríamos la opción 4, intentamos recopilar información sobre todas las opciones propuestas para poder decantarnos por una de ellas. Para ello, hemos investigado tanto en fuentes privadas, municipales o gubernamentales (Ver en ANEXO I: Fuentes de información analizadas)
Finalmente, determinamos que la mejor fuente de información serían los portales de venta o alquiler de pisos tales como:
-	AirBNB  (http://insideairbnb.com/get-the-data.html)
Este portal ofrece amplia información sobre los precios de alquileres de viviendas y habitaciones por días presentes en la web en un formato CSV pero dado el tipo de mercado al que va dirigido, en el que actualmente las limitaciones en la movilidad de las personas a causa de la prohibiciones y las restricciones auto aplicadas por las empresas para limitar el movimiento de sus empleados, unido a que los datos aportados presentan un espaciado temporal mensual, hacen que la información no sea muy relevante dado la adulteración del mercado y lo espaciado de los mismos.

-	Idealista (https://www.idealista.com/)
Se trata de uno de los principales portales web utilizados en España, y como tal presenta gran cantidad de inmuebles y múltiples tipos de filtros que permiten visualizar mediante su plataforma web multitud de información. Pese a la gran cantidad de información que ofrece al usuario mediante su interfaz web es difícilmente exportable ya que no permite descargar la información mediante el uso de plataformas externas.

Imagen 14 Portal idealista.com
En él, encontramos la posibilidad incluso de mediante una API pensada para tareas de análisis como la nuestra, nos hicieron plantearnos un gran abanico de posibilidades de análisis y estudio de la información https://www.idealista.com/labs/, pero que pronto descubrimos que esta API solo nos ofrecía unas funcionalidades muy limitadas de consulta dado solo nos permitía realizar unas pocas consultas al mes.

Imagen 15 Web de desarrollo de idealista.com
Pese a las limitaciones detectadas, continuamos explorando las posibilidades que nos daba la web mediante técnicas de Web Scraping para tratar de sacar la tan abundante información que tiene este sitio web, pero nuevamente nos encontramos con nuevas problemáticas. En este caso, una Legal y otra Técnica que nos obligó a cesar en nuestro desempeño.

Imagen 16 Proceso de extracción y estructuración de datos de un site
Seguramente mediante algún tipo de alianza o pago sea posible hacer uso de la API que tienen implementada de una forma más intensiva, pero esto no ha sido explorado al quedar fuera del alcance del presente trabajo.

LEGAL:
Al analizar más en profundamente la web de idealista.com vimos como en la se sección de términos y condiciones de uso del sitio web se indica expresamente que este tipo de acciones de extracción de la información desde en su sitio web están prohibidas:

Imagen 17 Términos y condiciones Idealista.com

 
TÉCNICO:
Al lanzar la aplicación desarrollada para la extracción de la información de una forma más continuada (ya no para simples pruebas de funcionamiento y depuración) con objeto de poblar la Base de Datos MySQL contrastamos las diferentes medidas que tiene el sitio web implementados para bloquear intentos de acceso no legítimos a la web como:
	Filtrado de cabeceras HTTP no procedentes típicamente de navegadores web tradicionales, esto es, peticiones HTTP mediante módulos Python.
	Bloqueo ante la realización grandes cantidades de consultas por minuto
	Bloqueo antes grandes cantidades de consultas realizadas desde una misma IP
	Filtrado de PROXY gratuitos existente en nube para la distribución de las consultas mediante el empleo de diferentes maquinas e IPs
Llegados a este punto en el que detectamos el problema técnico, y vista la nota legal encontrada en la propia web, tuvimos que cesar en nuestro empeño de extracción de información de esta web solo pudiendo obtener de ella unas pocas referencias sin valor alguno para nuestro proyecto por la escasez e inconexión de las mismas.
-	Fotocasa (https://www.fotocasa.es/es/)
Portal muy importante en el sector inmobiliario nacional, similar a idealista, el cual te ofrece información muy detallada sobre los bienes inmuebles, tanto para alquilar como para su compra-venta.
Nuevamente, y ante la falta de una API facilitada por la propia web, procedimos a realizar una extracción de datos haciendo uso de técnicas de Web Scraping mediante el desarrollo de un pequeño módulo Python llamado recuperarDatos, que hace uso de librerías como  Beautiful Soap, chromedriver.exe y geckodriver.exe, con los que si alcanzamos buenos resultados permitiéndonos almacenar sobre una Base de Datos MySQL información de los inmuebles que posteriormente analizaremos y sobre los cuales pudimos realizar los análisis y predicciones que en los siguientes apartados del presente proyecto iremos desgranando.
Para ello, hemos realizado dentro del proyecto, un módulo denominado recuperarDatos:

Imagen 18 Módulo de extracción de información de Fotocasa.
El cual abre la página web de fotocasa (con la ayuda de chromedriver.exe y geckodriver.exe) y recupera las publicaciones de los diferentes distritos de la ciudad de Madrid. De cada publicación, recuperamos los siguientes datos(Tabla 2) que guardamos en la base de datos.
CAMPO TABLA	TIPO DATO
idInmueble	Número de identificador introducido auto incrementalmente por la base de datos a cada registro de la tabla
urlInmueble	URL de descarga de los datos para cada publicación
fuenteInfo 	Fotocasa
tipoInmueble 	vivienda/local
tipoOperacion 	comprar/alquilar
precio 	Precio de venta o alquiler en Euros
habitaciones	Número de habitaciones de la vivienda
tamano 	Tamaño en m2 de la vivienda
planta 	Ubicación vertical de la vivienda
distrito	Distrito de la ciudad al que pertenece
ciudad 	Madrid-capital
fecha	Fecha de introducción de los datos en base de datos
descripción 	Descripción más detallada que ha podido introducir el usuario de la vivienda
eficienciaEnergetica 	tipo de categorización de eficiencia energética (A, B, C, D, E, F, G)
ascensor 	Si/No
terraza 	Si/No
garaje 	Si/No
balcon 	Si/No
aireAcondicionado 	Si/No
piscina 	Si/No
vendedor 	Nombre de inmobiliaria / particular
banios 	Número de baños de la vivienda
Tabla 2 Datos insertados en Base de Datos
El script para la creación de la base de datos está incluido en el ANEXO III: Script creación base de datos MySql.
Cabe destacar que, mientras recuperamos los datos de las publicaciones de la web Fotocasa, vamos tratando los mismos para que no se guarden nulos, por lo que posteriormente en la fase 3.- Preparación de los datos no tendremos este inconveniente.
El módulo mencionado, una vez ha insertado en base de datos todas las publicaciones, crea un fichero CSV, que se guarda en el directorio data, para poder tratar los datos y generar posteriormente el modelo de predicción.

Imagen 19 Directorio del módulo de extracción de información de Fotocasa, donde vamos a ubicar el CSV que utilizaremos para generar el modelo de predicción

IMPORTANTE: Este módulo solo se ejecuta cuando queramos generar nuevos datos más actualizados para un nuevo modelo de predicción. Al ejecutar dicho módulo, el proceso de recuperación e inserción de datos en base de datos y su posterior creación del fichero .CSV tarda alrededor de unas 5-6 horas, dependiendo del volumen de datos que tenga en ese instante la web Fotocasa.



4.2.- DESCRIBIR DATOS
Los datos que hemos recuperado están formados por un conjunto de 12.627 observaciones en bruto recuperados de la web, con 17 variables. El conjunto de datos no presenta valores nulos, como hemos indicado anteriormente, formados por 2.939 observaciones clasificadas como compra-venta y 9.688 observaciones clasificadas como alquilar.

Imagen 20 Código ejecutado en Pycharm para obtener los tipos de observaciones de la variable tipoOperacion

Las variables y sus tipos de datos son las siguientes:
 
CAMPO TABLA	TIPO DATO
tipoInmueble	vivienda = 1
local = 2
tipoOperacion	comprar = 1
alquilar = 2
habitaciones	Número de habitaciones de la vivienda = 0, 1, 2 …
tamano	Tamaño en m2 de la vivienda
planta	Ubicación vertical de la vivienda = 0, 1, 2 ...
distrito	Distrito de la ciudad al que pertenece:
arganzuela
barajas
carabanchel
centro
chamartin
chamberi
ciudad_lineal
fuencarral
hortaleza
latina
moncloa
moratalaz
puente_de_vallecas
retiro
salamanca
san_blas
tetuan
usera
vicalvaro
villa_de_vallecas
villaverde
ciudad	madrid-capital
eficienciaEnergetica	A, B, C, D, E, F, G
ascensor	True/False
terraza	True/False
trastero	True/False
garaje	No-detallado
Privado
Comunitario
balcon	True/False
aireAcondicinado	True/False
piscina	True/False
banos	Número de baños de la vivienda = 0, 1, 2 …
precio	precio de venta o alquiler en Euros
Tabla 3 Datos CSV
4.3.- EXPLORACIÓN Y VERIFICACIÓN DE LOS DATOS
Una vez cargadas la mayor parte de las librerías que vamos a necesitar:

Imagen 21 Carga de algunas librerías

Cargamos en el código el archivo .CSV con todos los datos de la base de datos, el cual se llama:  datos_fotocasa_final.csv.

Imagen 22 Datos de los inmuebles en archivo .CSV

De entre las varias formas de carga de archivos en Python, hemos elegido abrirlo con la librería pandas. A la vez, hemos creado una función que lo convierte en un Dataframe.

Imagen 23 Apertura de CSV con pandas

Vemos la información general de nuestro Dataset. Llamamos a la función vistazo donde podemos ver las cinco primeras líneas, las cinco últimas, los valores de cada columna, comprobamos que no haya valores faltantes en ninguna columna y conocemos en detalle la cantidad de datos que tenemos (filas y columnas).

Imagen 24 Métodos para entender el Dataframe

Al ejecutar el método vistazo (), entre otros, podemos observar la función .info(), el cual nos indica el DType de cada atributo del CSV:

Imagen 25 Salida de datos de la función .Info()

A continuación, mostramos una imagen de algunos registros del fichero CSV:

Imagen 26 Datos recuperados en el CSV

Se procede a realizar un análisis estadístico básico, para entender mejor los datos: cálculo de la media, la desviación estándar y los cuartiles para todas las variables.


Imagen 27 Análisis estadístico básico

Para tener una mejor visión de los datos, analizamos gráficamente los datos recuperados:

Imagen 28 Clasificación de inmuebles según su tipo de operación.

Imagen 29 Clasificación de inmuebles según tenga o no trastero.


Imagen 30 Clasificación de inmuebles según tenga o no balcón.


Imagen 31 Clasificación de inmuebles según tenga o no aire acondicionado.


Imagen 32 Clasificación de inmuebles según su eficiencia energética.

Imagen 33 Clasificación de inmuebles según tengan o no terraza.

Imagen 34 Clasificación de inmuebles según tengan o no piscina.

Imagen 35 Clasificación de inmuebles según tengan o no ascensor.

Imagen 36 Clasificación de inmuebles según su eficiencia energética.


Imagen 37 Clasificación de inmuebles según su planta.

Imagen 38 Clasificación de inmuebles según su planta.

Imagen 39 Clasificación de inmuebles según tipo operación y habitaciones

Imagen 40 Distribución de los bienes inmuebles por distritos, agrupados por alquiler y venta.
Como hemos recuperado inmuebles de compra-venta y alquiler, ha sido necesario dividir los datos en 2 Dataframes clasificados por los mismos. Esto se realiza para estructurar mejor los datos y que a la hora de entrenar y generar un buen modelo para la predicción, tenga una mayor precisión y no se distorsione el resultado final por tener valores en el feature de precios con tanta diferencia.
4.4.- OUTLIERS
Una vez hemos dividido los datos recuperados en bruto en 2 Dataframe, vamos a comprobar los datos Outliers que tienen cada uno. Los Outliers en nuestro Dataset serán los valores que se “escapan al rango en donde se concentran la mayoría de las muestras”, siendo las muestras que están distantes de otras observaciones.
BIENES INMUEBLES COMPRA-VENTA:

Imagen 41 Distribución de los datos según varios features.
Como se puede observar en la figura, hay bastantes datos que se encuentran fuera del rango medio de distribución de las demás muestras, por lo que tendremos que realizar posteriormente un tratamiento a los datos Outilers.

Imagen 42 Relación entre el tamaño y el precio de bienes inmuebles de compra-venta.
Se observa que hay valores distorsionados; por ejemplo, se pueden encontrar registros de bienes inmuebles de venta, donde su precio es bastante elevado para los metros cuadrados que tiene la casa y viceversa, los cuales son dudosos, y deberíamos de estudiarlos para tenerlos en cuenta a la hora de generar el modelo de predicción.
BIENES INMUEBLES ALQUILER

Imagen 43 Distribución de los datos según varios features.
Como se puede observar en la figura, hay bastantes datos que se encuentran fuera del rango medio de distribución de las demás muestras, por lo que tendremos que realizar posteriormente un tratamiento a los datos Outilers.

Imagen 44 Relación entre el tamaño y el precio de bienes inmuebles de alquiler.
Ocurre lo mismo con registros de bienes inmuebles de alquiler cuyos precios de alquiler son demasiado elevados con respecto a las características de la casa.
Se observa que hay valores distorsionados; por ejemplo, se pueden encontrar registros de bienes inmuebles de alquiler, donde su precio es bastante elevado para los metros cuadrados que tiene la casa y viceversa, los cuales son dudosos, y deberíamos de estudiarlos para tenerlos en cuenta a la hora de generar el modelo de predicción.
Para solucionar los problemas de datos incoherentes que puedan ocasionar un mal modelaje y posteriormente una predicción de muy mala calidad, en el punto 3.- Preparación de los datos realizaremos el tratamiento de los datos, limpiándolos de valores nulos, duplicados y Outliers.
 
5.-  PREPARACIÓN DE LOS DATOS

5.1.- ESTRUCTURAR LOS DATOS

Imagen 45 Visualizar tipo de variable de los atributos

Tal como se ve en la imagen 42, hay datos donde su DType es un objeto o un booleano, por lo que realizamos un casteo de sus variables para convertirlas en el tipo de dato que mejor nos conviene:

Imagen 46 Casteo de variables

El Dataframe tiene 4 columnas donde su Dype es un object:

Imagen 47 One Hot Encoding

Para este tipo de datos, realizamos un One Hot Encoding.  La estrategia que implementa es crear una columna para cada valor distinto que exista en la característica que estamos codificando y, para cada registro, marcar con un 1 la columna a la que pertenezca dicho registro y dejar las demás con 0.
COLUMNA DISTRITO: en nuestro Dataframe la columna distrito puede tener hasta 21 distritos diferentes:
TIPOS DISTRITOS
distrito_arganzuela
distrito_barajas
distrito_carabanchel
distrito_centro
distrito_chamartin
distrito_chamberi
distrito_ciudad_lineal
distrito_fuencarral
distrito_hortaleza
distrito_latina
distrito_moncloa
distrito_moratalaz
distrito_puente_de_vallecas
distrito_retiro
distrito_salamanca
distrito_san_blas
distrito_tetuan
distrito_usera
distrito_vicalvaro
distrito_villa_de_vallecas
distrito_villaverde
Tabla 4 Datos CSV

Con la herramienta One hot encoding, en el Dataframe se crearían 21 columnas. Cada columna llevará el nombre de los diferente4s distritos, y si el registro pertenece a ese distrito, se marcará con un 1, por el contrario, con un 0.


COLUMNA TIPOS DE GARAJES: en nuestro Dataframe la columna GARAJE puede tener hasta 3 tipos diferentes:
TIPOS DE GARAJES
garaje_Comunitario
garaje_No_detallado
garaje_Privado
Tabla 5 One Hot Enconding de Garaje
Con la herramienta One Hot Encoding, en el Dataframe se crearían 3 columnas. Cada columna llevará el nombre del tipo de garaje y si el registro tiene ese garaje, se marcará con un 1, por el contrario, con un 0.

COLUMNA CIUDAD: en nuestro Dataframe la columna ciudad puede tener hasta 1 tipo solamente, ya que solo hemos recuperado datos para la ciudad de Madrid:
CIUDADES
madrid_capital
Tabla 6 One Hot Enconding de Ciudad

Con la herramienta One Hot Encoding, en el Dataframe se crearían tantas columnas como ciudades tengamos en el Dataframe. Como en nuestro caso, solo tenemos registros pertenecientes a Madrid, se introduce el valor 1 en todos los registros del Dataframe.

COLUMNA EFICIENCIA ENERGETICA: en nuestro Dataframe la columna eficiencia energética puede tener 3 tipos:
LISTADO DE EFICIENCIA ENERGETICA
eficienciaEnergetica_A
eficienciaEnergetica_B
eficienciaEnergetica_C
Tabla 7 One Hot Enconding de Eficiencia Energética
Con la herramienta One Hot encoding, en el Dataframe se crearían 3 columnas. Cada columna llevará el nombre del tipo de eficiencia energética y si el registro pertenece a ese distrito, se marcará con un, y por el contrario con un 0.

Imagen 48 Código fuente que realiza la herramienta One Hot Encoding








5.2.- INTEGRAR LOS DATOS
Una vez tenemos todas las variables de nuestro Dataframe clasificadas y bien organizadas, si ejecutamos el método vistazo () de la figura 10, se mostrarían los datos de la siguiente manera, 3.3. Información de los datos


 
5.3.- INFORMACIÓN DE LOS DATOS
La función Info () muestra el total de registros que tiene cada columna y su tipo de dato.

Imagen 49 datos que devuelve la función info()









 
La función head () muestra los primeros 5 registros de los Dataframes:



Imagen 50 datos que devuelve la función head ()

La función column.values () muestra el nombre de las columnas de los dataframes.

Imagen 51 Datos que devuelve la función column.values ()

La función isnull().sum() muestra el total de nulos que tiene cada una de las columnas del Dataframe (Se ha realizado sobre los 2 Dataframes, compra-venta y alquiler).


Imagen 52 Búsqueda de valores nulos o faltantes.

Como se indicó anteriormente en el punto 2.- Recolectar Datos, se trataron los datos mientras los recuperábamos de la web de Fotocasa, por lo que eliminamos los nulos.
Un problema habitual en los conjuntos de datos es la existencia de registros duplicados. La duplicidad puede ser del registro completo o solamente de unos elementos. Por ejemplo, se ha registrado dos veces la misma operación con diferente identificador. Saber cómo eliminar estos registros duplicados es imprescindible para evitar posibles errores en los análisis posteriores. En esta, se explicarán los métodos disponibles en los Dataframes para la eliminación de registros duplicados en pandas.

Imagen 53 Código utilizado para eliminar registros duplicados.

Para eliminar los datos Outliers explicados en el punto 2.4.- Outliers, hemos eliminado los siguientes datos de los 2 Dataframes:

TIPO DE INMUEBLE	VALORES ELIMINADOS
Compra-venta	< percentil 25
> percentil 75
Alquiler	< percentil 20
> percentil 80
Tabla 8 Limpieza de Outliers



Imagen 54 Código que elimina los Outliers según los percentiles introducidos a eliminar





 
BIENES INMUEBLES COMPRA-VENTA

Imagen 55 Distribución de los datos según varios features.

Imagen 56 Relación entre el tamaño y el precio de bienes inmuebles de compra-venta.
Ahora sí, tenemos ya una distribución más homogénea de los datos.
 
BIENES INMUEBLES ALQUILER

Imagen 57 Distribución de los datos según varios features.


Imagen 58 Relación entre el tamaño y el precio de bienes inmuebles de alquiler.
Ahora ya tenemos una distribución más homogénea de los datos, pero se han borrado demasiados registros realizando la operativa de Outliers:
TIPO INMUEBLE	REGISTROS INICIALES	REGISTROS TRAS BORRAR OUTILERS
Compra-venta	2939	481
Alquiler	9688	1415
Total	12627	1896
Tabla 9 Datos resultantes
Tras ver que se elimina la gran mayoría de datos, se hace un análisis para entender porque se eliminan tantos registros:

COMPRA-VENTA
De los datos iniciales, como se observa en la Figura 4 del apartado 2.2.- Describir datos, la distribución de los datos según el distrito al que pertenece es el siguiente:

Imagen 59 Distribución de los datos de compra-venta según el distrito al que pertenecen.
De los 481 registros obtenidos tras realizar la operativa Outliers (eliminar los registros superiores al percentil 75 e inferiores al percentil 25), se observa que todos pertenecen al distrito Chamberí.
Esto es debido a que el precio de los inmuebles de compra-venta puede variar mucho según el distrito al que pertenezca, y como la gran mayoría de datos pertenece al distrito Chamberí, los que no estén dentro de sus características los va a borrar.
Por ello se llega a la conclusión de no realizar la operativa Outliers.

ALQUILER
De los datos iniciales, como se observa en la Figura 4 del apartado 2.2.- Describir datos, la distribución de los datos según el distrito al que pertenece es el siguiente:

Imagen 60 Distribución de los datos de alquiler según el distrito al que pertenecen.
De los 1416 registros obtenidos tras realizar la operativa Outliers (eliminar los registros superiores al percentil 80 e inferiores al percentil 20), se observa que todos pertenecen al distrito Centro.
Esto es debido a que el precio de los inmuebles de alquiler puede variar mucho según el distrito al que pertenezca, y como la gran mayoría de datos pertenece al distrito centro, los que no estén dentro de sus características los va a borrar.
Por ello se llega a la conclusión de no realizar la operativa Outliers, pero sí vamos a borrar algunos registros que pueden ser incoherentes:

Imagen 61 Parte del código fuente que borra los posibles Outilers.

TIPO INMUEBLE	ELIMINACIÓN
Compra-Venta	precio < 50.000 Euros
tamaño <10 m2
Alquiler	precio < 100 Euros
precio > 9.000 Euros
tamaño < 10 m2
baños = 0
baños > 8
habitaciones > 7
Tabla 10 Limpieza De Datos Sospechosos

Finalmente, tras el tratado y limpiado de los datos, nuestro Dataframe queda de la siguiente forma:
TIPO INMUEBLE	REGISTROS INICIALES	REGISTROS TRAS BORRAR OUTILERS
Compra-venta	2939	2709
Alquiler	9688	8999
Total	12627	11708
Tabla 11 Forma de los datos resultantes
Distribución de la relación entre el tamaño y el precio de los registros:

Imagen 62 Relación entre el tamaño y el precio de bienes inmuebles de compra-venta.


Imagen 63 Relación entre el tamaño y el precio de bienes inmuebles de alquiler.


 
5.4.- ANÁLISIS DE DATOS CON ESTADÍSTICA DESCRIPTIVA Y VISUALIZACIÓN
Ahora que ya conocemos en general la estructura de nuestro Dataframe, podemos resumir nuestros datos utilizando estadísticas descriptivas. De esta manera, podemos ver los resultados de las observaciones en detalle. Esto también es útil para verificar la presencia de valores NA, de MVs y la distribución de atributos. Para ello, utilizamos el siguiente fragmento de código:

Imagen 64 Funciones para el estudio de los Dataframes.

El cual nos muestra la función describe (), las correlaciones entre las variables, el sesgo, y la media de cada columna.
·	El método describe ():
o	Count: Esto nos dará una idea sobre la cantidad de registros en nuestro conjunto de datos de capacitación.
o	Mean: Este valor nos da una indicación de la media de cada uno de los atributos de los datos.
o	Std: Este valor indica la desviación estándar para cada uno de los atributos de los datos.
o	Min: Este valor nos da una idea de cuál es el valor mínimo para cada uno de los atributos de los datos.
o	25%: Este valor indica el percentil 25.
o	50%: Este valor indica el percentil 50.
o	75%: Este valor indica el percentil 75.
o	max: Este valor nos da una idea de cuál es el valor máximo para cada uno de los atributos de datos.
o
•	Por otro lado, es importante averiguar si existe alguna relación entre las variables. Esto se puede calcular mediante la matriz de correlación. El método más común para calcular la correlación es el coeficiente de correlación de Pearson, que asume una distribución normal de los atributos involucrados: La correlación nos proporciona una indicación del grado de correlación entre dos variables. Si dos variables cambian en la misma dirección, están correlacionadas positivamente; si cambian juntas en direcciones opuestas (una sube y la otra baja), están correlacionadas negativamente.

BIENES INMUEBLES COMPRA-VENTA

Imagen 65 Pearson correlational Model





BIENES INMUEBLES ALQUILER

Imagen 66 Pearson correlational Model

Como se puede apreciar en la figura, la mayoría de las columnas están bastante bien correlacionadas, ya que tienen un tono como el del color 0.00. Se puede apreciar que hay columnas (0, 1, 37) en blanco, que muestran que no tienen ninguna correlación con las demás columnas, y ello es debido a que en estas columnas en blanco en todos sus registros solo hay un tipo de dato que será igual a 1.

·	El Sesgo se refiere a una distribución gaussiana (curva normal o de campana) que se mueve o aplasta en una dirección u otra. Este tipo de distribución existe en muchos algoritmos de aprendizaje automático. Saber que los atributos están sesgados nos permitirá preparar datos que tengan esto en cuenta y hacer correcciones para mejorar la precisión del modelo. El resultado del sesgo muestra una desviación positiva (derecha) o negativa (izquierda). Los valores cercanos a 0 muestran menos sesgo. La media (promedio) de un conjunto de datos se encuentra al sumar todos los números en el conjunto de datos y luego al dividir entre el número de valores en el conjunto.


BIENES INMUEBLES COMPRA-VENTA


Imagen 67 Correlación del Dataframe de compra-venta.





BIENES INMUEBLES ALQUILER

Imagen 68 Cálculo de media y sesgo del Dataframe de alquiler






6.- MODELADO
En esta fase se seleccionan y aplican diferentes técnicas (algoritmos) de modelado, calibrando sus parámetros para conseguir sus valores óptimos.
Para un mismo problema de minería de datos tenemos diferentes técnicas susceptibles de ser usadas y, dado que cada una de ellas puede tener requisitos diferentes en la forma en que deben presentarse los datos de entrada, es probable que sea necesario realizar ciclos adicionales de “preparación de los datos”.
Las principales tareas que abarca esta fase son las siguientes:
-  Selección de la técnica de modelado: Aunque ya desde el principio del proyecto, en la fase de comprensión del negocio, se realiza una selección preliminar del tipo de técnica a emplear, en este caso la tarea se centra en poner “nombre y apellidos” a la técnica, de entre las diferentes opciones de configuración, versionado, etc. que puede presentar.
Además, hay que tener en cuenta que muchas técnicas de modelado funcionan bajo la premisa de unas asunciones específicas sobre los datos (p.ej. distribuciones uniformes, ausencia de MVs, atributos simbólicos para la clase, etc.), por lo que las asunciones realizadas para seleccionar una u otra técnica deben quedar documentadas.

- Diseño de los test: Antes de ponernos a generar un modelo, debemos diseñar el procedimiento según el cual se va a medir la calidad y validez del modelo. Esto abarca la métrica concreta de error que se va a emplear, o la descripción del plan para entrenar y evaluar los modelos, incluyendo el diseño de la separación entre datos de entrenamiento, de testeo y de validación.
- Construcción del modelo: Consiste en la ejecución del algoritmo de modelado seleccionado sobre el Dataset preparado siguiendo el procedimiento diseñado. Es importante documentar la parametrización utilizada y la justificación de la elección, así como una descripción del modelo resultante, lo interpretable que resulta y las dificultades para dicha interpretación.
- Evaluación del modelo: Partiendo de la calidad del modelo o modelos obtenidos según las métricas definidas en el procedimiento diseñado, se realiza también una interpretación y contraste preliminares de los modelos según el conocimiento del dominio y los objetivos de éxito planteados en términos de negocio. La conclusión de esta tarea puede implicar una revisión de la tarea de construcción del modelo para cambiar la configuración de los parámetros de la técnica, y así afinar en la calidad del resultado.
IMPORTANTE: Cabe destacar que nuestro Dataframe tiene registros de datos de viviendas en venta y viviendas en alquiler, por lo que tenemos que dividir en Dataframes diferentes los datos de uno y otro, y generar 1 modelo de predicción por cada uno de ellos.
Esto lo realizamos para que, dependiendo de si el usuario quiere predecir el precio de venta o alquiler de una vivienda, tengamos mejor resultado en la predicción.
Tras analizar, limpiar y dividir los datos en bienes inmuebles de Venta o alquiler, para realizar el plan de pruebas vamos a utilizar 2 Dataframes formados por los siguientes registros:

Imagen 69 Registros totales de Dataframes de Compra-venta y Alquiler.

 
6.1.- SELECCIONAR TÉCNICA DE MODELADO

Como el objeto de este proyecto es predecir el precio de un bien inmueble a través de las características de este, introducidas por el usuario cliente a través de teclado, se realizará un aprendizaje automático supervisado.  Como vamos a predecir una variable continua (precio/alquiler de una vivienda), vamos a realizar una regresión.
Procedemos a realizar una normalización de los 2 dataframes. La normalización es una técnica que se aplica a menudo como parte de la preparación de datos para el aprendizaje automático. El objetivo de la normalización es cambiar los valores de las columnas numéricas del conjunto de datos para usar una escala común, sin distorsionar las diferencias en los intervalos de valores ni perder información. La normalización también es necesaria para que algunos algoritmos modelen los datos correctamente.

6.2.- GENERAR PLAN DE PRUEBAS (CONJUNTOS DE ENTRENAMIENTO Y TEST)
En esta fase, utilizamos diferentes datos de entrenamiento y test. Para ello dividimos el Dataset en dos partes:
-	Entrenamos el algoritmo en la primera parte y realizamos pruebas de predicciones en la segunda parte.
-	Evaluamos las predicciones últimas contra los resultados esperados.
-	Tamaño de la división: Utilizamos el 70% de los datos para entrenar y el 30% para las pruebas.

Imagen 70 División del algoritmo de entrenamiento y pruebas



6.3.- CONSTRUIR MODELO
Como hemos mencionado anteriormente, la predicción que queremos realizar se adecua a algoritmos de regresión, por lo que probaremos con los algoritmos de regresión más importantes para ver cuál de ellos nos proporciona mejor precisión.
Algunos de los algoritmos que vamos a utilizar van a estar tuneados, para optimizar los parámetros de los modelos, en vista de mejorar los scores de cada modelo.

Imagen 71 Tuneado de los modelos
Los que están tuneados realizarán un GridSearchCV y los que no, realizaran una cross validation score
 

Imagen 72 Funciones de modelado

 
6.4.- EVALUAR EL MODELO (COMPARACIÓN DE MODELOS)

Imagen 73 Evaluación de los modelos para compra-venta


Imagen 74 Visualización de los modelos para compra-venta

Según se puede observar en la imagen 73 e imagen 74, el mejor algoritmo para realizar la predicción de nuestro trabajo para los datos de compra-venta es GradientBoostingRegressor, con un validation score de 0,83


Imagen 75 Evaluación de los modelos para alquiler


Imagen 76 Visualización de los modelos para alquiler

Según se puede observar en la imagen 75 e imagen 76, el mejor algoritmo para realizar la predicción de nuestro trabajo para los datos de alquiler es GradientBoostingRegressor, con un validation score de 0,75
6.5.- GUARDADO DEL MODELO.
Una vez hemos comprobado en el apartado 4.2.- Evaluar el modelo(comparación de modelos) el algoritmo que mejor se ajusta para realizar el trabajo, procedemos a guardar el modelo. Guardaremos un modelo para precio de venta-compra y otro de alquiler de bienes inmuebles, para utilizarlo para la posterior predicción, cuando el usuario introduzca por teclado los valores del bien inmueble que quiere predecir.

Imagen 77 Modelo generado de compra-venta


Imagen 78 Modelo generado de alquiler


 
7.- VISUALIZACIONES CON POWER BI
Hemos realizado dos dashboard mediante power BI para facilitar la visualización de la información y la compresión de los datos.
El primero de ellos, visualizamos la información sin procesar, con objeto de poder comprender mejor la información recuperada. Así, con un simple clic, es posible analizar las diferentes variables asociadas a los inmuebles que tienen nuestros datos.

Imagen 79 Dashboard datos sin procesar


Imagen 80 Diferentes filtros del dashboard

El segundo, visualizamos la información procesada (Enlace visualización dashboard Power BI), con objeto de poder comprender mejor la información que tenemos para poder realizar el modelo para la predicción. Así, con un simple clic, es posible analizar las diferentes variables asociadas a los inmuebles que tienen nuestros datos.

Imagen 81 Dashboard datos procesados


Imagen 82 Diferentes filtros del dashboard


 
8.- CONCLUSIONES DEL MODELO PREDICTIVO
Analizados los datos recuperados de las fuentes de información (datos sin procesar) que han sido estudiados (datos procesados), correspondientes a los bienes inmuebles de la comunidad de Madrid, y cuyas distribuciones de precios se muestran a continuación, se observa la necesidad de tratar los datos para filtrar aquella información que entendemos es irrelevante.

DATOS SIN PROCESAR COMPRA –VENTA

Imagen 83 Relación precios venta por distritos de Madrid de datos sin procesar

DATOS PROCESADOS COMPRA -VENTA

Imagen 84 Relación precios venta por distritos de Madrid de datos procesados




 
DATOS SIN PROCESAR ALQUILER

Imagen 85 Relación precios alquiler por distritos de Madrid de datos sin procesar

DATOS PROCESADOS ALQUILER

Imagen 86 Relación precios alquiler por distritos de Madrid de datos procesados

Como se puede observar, no hemos limpiado todos los datos outliers, solo hemos realizado algunos filtros (ver módulo 3.3 Información de los datos).
Esto es debido a que, si realizábamos la limpieza de los mismos, como la distribución media de los datos pertenece a un par de distritos, se iban a borrar la gran mayoría de datos de los demás distritos, obteniendo posteriormente un modelo mucho peor.
Pensamos que para generar un modelo sin outliers, necesitamos tener una distribución de datos más equitativo entre los diferentes distritos.
También observamos que se debería de haber tenido otro tipo de variables a tomar en cuenta como, por ejemplo:
-	Estado del inmueble.
-	Años desde su construcción.
-	Localización exacta.
-	Cercanía a sector servicios (metro, centro salud, colegios, cercanías, zona de ocio).
-	Orientación del inmueble

Muchas de estas variables no son públicas o no están identificadas en la webpage de fotocasa. Por eso resulta muy difícil abarcar todas ellas a la hora de predecir.
Aun así, tras realizar una serie de predicciones sobre el modelo predictivo que hemos obtenido, creemos que con los datos que hemos trabajado, el pronóstico es muy cercano a la realidad.
Entre los modelos probados, el Gradient Boosting Regressor obtuvo el mejor rendimiento en ambos dataframes, donde produjo un validation score de 0.83 en compra-venta y un 0.75 en alquiler.
Este nivel de precisión es un resultado prometedor dada la heterogeneidad del conjunto de datos y los factores ocultos, incluidas las características extra de los propietarios, que eran imposibles de considerar.
Para comprobar el grado de exactitud de predicción hemos obtenido de nuestro csv preprocesado, varios ejemplos de compra-venta y alquiler. Hemos predicho usando las mismas características para ambos y las diferencias son las siguientes:



Imagen 87 Relación precios venta real vs predicción


Imagen 88 Relación precios alquiler real vs predicción 
9.- TRABAJOS FUTUROS
A la vista de los resultados obtenido tras todo el trabajo realizado, creemos que éste puede seguir evolucionando.
-	Mejorar el proceso de extracción de información.
Para ello, pensamos que llegar a una alianza con algún portal de compra-venta-alquiler de inmuebles puede venir bien, ya que la extracción de información en tiempo real de las mismas, es bastante complejo, al ser ésta información la base de negocio de las empresas que hemos utilizado como fuentes de información.
-	Introducción de variables adicionales para mejorar
A la vista de los resultados, observamos que hay muchas más variables a tener en cuenta y a ser estudiadas para mejorar la predicción del negocio del que estamos hablando, que con motivo de la inexperiencia y el tiempo que necesitábamos, no hemos abordado.
-	Mejorar precisión de algoritmos de modelado
Como se puede observar en el módulo 6.3.- CONSTRUIR MODELO en la Imagen 71, se puede realizar un ajuste de híperparámetros (Tuning) de los algoritmos que no tienen parámetros de Tuning.
Posteriormente se podría realizar un Voting. Éste es una técnica que se puede utilizar para mejorar el rendimiento del modelo, idealmente logrando un mejor rendimiento que cualquier modelo único utilizado en el conjunto. funciona combinando las predicciones de varios modelos. Puede usarse para clasificación o regresión. En el caso de la regresión, esto implica calcular el promedio de las predicciones de los modelos. En el caso de la clasificación, se suman las predicciones para cada etiqueta y se predice la etiqueta con el voto mayoritario.
-	Uso de redes neuronales
Utilización de un conjunto de algoritmos diseñados especialmente para reconocer patrones.
 
ANEXO I: INSTALACIÓN, CONFIGURACIÓN Y VERIFICACIÓN DE DOCKER
(Fuente: https://docs.docker.com/engine/install/ubuntu/)

INTALACION EN UBUNTU LINUX
1.	Iniciar una terminal y proceder a actualizar la lista de paquetes del sistema operativo disponibles:
$ sudo apt-get update
$ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

2.	Anadir la clave GPG oficial de Docker
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

3.	Instalar la última versión de Docker
$ sudo apt-get update
$ sudo apt-get install -y docker.io


INTALACION EN Windows

1.	Descargar el paquete de instalación para Windows:
https://www.docker.com/products/docker-desktop

Imagen 89 Web oficinal Docker

2.	Seguir los pasos del instalador
NOTA: En nuestro caso, se ha intentado instalar Docker en varias máquinas con sistema operativo Windows 10 y en ninguno de los casos el instalador se ha sido capaz de completarse correctamente

Instalación de BBDD SQL sobre Docker
1.	Crear la estructura de carpetas para la BBDD MySQL
$ sudo mkdir /home/proyecto
$ sudo mkdir /home/proyecto/bbdd

2.	Copiar los siguientes ficheros en el directorio /home/proyecto creado en el paso anterior
	“bk_db_proyecto_miriadax.sql”
	“comandosCreateDB”

Nota: Puede ayudarse del siguiente comando para realizar la copia
$ sudo cp <ruta_donde_tenga_el_fichero>/<nombre_fichero> /home/proyecto

 
3.	Instalar y arrancar la BBDD MySQL en la plataforma Docker
$ sudo docker run -d -p 3306:3306 --name mysql-db -e MYSQL_ROOT_PASSWORD=contraseña -v /home/proyecto/bbdd:/var/lib/mysql mysql

4.	Inicializar la BBDD MySQL db_proyecto_miriadax que utilizaremos
$ sudo docker exec -i mysql-db mysql --password=contraseña < commandos

5.	Instalar la BBDD MySQL db_proyecto_miriadax que utilizaremos
$ sudo docker exec -i mysql-db mysql -p db_proyecto_miriadax --password=contraseña < bk_db_proyecto_miriadax.sql

6.	Instalar y arrancar la BBDD MySQL en la plataforma Docker
$ sudo docker run -d -p 3306:3306 --name mysql-db -e MYSQL_ROOT_PASSWORD=contraseña -v /home/proyecto/bbdd:/var/lib/mysql mysql

Puede verificar que puede acceder correctamente de la siguiente manera:
1.	Acceder a la BBDD:
        $sudo docker exec -it mysql-db mysql -p

Imagen 90 Acceso a BBDD MySQL en Docker
 
2.	Visualizamos las BBDD de las que dispone:

Imagen 91 Visualización BBDD en MySQL
3.	Realizamos una consulta simple para ver su contenido:

Imagen 92 Visualización BBDD en MySQL






 
ANEXO II: FUENTES DE INFORMACIÓN ANALIZADAS
Listado de referencias consultadas para la definición de la información a tratar y aprendizaje del modelo de negocio por parte de los integrantes del presenta trabajo:
-	Evolución epidemiológica de Madrid por Distritos y semana
https://datos.comunidad.madrid/catalogo/dataset/covid19_tia_muni_y_distritos

-	Información estadística de la Comunidad de Madrid sobre precios de Viviendas
https://www.madrid.es/portales/munimadrid/es/Inicio/El-Ayuntamiento/Estadistica/Areas-de-informacion-estadistica/Edificacion-y-vivienda/Mercado-de-la-vivienda/Compra-venta-de-viviendas/?vgnextfmt=default&vgnextoid=9b8db9602f841510VgnVCM1000000b205a0aRCRD&vgnextchannel=22613c7ea422a210VgnVCM1000000b205a0aRCRD

https://www.madrid.es/portales/munimadrid/es/Inicio/El-Ayuntamiento/Estadistica/Areas-de-informacion-estadistica/Edificacion-y-vivienda/Mercado-de-la-vivienda/Precios-de-la-vivienda/?vgnextfmt=default&vgnextoid=bf281b47a277b210VgnVCM1000000b205a0aRCRD&vgnextchannel=22613c7ea422a210VgnVCM1000000b205a0aRCRD

-	Noticia de prensa de VozPopuli.com (Septiembre 2019)
https://www.vozpopuli.com/economia-y-finanzas/conoce-sueldo-vecino-herramienta-INE-renta-barrios_0_1281472270.html

-	Indicadores del Instituto Nacional de Estadística en base a renta, edad y nacionalidad
https://www.ine.es/experimental/atlas/experimental_atlas.htm
https://www.ine.es/experimental/atlas/exp_atlas_tab.htm#

-	Población estadística por municipios, sexo y edad
https://datos.gob.es/es/catalogo/ea0010587-altas-por-municipio-sexo-y-edad-estadistica-de-variaciones-residenciales-identificador-api-t20-p307-a2018-l0-a4_1-px

-	Población residente en España a 1 de enero por lugar de nacimiento y año. Anual
https://datos.gob.es/es/catalogo/ea0010587-poblacion-residente-en-espana-a-1-de-enero-por-lugar-de-nacimiento-y-ano-anual-comunidades-autonomas-proyecciones-de-poblacion-identificador-api-36679

-	Portal inmobiliario idealista.com
https://www.idealista.com/

-	Portal inmobiliario Fotocasa.es
https://www.fotocasa.es/es/









 
ANEXO III: SCRIPT CREACIÓN BASE DE DATOS MYSQL
DROP database if exists db_proyecto_miriadax;

create database db_proyecto_miriadax;
use db_proyecto_miriadax;

CREATE TABLE pisos (
  idInmueble int NOT NULL,
  urlInmueble varchar(500) DEFAULT null,
  fuenteInfo varchar(45) DEFAULT null,
  tipoInmueble int DEFAULT NULL,
  tipoOperacion int DEFAULT NULL,
  precio decimal(10,2) NOT NULL,
  habitaciones int DEFAULT NULL,
  tamano decimal(10,2) DEFAULT NULL,
  planta varchar(45) DEFAULT NULL,
  distrito varchar(45) DEFAULT NULL,
  ciudad varchar(45) DEFAULT NULL,
  fecha varchar(45) DEFAULT NULL,
  descripcion varchar(5000) DEFAULT null,
  eficienciaEnergetica varchar(1) DEFAULT null,
  ascensor BOOLEAN,
  terraza BOOLEAN,
  trastero BOOLEAN,
  garaje varchar(45) DEFAULT null,
  balcon BOOLEAN,
  aireAcondicionado BOOLEAN,
  piscina BOOLEAN,
  vendedor varchar(200) DEFAULT null,
  banios int NOT NULL
)

USE DB_PROYECTO_MIRIADAX;
CREATE INDEX IDX_PISOS_IDINMUEBLE ON PISOS (idInmueble);
