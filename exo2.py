#Exercice2

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