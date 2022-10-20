#FUNCION
#Escribir un programa que pregunte al usuario su nombre, y luego lo salude.

print("EJERCICIO 1: DAR UN NOMBRE")
def ejer1():
    nombre=""
    nombre=input("¿Cúal es tu nombre? ")
    print("tu nombre es:" ,nombre,)
ejer1()

print("EJERCICIO 2: AREA")
def ejer2():
    base=0
    altura=0
    base=(int)(input("¿Cúanto mide la base? "))
    altura=(int)(input("¿Cúanto mide la altura? "))
    print("El área es: " ,base * altura, )
ejer2()

print("EJERCICIO 3: HIPOTENUSA")
def ejer3():
    from math import sqrt
    cat1=0
    cat2=0
    cat1=(int)(input("¿Cúanto mide el primer cateto? "))
    cat2=(int)(input("¿Cúanto mide el segundo cateto? "))
    print("La hipotenusa del triángulo rectángulo: " ,sqrt(cat1**2+cat2**2 ),  )
ejer3()

print("EJERCICIO 4: CALCULADORA +-*/")
def ejer4():
    num1=0
    num2=0
    num1=(int)(input("¿cuál es tu primer número? "))
    num2=(int)(input("¿cuál es tu segundo número? "))
    print("Estas son las operaciones posibles: suma=" ,num1+num2,  "resta=",num1-num2, "multiplicación=",num1*num2, "división=",num1/num2, )
ejer4()

print("EJERCICIO 5: GRADOS CELSIUS")
def ejer5():
    grados=0
    grados=(int)(input("¿Cuál es la temperatura en grados Fahrenheit? "))
    print("La temperatura en grados Celsius: " ,(grados-32)*5/9, "°C")
ejer5()

print("EJERCICIO 6: MEDIA DE 3 NUMEROS")
def ejer6():
    num1 = 0
    num2 = 0
    num3 = 0
    num1=(int)(input("Dime el primer numero "))
    num2=(int)(input("Dime el segundo numero "))
    num3=(int)(input("Dime el tercer numero "))
    print("La media de tus numeros" ,(num1+num2+num3)/3,)
ejer6()

print("EJERCICIO 7: CONVERSION DE MINUTOS A HORAS")
def ejer7():
    minutos = (int)(input("Dime los minutos "))
    print(f" Los {minutos} minutos son: {int(minutos/60)} horas y {minutos%60} minutos")
ejer7()

print("EJERCICIO 8: SUELDO TOTAL")
def ejer8():
    sueldo = 0
    venta1 = 0
    venta2 = 0
    venta3 = 0
    venta1=(int)(input("Gasto en la venta 1.: "))
    venta2=(int)(input("Gasto en la venta 2.: "))
    venta3=(int)(input("Gasto en la venta 3.: "))
    print("El total de tus ventas + comisión= " ,(venta1+venta2+venta3)*1.1, "€")
    sueldo=(int)(input("El total que recibes este mes "))
    print("El total que recibirás este mes= ",(venta1+venta2+venta3)*1.1+sueldo, "€")
ejer8()

print("EJERCICIO 9: DESCUENTO")
def ejer9():
    precio = 0
    precio=(int)(input("¿Cuánto llevas gastado?"))
    print("El precio total con el descuento del 15%= ",precio-(precio*0.15)," €")
ejer9()

print("EJERCICIO 10: CALIFICACION FINAL")
def ejer10():
    c1 = 0
    c2 = 0
    c3 = 0
    ex = 0
    tra = 0
    c1=(int)(input("¿Cúal es la nota de tu primer parcial? "))
    c2=(int)(input("¿Cúal es la nota de tu segundo parcial? "))
    c3=(int)(input("¿Cúal es la nota de tu tercer parcial? "))
    ex=(int)(input("¿Cúal es la nota de tu examen final? "))
    tra=(int)(input("¿Cúal es la nota de tu trabajo? "))
    print("Califiacaion final= " ,(((c1+c2+c3)/3)*0.55)+(ex*0.3)+(tra*0.15),)
ejer10()

print("EJERCICIO 20: TOTAL DE DINERO")
def ejer20():
    mon2e = 0
    mon1e = 0
    mon05e = 0
    mon01e = 0
    mon02e = 0
    mon2e = (int)(input("¿Cuántas monedas de 2€ tiene? " ))
    mon1e = (int)(input("¿Cuántas monedas de 1€ tiene? " ))
    mon05e = (int)(input("¿Cuántas monedas de 50 centimos tiene? "))
    mon01e = (int)(input("¿Cuántas monedas de 10 centimos tiene? "))
    mon02e = (int)(input("¿Cuántas monedas de 20 centimos tiene? "))
    print("El total de dineros que tienes" ,(mon1e*1)+(mon02e*2)+(mon05e*0.50)+(mon01e*0.10)+(mon02e*0.20),"€"  )
ejer20()
