def menuPrincipal():
    print("********* Operaciones con conjuntos  *********")
    print(" 0- Salir")
    print(" 1- Union")
    print(" 2- Interseccion")
    print(" 3- Diferencia")
    print(" 4- Diferencia Simétrica")
    return leerEnteromenu(">>> Ingrese una opcion: ")

def leerEntero(mensaje):
    contador = 0
    while contador < 3:
        try:
            return int(input(mensaje))
            # break;
        except:
            print(": Entero no válido..")
            contador = contador + 1
    print("Usted exedió los intentos validos, regresará al menu conjuntos")
    print("")
    print("Binevenido a opercaiones con conjuntos")
    return leerConjunto()

def leerEnteromenu(mensaje):
    contador = 0
    while contador < 3:
        try:
            return int(input(mensaje))
            # break;
        except:
            print(": Entero no válido..")
            contador = contador + 1
    print("Usted exedió los intentos validos, regresará al menu conjuntos")
    print("")
    print("Vinevenido a opercaiones con conjuntos")
    return menuPrincipal()
# def leerConjunto():
#
#     conj = []
#     numElementos = leerEntero("  Ingrese el numero de elementos: ")
#
#     for i in range(numElementos):
#         elem = leerEntero(f"Ingrese el elemento {i+1}: ")
#         conj.append(elem)
#     return  conj

def leerConjunto():
    conj = []
    numElementos = leerEntero("Ingrese el número de elementos: ")

    for i in range(numElementos):
        elem = leerEntero(f"Ingrese el elemento {i+1}: ")
        if elem not in conj:
            conj.append(elem)
        else:
            print("El elemento ya existe en el conjunto.")
            return leerConjunto()
    return conj


def unir(conj1, conj2):
    union = list(conj1)
    for elem in conj2:
        if elem not in conj1:
            union.append(elem)
    return union


def diferencia(conj1, conj2):
    difer = []
    for elem in conj1:
        if elem not in conj2:
            difer.append(elem)
    return difer

def diferenciaSimétrica(conj1, conj2):
    diferSim = []
    for elem in conj1:
        if elem not in conj2:
            diferSim.append(elem)
    for elem in conj2:
        if elem not in conj1:
            diferSim.append(elem)
    return diferSim

def interseccion(conj1, conj2):
    inter = []
    for elem in conj1:
        if elem in conj2:
            inter.append(elem)
    return inter

def main():
    conj1 = leerConjunto()
    conj2 = leerConjunto()
    opcion = menuPrincipal()
    while opcion != 0:
        if opcion == 1:
            print(f"la Unión de conjunto A {conj1} y conjunto B {conj2} es {unir(conj1,conj2)}")
        elif opcion == 2:
            print(f"la Interseccion de conjunto A {conj1} y conjunto B {conj2} es {interseccion(conj1,conj2)}")
        elif opcion == 3:
            print(f"la Diferencia de conjunto A {conj1} y conjunto B {conj2} es {diferencia(conj1,conj2)}")
        elif opcion == 4:
            print(f"la Diferencia Simétrica de conjunto A {conj1} y conjunto B {conj2} es {diferenciaSimétrica(conj1,conj2)}")
        else:
            print(" Error: opción inválida.")
        opcion = menuPrincipal()

main()