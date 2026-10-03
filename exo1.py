#Exercice1
def division_entier(dividende,diviseur) :
     #affiche le resultat  de la
     #divison entiere de 2 nombres
     #(float,float)->(int)

    quotient = dividende//diviseur
    return quotient

def division_modulo(dividende,diviseur) :
    #affiche le modulo  de la
    #divison entiere de 2 nombres
    #(float,float)->(int)
    modulo = dividende%diviseur
    return int(modulo)

dividende = float(input("Entrer la dividende de l'operation"))
diviseur = float(input("Entrer le diviseur de l'operation"))
quotient = division_entier(dividende,diviseur)
modulo = division_modulo(dividende,diviseur)
print("le resultat la division entiere de",dividende,"par",diviseur,"est",quotient)
print("le reste la division de",dividende,"par",diviseur,"est",modulo)

