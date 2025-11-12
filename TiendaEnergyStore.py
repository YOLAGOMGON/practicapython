#SIMULADOR DE PUNTOS

def calcular_puntos():
    numero = int(input("ingrese el numero que desee"))
    puntos = 0
    for i in range (numero):
        if i % 3==0:
            puntos = puntos + 10
            print (i,"SE AGREGAN 10 PUNTOS")
        else:
            puntos = puntos + 5
            print (i,"SE AGREGAN 5 PUNTOS")

    print(f"puntos totales { puntos}")



calcular_puntos()





