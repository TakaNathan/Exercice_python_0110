#Exercice1
#titre de l'exercice
from math import sqrt
print("EXERCICE1")
def division_entier_modulo() :
     
    "Retourne la resultat de la division entiere et le modulo"
    #contrat de type : ()->()
    "On lis les valeurs avec input et les convertit en int"
    #dividende, diviseur sont des variables locales

    dividende = int(input("Entrez le premier nombre : "))
    diviseur = int(input("Entrer le deuxieme nombre : "))

    #on recommence la fonction le diviseur = 0
    if (diviseur == 0) :
        print("Division par 0 impossible")
        division_entier_modulo()
    else :
        #quotient et modulo sont variables globales
        #quotient retourne le resultat de la division entiere
        quotient = dividende//diviseur
        modulo = dividende%diviseur

        print("le resultat la division entiere de",dividende,"par",diviseur,"est",quotient)
        print("le reste la division de",dividende,"par",diviseur,"est",modulo,"\n")

division_entier_modulo()


#Exercice2
#titre de l'exercice
print("EXERCICE2")
"Transform la temperature de Celsius en Fahrenheit"
#(float)->(float)
def celsius_en_fahrenheit(temp_Celsius) :

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

#on teste avec 37˚C
t_celsius = 37
t_fahrenheit = celsius_en_fahrenheit(t_celsius)
print(t_celsius,"˚C correspond a",t_fahrenheit,"˚F\n")


#Exercice3
#titre de l'exercice
print("EXERCICE3")


def calcule_note_finale(devoirsMoyenne,partiel,examen) :
    #Calcul de la note finale a partir des 3 notes donnees
    #(float,float,float)->(float)
    
    #si une note<0 alors la fonction ne retourne rien et s'arrete
    if(devoirsMoyenne<0) or (partiel<0) or (examen<0) :
        print("Note invalide!")
        return
    else :
        note_finale = devoirsMoyenne*25/100 + partiel*25/100 + examen*50/100
        return note_finale

#on teste avec 15,14,18
note_finale = calcule_note_finale(15.0,14.0,18.0)
print("La note finale est :",note_finale)

#on teste avec 8,17,2
note_finale = calcule_note_finale(8.0,14.0,2.0)
print("La note finale est :",note_finale)


#Exercice4
#titre de l'exercice
print("EXERCICE4")
"Calcul de la surface du triangle"
#(float,float,float)->(float)

def calcul_surface_triangle(cote1,cote2,cote3) :
#test de comparaison pour connaitre le plus grand cote
    grand_cote = cote1
#je compare grand_cote avec chaque cote et le cote dont grand_cote prend la valeur du plus grand
    if(grand_cote<cote2) :
        grand_cote=cote2
        if(grand_cote<3):
            grand_cote = cote3
    if (grand_cote<cote3) :
        grand_cote = cote3
#je teste la condition sum(petit_cote)>grand_cote    
    if (cote1+cote2+cote3)<= 2*grand_cote :
        print("ce n'est pas des bonnes dimensions pour un triangle")
        return
    else :
        #pour inclure tout les cotes je rejoute grand_cote car j'ai annule un cote a cause de lui
        # p designe le perimetre
        p = cote1+cote2+cote3
        surface = sqrt(p*(p-cote1)*(p-cote2)*(p-cote3))/4
        return surface

#test de calcul de la surface du triangle avec 3,3 et 4
print(calcul_surface_triangle(3,3,4))