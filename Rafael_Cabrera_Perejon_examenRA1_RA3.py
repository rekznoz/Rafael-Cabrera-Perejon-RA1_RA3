
import os

def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def VerNumero(Dato):
    # Verificacion de si el objeto puede convertirse a numero
    try:
        int(Dato)
        return True
    except ValueError:
        return False

def Encabezado():
    # Encabezado de la aplicacion
    Clear()
    print("* "*20)
    print("PROGRAMA DE GENERACION DE TABLAS RAFAEL CABRERA PEREJON")
    print("- "*20)

def Errores(Dato):
    # Impresion de errores
    print(Dato)
    print("- "*20)
    print("* "*20)

def NumeroPar(Dato):
    # Verificacion de Numero Par
    if Dato % 2 == 0:
        return True
    else:
        return False

def EdadValida(Dato):
    # Entrada de Edad Valida
    if (Dato > 10 and Dato <= 12) or (Dato > 8 and Dato <= 10) or (Dato >= 6 and Dato <= 8):
        return True
    else:
        return False

def MesValido(Dato):
    # Entrada de Edad Valida
    if (Dato > 0 and Dato <= 12):
        return True
    else:
        return False

def GeneradordeTablas(Dato):
    # Generador de tablas de multiplicacion
    for x in Dato:
        print("- "*20)
        print("TABLA DEL",x)
        print("* "*8)
        for Numero in range (1,11):
            Calculo = x * Numero
            print(str(x) + " x " + str(Numero) + " = " + str(Calculo))
        print()

def VerificacionEdadMes(Dato1,Dato2):
    # Se compara la edad y el mes con los rangos
    if Dato1 >= 11 and Dato1 <= 12:
        return (11,12,13)
    elif Dato1 > 8 and Dato1 <= 10:
        if NumeroPar(Dato2):
            return (6,8,10)
        else:
            return (7,9)
    elif Dato1 >= 6 and Dato1 <= 8: 
        if NumeroPar(Dato2):
            return (2,4)
        else:
            return (1,3,5)
    else:
        # Impresion de error por cualquier problema no implementado
        Errores("Error inesperado!")
    
if __name__ == "__main__":

    Encabezado()

    while True:
        # Aqui pregunto la edad
        Edad = input('Edad ')
        if VerNumero(Edad):
            Edad = int(Edad)
            if EdadValida(Edad):
                # Se verifica que tanto el caracter como la Edad son validos
                Encabezado()
                print("Edad",Edad,'Se encuentra dentro del rango')
                # Aqui pregunto el mes
                Mes = input('Mes ')
                if VerNumero(Mes):
                    Mes = int(Mes)
                    if MesValido(Mes):
                        # Se verifica que tanto el caracter como la Mes son valido
                        # Y depues se compara para crear un cambio en una impresion
                        if NumeroPar(Mes):
                            MesParImpar = 'Par'
                        else:
                            MesParImpar = 'Impar'

                        Encabezado()
                        print("Edad",Edad,'Se encuentra dentro del rango')
                        print("Mes",Mes,'El mes es ' + MesParImpar + 'Tablas',VerificacionEdadMes(Edad,Mes))
                        GeneradordeTablas(VerificacionEdadMes(Edad,Mes))

                    else:
                        # Impresion de Errores al poner el Mes
                        Encabezado()
                        Errores("Mes " + str(Mes) + " El mes es erroneo.")
                else:
                    # Impresion de Errores al poner letras en el Mes
                    Encabezado()
                    print("\nAVISO. \nSolo se pueden ingresar numeros\n")
            else:
                # Impresion de Errores al poner la Edad
                Encabezado()
                Errores("Edad " + str(Edad) + " No se contempla esta edad.")
        else:
            # Impresion de Errores al poner una letra en la Edad
            Encabezado()
            print("\nAVISO. \nSolo se pueden ingresar numeros\n")
