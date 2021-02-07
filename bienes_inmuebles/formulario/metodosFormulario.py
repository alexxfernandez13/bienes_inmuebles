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
        self.maxHabitaciones = 20
        self.maxPlantas = 16
        self.maxMetros = 999999
        self.maxBaños = 20


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


    def formulario (self):

        objetoForm = ObjetoFormulario()

        tipoOperacion = self.getOpcion(self.listaOperaciones, "¿Que TIPO de OPERACION tiene pesando realizar?")
        if tipoOperacion=='Comprar':
            objetoForm.setTipoOperacion(1)
        elif tipoOperacion=='Alquiler':
            objetoForm.setTipoOperacion(2)

        distrito = self.getOpcion(self.listaDistritos, "¿En qué DISTRITO se encuentra la vivienda?")
        objetoForm.setDistrito("distrito_" + distrito)

        objetoForm.setHabitaciones(self.getNumero("¿Cuantos HABITACIONES tiene la vivienda?,", self.maxHabitaciones))

        objetoForm.setPlanta(self.selfgetNumero("¿En qué PLANTA esta la vivienda?", self.maxPlantas))

        objetoForm.setTamano(self.getNumero("¿Cuantos METROS CUADRADOS tiene la vivienda?", self.maxMetros))

        objetoForm.setBanos(self.getNumero("¿Cuantos BAÑOS tiene la vivienda?", self.maxBaños))

        terraza = self.getSIoNO("TERRAZA")
        if terraza=='s' or terraza=='S':
            objetoForm.setTerraza(1)
        elif terraza=='n' or terraza=='N':
            objetoForm.setTerraza(0)


        trastero = self.getSIoNO("TRASTERO")
        if trastero=='s' or trastero=='S':
            objetoForm.setTrastero(1)
        elif trastero=='n' or trastero=='N':
            objetoForm.setTrastero(0)

        garaje = self.getSIoNO("GARAJE")
        if (garaje == 's'):
            garaje = self.getOpcion(self.listaOpcionesGarage, "¿Qué TIPO de GARAJE tiene?")

        balcon = self.getSIoNO("BALCON")
        if balcon=='s' or balcon=='S':
            objetoForm.setBalcon(1)
        elif balcon=='n' or balcon=='N':
            objetoForm.setBalcon(0)

        aireAcondicionado = self.getSIoNO("AIRE ACONDICIONADO")
        if aireAcondicionado=='s' or aireAcondicionado=='S':
            objetoForm.setAireAcondicionadoa(1)
        elif aireAcondicionado=='n' or aireAcondicionado=='N':
            objetoForm.setAireAcondicionadoa(0)

        piscina = self.getSIoNO("PISCINA")
        if piscina=='s' or piscina=='S':
            objetoForm.setAireAcondicionado(1)
        elif piscina=='n' or piscina=='N':
            objetoForm.setAireAcondicionado(0)

    if __name__ == "__main__":