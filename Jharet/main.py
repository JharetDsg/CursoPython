def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def divicion(a,b):
    if b == 0:
        print("No se puede realizar la operacion por 0")
        return
    return a/b

switcher = {
    # 0: Salir,
    1: suma,
    2: resta,
    3: multiplicacion,
    4: divicion
}
try:
    opcion = int(input("Ingrese una opcion: "))
    funcion = switcher.get(opcion)
    if funcion:
        n1 = float(input("Ingrese el primer número: "))
        n2 = float(input("Ingrese el segundo número: "))
        print("El resultado es:", funcion(n1, n2))
    else:
        print("Opción inválida. Intente de nuevo.")
except ValueError:
    print("Error")



# opcion = None
# while opcion != 0:
#     print("""
#     0 Salir
#     1 Sumar
#     2 Restar
#     3 Multiplicar
#     4 Dividir
#     """)
#     opcion = input("Seleccione una opción: ")
#     try:
#         opcion = int(opcion)
#         if opcion == 0:
#             break
#         elif opcion > 4 or opcion < 0:
#             print("Opción inválida. Intente de nuevo.")
#             continue
#         else:
#             if opcion == 1:
#                 print("Escojio la opcion de sumar")
#                 n1 = int(input("Ingrese el primer número: "))
#                 n2 = int(input("Ingrese el segundo número: "))
#                 print("El resultado de la suma es:", suma(n1, n2))
#             elif opcion == 2:
#                 print("Escojio la opcion de restar")
#                 n1 = float(input("Ingrese el primer número: "))
#                 n2 = float(input("Ingrese el segundo número: "))
#                 print("El resultado de la resta es:", resta(n1, n2))
#             elif opcion == 3:
#                 print("Escojio la opcion de multiplicar")
#                 n1 = float(input("Ingrese el primer número: "))
#                 n2 = float(input("Ingrese el segundo número: "))
#                 print("El resultado de la multiplicacion es:", multiplicacion(n1, n2))
#             elif opcion == 4:
#                 print("Escojio la opcion de dividir")
#                 n1 = float(input("Ingrese el primer número: "))
#                 n2 = float(input("Ingrese el segundo número: "))
#                 print("El resultado de la divicion es:", divicion(n1, n2))
#     except ValueError:
#         print("Entrada inválida. Intente de nuevo con un número.")