from math import sqrt

#Exercice1

def division_entier_modulo() :
     #affiche le resultat et le module de la
     #divison entiere de 2 nombres
    dividende = int(input("Entrez le premier nombre : "))
    diviseur = int(input("Entrer le deuxieme nombre : "))
    
        #quotient et modulo sont variables globales
        #quotient retourne le resultat de la division entiere
    
    print("le resultat la division entiere de",dividende,"par",diviseur,"est",dividende//diviseur)
    print("le reste la division de",dividende,"par",diviseur,"est",dividende%diviseur)

#division_entier_modulo()

#Exercice2
#titre de l'exercice
print("EXERCICE2")

def celsius_en_fahrenheit(temp_Celsius) :
    #Transform la temperature de Celsius en Fahrenheit
    #(float)->(float)
    #˚F=˚C(9/5)+32
    temp_Fahrenheit = (temp_Celsius * 9/5) + 32
    return temp_Fahrenheit

#t_fahrenheit et t_celsius sont des variables globales
#on teste avec 0˚C
t_celsius = 0
t_fahrenheit = celsius_en_fahrenheit(t_celsius)
print(t_celsius,"˚C correspond a",t_fahrenheit,"˚F")

#on teste avec 100˚C
t_celsius = 100
t_fahrenheit = celsius_en_fahrenheit(t_celsius)
print(t_celsius,"˚C correspond a",t_fahrenheit,"˚F")

#Exercice3
#titre de l'exercice
print("EXERCICE3")

def calcule_note_finale(devoirsMoyenne,partiel,examen) :
    #Calcul de la note finale a partir des 3 notes donnees
    #(float,float,float)->(float)
    
    note_finale = devoirsMoyenne*25/100 + partiel*25/100 + examen*50/100
    return note_finale

#on teste avec 80,70,90
note_finale = calcule_note_finale(80,70,90)
print("La note finale est :",note_finale)


#Exercice4
#titre de l'exercice
print("EXERCICE4")

def calcul_surface_triangle(cote1,cote2,cote3) :
    #Calcul de la surface du triangle
    #(float,float,float)->(float)

    # p designe le perimetre
    p = cote1+cote2+cote3
    surface = sqrt(p*(p-2*cote1)*(p-2*cote2)*(p-2*cote3))/4
    return surface

#test de calcul de la surface du triangle avec 3,3 et 4
print("La surface est : ",calcul_surface_triangle(3,3,4))