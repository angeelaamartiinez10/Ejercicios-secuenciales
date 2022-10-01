#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

from math import sqrt


cat1=0
cat2=0


cat1=(int)(input("¿Cúanto mide el primer cateto? "))
cat2=(int)(input("¿Cúanto mide el segundo cateto? "))
print("La hipotenusa del triángulo rectángulo: " ,sqrt(cat1**2+cat2**2 ),  )
