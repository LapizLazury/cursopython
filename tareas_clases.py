#DESTINADO A LAS TAREAS


#CLASE 18/6: CREAR UN SCRIPT EN EL QUE PODAMOS CALCULAR LA NOTA FINAL EN BASE A 5 EXAMENES, ESTOS EXAMENES EQUIVALEN A UN PORCENTAJE DE LA NOTA FINAL.

# LA NOTA NUMERO 1 CORRESPONDE AL 20% DE LA NOTA FINAL.
# LA NOTA NUMERO 2 CORRESPONDE AL 10% DE LA NOTA FINAL.
# LA NOTA NUMERO 3 CORRESPONDE AL 10% DE LA NOTA FINAL.
# LA NOTA NUMERO 4 CORRESPONDE AL 10% DE LA NOTA FINAL.
# LA NOTA NUMERO 5 CORRESPONDE AL 50% DE LA NOTA FINAL.

#A esto se lo suele llamar promedio ponderado: no todos los valores tienen el mismo "peso".
#Por ejemplo, dado el ejercicio de arriba me conviene sacarme una mejor nota en el examen donde la nota vale casi el 50% de la nota final.



"""print = int("verificar la nota")
nota = int(input())
if((nota)=(20%))
print(10/20%)"""
# esto esta mal________________________________________________________

# Solicitar las notas de los exámenes al usuario
"""nota1 = float(input("Ingrese la nota del examen 1 (20%): "))
nota2 = float(input("Ingrese la nota del examen 2 (10%): "))
nota3 = float(input("Ingrese la nota del examen 3 (10%): "))
nota4 = float(input("Ingrese la nota del examen 4 (10%): "))
nota5 = float(input("Ingrese la nota del examen 5 (50%): "))

# Porcentajes asignados a cada examen
porcentaje1 = 0.20
porcentaje2 = 0.10
porcentaje3 = 0.10
porcentaje4 = 0.10
porcentaje5 = 0.50

# Calcular la nota final
nota_final = (nota1 * porcentaje1) + (nota2 * porcentaje2) + (nota3 * porcentaje3) + (nota4 * porcentaje4) + (nota5 * porcentaje5)

# Mostrar la nota final
print("La nota final es: " + str(nota_final))"""


#_______________________________________________________________-

#CLASE 25/6: TENIENDO DOS LISTA LA CUAL LLAMAREMOS lista_1 y lista_2 hay que hacer 
# los siguientes ejercicios:

#Añadir a la lista_1 el entero 4567 y despues el string "UNAHUR"

#Añadir a la lista_2 el string "EDUCACION" y despues el entero 789

#Crear una lista_3 con todos los elementos de la lista_1 MENOS el último

#Crear una lista_4 con todos los elementos de la lista_2 MENOS el primero y último

#Crear una lista_5 con todos los elementos de la lista_3 y de la lista_4
#______________________________________________________________________________________________

# El ultimo item de la tupla creada, el numero de items de la misma,
# la posicion donde se encuentra algun item que haya dentro, 
# una lista con los ultimos cuatro items de la tupla, un item que haya en la posicion 8, 
# el numero de veces que se repite algún item dentro de la misma.

#________________________RESULTADO___________________________25/06

#Añadir a la lista_1 el entero 4567 y despues el string "UNAHUR"

"""lista_1 = "4567"
print(len(lista_1))
string = "UNAHUR"
print(len(string))"""

#__________________________

#Añadir a la lista_2 el string "EDUCACION" y despues el entero 789

"""lista_2 = "789"
print(len(lista_2))
string = "EDUCACION"
print = (len(string))"""

#_____________________________

#Crear una lista_3 con todos los elementos de la lista_1 MENOS el último
"""lista_1 = "4567"
print(len(lista_1))
string = "UNAHUR"""

#Crear una lista_4 con todos los elementos de la lista_2 MENOS el primero y último
"""lista_2 = "789"
print(len(lista_2))
string = "EDUCACION"""

#Crear una lista_5 con todos los elementos de la lista_3 y de la lista_4

"""lista_1 = "4567"
print(len(lista_1))
string = "UNAHUR"
lista_2 = "789"
print(len(lista_2))
string = "EDUCACION"""


#____________________________________________________________________________________
#EJERCICO 3 : 2 / JULIO / 2024
#                              AHORA CON TUPLAS
#Crear una variable llamada tupla con más de 15 items y printear lo siguiente:

"""mi_tupla=(1, 2, 3, 7, 9, 8, 2, 2, 50, 2, 13, 47, 33, 25, 19, 0)
print(len(mi_tupla))"""

# Buscamos el ultimo item
"""print(mi_tupla[-1])"""

# Buscamos el numero de items de la tupla
"""print(mi_tupla.index(0))"""

# la posicion donde se encuentra algun item que haya dentro

"""print(mi_tupla[2])"""

# Buscamos los ultimos 4 item

"""print(f"{mi_tupla[11],mi_tupla[12],mi_tupla[13],mi_tupla[14]}")"""

# Buscamos el item en la posición 8

"""print(mi_tupla[8])"""

#busca, los numeros repetidos 
"""print(mi_tupla.count(2))"""


#____________________________ECHO POR EL PROFESOR_______________________________________________________________________________

# Ahora trabajamos con tuplas
"""tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)"""

# Printeamos el último item de la tupla
"""print("Último item de la tupla:", tupla[-1])"""

# Printeamos el número de items de la tupla
"""print("Número de items en la tupla:", len(tupla))
"""
# Printeamos la posición de algún item específico
"""item = 5
print(f"Posición del item {item} en la tupla:", tupla.index(item))"""

# Creamos una lista con los últimos cuatro items de la tupla
"""ultimos_cuatro = tupla[-4:]
print("Últimos cuatro items de la tupla:", ultimos_cuatro)"""

# Printeamos el item en la posición 8
"""print("Item en la posición 8:", tupla[8])"""

# Printeamos el número de veces que se repite algún item en la tupla
"""item = 4
print(f"El item {item} se repite {tupla.count(item)} veces en la tupla")"""

#_______________________________________________________________-
#CLASE 16 de Julio, analizar el código y explicar que hace cada linea,
# luego reemplazarlo por otra condición
#WHILE
n = 5
while n >5:
    if (n%2)==0:
        print(n,"Es un numero par")
        break
    n+=1
else:
        print(n,"es un numero impar")
    


    
    
#  IF ELSE ELIF
# Construir un algoritmo con lo viste en clase bajo el mismo diagrama de flujo de la imagen 
# que está en la carpeta assets del repo