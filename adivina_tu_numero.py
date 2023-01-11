import random

def adivina_el_numero(x):

    print("************************")
    print(" Bienvenido(a) al juego ")
    print("************************")
    print(" tu meta es adivinar el número generado por la computadora.")

    numero_aleatoreo = random.randint(1,x) # número aleatoreo entre 1 y x