#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla
#a cuantas horas y minutos corresponde.
#Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

minutos = (int)(input("Dime los minutos "))

print(f" Los {minutos} minutos son: {int(minutos/60)} horas y {minutos%60} minutos")