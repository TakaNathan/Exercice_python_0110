#Exercice3

def calcule_note_finale(devoirsMoyenne,partiel,examen) :
    #Calcul de la note finale a partir des 3 notes donnees
    #(float,float,float)->(float)
    
    note_finale = devoirsMoyenne*25/100 + partiel*25/100 + examen*50/100
    return note_finale

#on teste avec 80,70,90
note_finale = calcule_note_finale(80,70,90)
print("La note finale est :",note_finale)