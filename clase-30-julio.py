#upper
cadena= "Hola Chicos"
print(cadena.upper())

print("Hola Chicos".upper())

#lower

string= "Hola Chicos"
print(string.lower())

print("Hola Chicos".lower())

#CAPITALIZE
cadena1= "Hola Chicos"
print(cadena1.capitalize())

#TITLE
cadena2= "Hola mUNDO"
print(cadena2.title())

# COUNT
cadena3= "Hola mUNDO esta cadena tiene mas a"
print(cadena3.count("a"))

#find
cadena4= "Hola mUNDO esta cadena tiene mas a"
print(cadena4.find("mUN"))

#RFIND
cadena5= "Hola amigo como estas amigo"
print(cadena5.find("amigo"))
print(cadena5.rfind("amigo"))

#SPLIT

cadena6= "Hola mundo"
print(cadena6.split())

#JOIN
cadena7= "Hola mundo"
print("-".join(cadena7))

#STRIP
cadena8 = "---------Hola mundo----------"
print(cadena8)
print(cadena8.strip("-"))

cadena8= "      Hola mundo"
print(cadena8)
print(cadena8.strip())

#REPLASE
cadena9= "Moron"
print(cadena9.replace("o","0"))

#     METODOS PARA LISTA 
#CLEAR

letras = ["a", "b", "c", "d", "e", "f"]
print(letras)
letras.clear()
print(letras)

# EXTEND

numeros = [1,2,3,4,5,]
numeros + [6,7,8,9]

lista1 =[1,2,3,4,5]
lista2 = [6,7,8,9]

lista1.extend(lista2)

print(lista1)

#INSERT
lista4 = [1,2,3,4,5,6]
lista4.reverse()
print(lista4)

#SORT

lista5 = [5,2,8,1,9,3]
lista5.sort()
print(lista5)

#                CONJUNTOS
#COPY

set1 = {1, 2, 3, 4,}
set2 = set1.copy()
print(set2)

#ISDISJOINT

set3 = {1, 2, 3,}
set4 = {1, 2, 3,}
print(set3.isdisjoint(set4))

#ISSUBSET

set5 = {-1, 99}
set6 = {1, 2, 3, 4, 5}
print(set5.issubset(set6))

#ISSUPERSET

set7 = {1, 2, 3}
set8 = {1, 2,}
print(set7.issuperset(set8))

"""c1={1,2,3}
c2={3,4,5}
c3={-1,99}
c4={1,2,3,4,5}
print(c1.issubset(c2))
print(c1.issuperset(c4))
"""

#UNION

set9 = {1, 2, 3}
set10 = {3, 4, 5,}
print(set9.union(set10))

#DIFFERENCE
"""set1 = {1,2,3}
set2 = {3,4,5}
print(set1.difference(set2))"""

#DIFFERENCE_UPDATE

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.difference_update(set2)
print(set1)

#INTESECTION

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.intersection(set2)
print(set1.intersection(set2))

#INTERSECTION_UPDATE

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.intersection_update(set2)
print(set1)

#diccionario
#get
colores = {"amarillo":"yellow","azul":"blue","rojo":"red"}
print(colores.get("verde", "no hay clave verde"))

#KEYS

colores = {"amarillo":"yellow","azul":"blue","rojo":"red"}
print(colores.keys())

#VALUES

colores = {"amarillo":"yellow","azul":"blue","rojo":"red"}
print(colores.values())

#ITEMS

colores = {"amarillo":"yellow","azul":"blue","rojo":"red"}
print(colores.items())

for clave , valor in colores.items():
    print(clave , valor)
    
    
    



