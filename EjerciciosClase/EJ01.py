def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    return a / b
def validaCero(divisor):
    if (divisor == 0):
        print("Error: El divisor no puede ser cero.")
        return leerEntero("  Nuevo divisor (0 para salir):")
    else:
        return divisor

def leerEntero(mensaje):
    contador = 0
    while contador < 3:
        try:
            return int(input(mensaje))
            # break;
        except:
            print(": Entero no válido..")
            contador = contador + 1
    print("Usted exedió los intentos validos, regresará al menu")
    print("")
    return None

def menu():
    print("0- Salir")
    print("1- suma")
    print("2- resta")
    print("3- multiplicacion")
    print("4- division")
    return leerEntero("  >> Ingrese una opcion:")


def main():
    while True:
        opcion = menu()
        print("Opcion = ", opcion)
        if (opcion == 0):
            break
        else:
            match(opcion):
                case 1:
                    num1 = leerEntero("Num1: ")
                    if num1 is None:
                        print("Valor no válido")
                        continue
                    num2 = leerEntero("Num2: ")
                    if num2 is None:
                        print("Valor no válido")
                        continue
                    print("la resultado de Num1 y Num2 es de:",suma(num1,num2))
                case 2:
                    num1 = leerEntero("Num1: ")
                    if num1 is None:
                        print("Valor no válido")
                        continue
                    num2 = leerEntero("Num2: ")
                    if num2 is None:
                        print("Valor no válido")
                        continue
                    print("la resultado de Num1 y Num2 es de:", resta(num1, num2))
                case 3:
                    num1 = leerEntero("Num1: ")
                    if num1 is None:
                        print("Valor no válido")
                        continue
                    num2 = leerEntero("Num2: ")
                    if num2 is None:
                        print("Valor no válido")
                        continue
                    print("El resultado de Num1 y Num2 es de:", multiplicacion(num1, num2))
                case 4:
                    # num1 = validaCero(leerEntero("Num1: "))
                    num1 = leerEntero("Num1: ")
                    if num1 is None:
                        print("Valor no Válido")
                        continue
                    num2 = validaCero(leerEntero("Num2: "))
                    if num2 is None:
                        print("Valor no Válido")
                        continue
                    if (num2 != 0):
                        print(division(num1, num2))
                    else:
                        print("El divisor sigue siendo cero. Regresando al menu.")

main()