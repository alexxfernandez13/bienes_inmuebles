from colorama import Fore, Back, Style
from bienes_inmuebles.formulario.objetoFormulario import ObjetoFormulario

class MetodosFormulario():

    def __init__(self):
        self.listaDistritos = ["arganzuela", "barajas", "carabanchel", "centro", "chamartin", "chamberi", "ciudad-lineal",
                          "fuencarral", "hortaleza", "latina", "moncloa", "moratalaz", "puente-de-vallecas", "retiro",
                          "salamanca", "san-blas", "tetuan", "usera", "vicalvaro", "villa-de-vallecas", "villaverde",
                          "vicalvaro"]
        self.listaEficiencias = ["eficienciaEnergetica_A", "eficienciaEnergetica_B", "eficienciaEnergetica_C"]
        self.listaOperaciones = ["Comprar", "Alquiler"]
        self.listaOpcionesGarage = ["garaje-comunitario", "garaje-No-detallado", "garaje-Privado"]


    def getSIoNO(objetoPreguntado):
    dato = input("¿La vivienda tiene " + objetoPreguntado + "? (s)si - (n)no \n> ").lower()
    while (dato != 's' and dato != 'n'):
        print(Style.RESET_ALL)
        print(Back.YELLOW + "El dato introducido no es valido. Intentelo otra vez")
        print(Style.RESET_ALL)
        dato = input("La vivienda tiene " + objetoPreguntado + "? (s)si - (n)no\n> ").lower()

    return (dato)

    def getNumero(consulta, numeroMaximo):
        dato = input(consulta + "\n> ")
        if (dato.isnumeric()):
            dato = int(dato)
        else:
            dato = -1

        while (dato < 0 or dato > numeroMaximo):
            print(Style.RESET_ALL)
            print(Back.YELLOW + "El dato introducido no es valido. Intentelo otra vez")
            print(Style.RESET_ALL)

            dato = input(consulta + "\n> ").lower()
            if (dato.isnumeric()):
                dato = int(dato)
            else:
                dato = -1
        return (dato)

    def getOpcion(listaElementos, consulta):
        x = 1
        for elemento in listaElementos:
            print("(" + str(x) + ")" + elemento)
            x += 1

        opcion = input(consulta + "\n> ")
        if (opcion.isnumeric()):
            opcion = int(opcion)
        else:
            opcion = -1

        while (opcion < 0 or opcion > len(listaElementos)):
            print(Style.RESET_ALL)
            print(Back.YELLOW + "El dato introducido no es valido. Intentelo otra vez")
            print(Style.RESET_ALL)

            opcion = input(consulta + "\n> ")

            if (opcion.isnumeric()):
                opcion = int(opcion)
            else:
                opcion = -1

        return (listaElementos[opcion - 1])


    def formulario ():

        objetoForm = ObjetoFormulario()

        tipoOperacion = getOpcion(listaOperaciones, "¿Que TIPO de OPERACION tiene pesando realizar?")

        distrito = getOpcion(listaDistritos, "¿En qué DISTRITO se encuentra la vivienda?")
        distrito = "distrito_" + distrito

        habitaciones = getNumero("¿Cuantos HABITACIONES tiene la vivienda?,", maxHabitaciones)

        planta = getNumero("¿En qué PLANTA esta la vivienda?", maxPlantas)

        tamano = getNumero("¿Cuantos METROS CUADRADOS tiene la vivienda?", maxMetros)

        banos = getNumero("¿Cuantos BAÑOS tiene la vivienda?", maxBaños)

        eficiencia = getOpcion(listaEficiencias, "¿Qué EFICIENCIA energetica tiene la vivienda")

        ascensor = getSIoNO("ASCENSOR")

        terraza = getSIoNO("TERRAZA")

        trastero = getSIoNO("TRASTERO")

        garaje = getSIoNO("GARAJE")
        if (garaje == 's'):
            garaje = getOpcion(listaOpcionesGarage, "¿Qué TIPO de GARAJE tiene?")

        balcon = getSIoNO("BALCON")

        AireAcondicionado = getSIoNO("AIRE ACONDICIONADO")

        piscina = getSIoNO("PISCINA")


    if __name__ == "__main__":