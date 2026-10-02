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

division_entier_modulo()