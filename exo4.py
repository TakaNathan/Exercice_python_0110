#Exercice4
from math import sqrt

def calcul_surface_triangle(cote1,cote2,cote3) :
    #Calcul de la surface du triangle
    #(float,float,float)->(float)

    # p designe le perimetre
    p = cote1+cote2+cote3
    surface = sqrt(p*(p-2*cote1)*(p-2*cote2)*(p-2*cote3))/4
    return surface

#test de calcul de la surface du triangle avec 3,3 et 4
print("La surface est : ",calcul_surface_triangle(3,3,4))