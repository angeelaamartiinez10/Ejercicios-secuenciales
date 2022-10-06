#Un alumno desea saber cual será su calificación final en la materia de Algoritmos.
# Dicha calificación se compone de los siguientes porcentajes

#55% del promedio de sus tres calificaciones parciales.
#30% de la calificación del examen final.
#15% de la calificación de un trabajo final.

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




