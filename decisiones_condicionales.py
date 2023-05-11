"""
Escribir un programa que analice un número, e indique si es positivo o negativo, y si es par o impar. 
En caso de ser cero, también indicarlo. Se debe usar la expresión if-elif-else, y no usar 
subcondiciones; en su lugar, usar condiciones anidadas.
"""
#Crear variable con un número 
numero= 0
resto= numero%2
if resto == 0:
    print("El número", numero, "es par")
elif resto == 1:
    print("El número", numero, "es impar")
if numero >0:
    print("El número ", numero, "es positivo")
elif numero <0:
     print("El número ", numero, "es negativo")
else: 
     print("El número ", numero, "es 0")