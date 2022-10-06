#Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos)
#después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).

mon2e = 0
mon1e = 0
mon05e = 0
mon01e = 0
mon02e = 0

mon2e = (int)(input("¿Cuántas monedas de 2€ tiene? " ))
mon1e = (int)(input("¿Cuántas monedas de 1€ tiene? " ))
mon05e = (int)(input("¿Cuántas monedas de 50 centimos tiene? "))
mon01e = (int)(input("¿Cuántas monedas de 10 centimos tiene? "))
mon02e = (int)(input("¿Cuántas monedas de 20 cnetimos tiene? "))

print("El total de dineros que tienes" ,(mon1e*1)+(mon02e*2)+(mon05e*0.50)+(mon01e*0.10)+(mon02e*0.20),"€"  )
