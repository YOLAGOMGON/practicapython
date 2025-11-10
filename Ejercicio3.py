# Heladeria "Frosty" sabor y topping

chocolate=4000
vainilla = 3500
topping = "1000"

print ("Bienbenidos heladeria Frosty")

sabordehelado=  input ("sabor de healdo que desea  :")


if sabordehelado == "chocolate" :
    print ("sabor elegido chocolate valor:. ", chocolate)

    adiccioneschocolate = input ("desea adiciones topping por valor de "  + topping +  " si O no"  )
    
    if adiccioneschocolate  == "si" :
        print ("valor a pagar helado mas topping",chocolate + 1000 ) 

    else : 
        print ("valor a pagar helado de chocolate",chocolate )

elif sabordehelado == "vainilla" :
    print ("sabor elegido vainilla valor:.", vainilla)

    adiccionesvainilla = input ("desea adicioanr topping por valor de " + topping + "si o no")

    if adiccionesvainilla == "si":
        print("valor a pagar helado mas topping",vainilla + 1000)

    else :
        print ("valor a pagar helado vainilla", vainilla)

else:
    print ("Error, sabor invalido, por favor ingresa entre vainilla y chocolate")
