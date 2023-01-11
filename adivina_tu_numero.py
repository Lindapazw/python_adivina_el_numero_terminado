import random

def adivina_el_numero(x):

    print("************************")
    print(" Bienvenido(a) al juego ")
    print("************************")
    print(" tu meta es adivinar el número generado por la computadora.")

    numero_aleatoreo = random.randint(1,x) # número aleatoreo entre 1 y x

    predicción = 0 

    while predicción != numero_aleatoreo:
        # el usuario ingresa un numero
        predicción = int(input(f"Adivina el número entre 1 y {x}: ")) # f-string

        if predicción < numero_aleatoreo:
            print("Intenta otra vez. Este número es muy pequeño.")
        elif predicción > numero_aleatoreo:
            print("Intenta otra vez. Este número es muy grande.")

    print(f"¡Felicitaciones! adivinaste el número {numero_aleatoreo} correctamente.")