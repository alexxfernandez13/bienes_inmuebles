# bienes_inmuebles
> ``* Es IMPORTANTE guardar el proyecto en la carpeta C:\ del PC puesto 
que todos los aplicativos estan configuardos para leer de ese PATH``

## CONFIGURACION/INSTALACION CODIGO FUENTE
======================= DESCARGAR PYCHARM ==============================
> ``https://www.jetbrains.com/es-es/pycharm/download/#section=windows`` (Version Community)

======================= PATH PROYECTO ==================================
> ``Colocar Proyecto (root folder bienes_inmuebles) en: C:\``

======================= CONFIGURAR VARIABLES DE ENTORNO ================
> ``Abrir la pantalla de variables de entorno: Windows –> escribir “variables de entorno” –> 
Opciones Avanzadas –> Variables de Entorno``

> ``Cambiar/crear nueva variable: nueva variable –> Nombre de la variable (“PYTHONPATH”) 
y Valor de la variable (ruta de la root folder del proyecto)`` (C:\bienes_inmuebles)

======================= ABRIR PROYECTO CON PYCHARM =====================
> ``file –> open`` (C:\bienes_inmuebles)

======================= CONFIGURAR EJECUCIONES =========================
> ``run –> edit configurations`` 

> ``click en + –> python``(Añadir configuracion Nueva: son 4 en total)

> ``script path: C:\bienes_inmuebles\bienes_inmuebles\preprocesar\main.py`` (1ª Ejecucion)

> ``script path: C:\bienes_inmuebles\bienes_inmuebles\preprocesar\main.py`` (2ª Ejecucion)

> ``script path: C:\bienes_inmuebles\bienes_inmuebles\machine_learning\main.py`` (3ª Ejecucion)

> ``script path: C:\bienes_inmuebles\bienes_inmuebles\machine_learning\comprobacion_prediccion.py`` (4ª Ejecucion)

> ``script path: C:\bienes_inmuebles\bienes_inmuebles\machine_learning\main.py`` (Tests)

## INSTALAR PROYECTO DESDE CLIENTE
======================= SOURCE CODE ====================================
> ``Entrar en terminal: entrar en root folder del proyecto descargado –> 
Para instalar: python setup.py install –> Ir a C:/: cd .. –> 
Ejecución: pyhton -m bienes_inmuebles/main.py`` 

======================= PYPI ===========================================
> ``pip install “nombre proyecto” –> Ir a C:/: cd .. –> 
Ejecución: python -m bienes_inmuebles.machine_learning.main`` (Permite ejecutar desde cualquier ruta poniendo -m)

======================= CONDA ==========================================
> ``terminal anaconda: conda install -c -c alexxfernandez13 bienes_inmuebles –> yes/y ->
Ejecución: python -m bienes_inmuebles.machine_learning.main``

## CONFIGURACION/INSTALACION DASHBOARD
======================= POWER BI DESKTOP ===============================
> ``https://www.microsoft.com/es-ES/download/details.aspx?id=58494``
> ``Doble click en el fichero: Dashboard Bienes Inmuebles.pbix``


> ``set PYTHONPATH="/path/to/bienes_inmuebeles`` (Windows)

> ``export PYTHONPATH="/path/to/bienes_inmuebeles`` (Linux & MAC)

> ``python bienes_inmuebeles/main.py`` 
