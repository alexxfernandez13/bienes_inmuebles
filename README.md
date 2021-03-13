# bienes_inmuebles
> ``* Es IMPORTANTE guardar el proyecto en la carpeta C:\ del PC puesto 
que todos los aplicativos estan configuardos para leer de ese PATH``

## CONFIGURACION / INSTALACION CODIGO FUENTE
======================= DESCARGAR PYCHARM ==============================
> ``https://www.jetbrains.com/es-es/pycharm/download/#section=windows`` (Version Community)
>
> ``Al instalar marcar con un check todas las opciones -> Seleccionar reboot now -> 
confirmar acuerdo privavidad no mandar datos anonimos``

======================= PATH PROYECTO ==================================
> ``Colocar Proyecto en: C:\ ``  (root folder bienes_inmuebles)

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

> ``script path: C:\bienes_inmuebles\bienes_inmuebles\preprocesar\main.py`` (Preprocesamiento)

> ``script path: C:\bienes_inmuebles\bienes_inmuebles\machine_learning\main.py`` (Prediccion ML)

> ``script path: C:\bienes_inmuebles\bienes_inmuebles\machine_learning\comprobacion_prediccion.py`` (Test Prediccion Correcta/Fiable)

> ``script path: C:\bienes_inmuebles\bienes_inmuebles\machine_learning\main.py`` (Tests)

## INSTALAR PROYECTO DESDE CLIENTE
======================= SOURCE CODE ====================================
> ``Entrar en terminal: entrar en root folder del proyecto descargado –> 
Para instalar: python setup.py install –> Ir a C:/: cd .. –> 
Ejecución: python -m bienes_inmuebles.machine_learning.main``

> ``python setup.py install --user || exit 1``(Si da error la instalacion por los permisos)
> ``Instalar Pyhton 3.8 desde Microsoft (Si da error por Python, este caso no es habitual)

======================= PYPI ===========================================
> ``pip install “nombre proyecto” –> Ir a C:/: cd .. –> 
Ejecución: python -m bienes_inmuebles.machine_learning.main`` (Permite ejecutar desde cualquier ruta poniendo -m)

======================= CONDA ==========================================
> ``terminal anaconda: conda install -c -c alexxfernandez13 bienes_inmuebles –> yes/y ->
Ejecución: python -m bienes_inmuebles.machine_learning.main``

## CONFIGURACION/INSTALACION DASHBOARD
======================= POWER BI DESKTOP ===============================
> ``https://www.microsoft.com/es-ES/download/details.aspx?id=58494``
> ``Abrir Dashboard: Doble click en el fichero: Dashboard Bienes Inmuebles.pbix``
> ``Abrir enlace web: https://app.powerbi.com/view?r=eyJrIjoiZWVmZmZhZjItZGUyNy00NTI4LThiMDYtZTEyZGI3YmM4NTA3IiwidCI6ImIxNmI2NzE1LTUzZTItNGUxZi04YjEyLWRjNTBhMzdiM2EzMyIsImMiOjl9``
