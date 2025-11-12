
while True : 
    nombre = str (input("nombre del producto"))
    if nombre == "" or not nombre.isalpha():
        print ("Ingrese nombre del producto ")
        continue
    else :
     print (f"nombre del producto {nombre} agragado correctamente")
     break



while True :
    try:
        precio = float (input ("precio"))
        if precio <= 0 :
            print ("Ingrese precio del producto ")
        else :
            print (f"precio del producto {precio} agragado correctamente")
        break
    except ValueError:
        print("Ingrese precio del producto ")


while True :
    try: 
        cantidad =int (input ("cantidad"))
        if cantidad <= 0:
            print ("Ingrese cantidad del producto ")
        else :
            print (f"cantidad del producto {precio} agragado correctamente")
            break
    except ValueError:
        print ("Ingrese cantidad del producto ")

