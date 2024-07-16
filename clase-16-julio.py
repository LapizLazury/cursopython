#SENTENCIAS INTERATIVAS
#WHILE
#FOR

# EL flujo de ejecucion de una sentencia WHILE:
#1. Se evalúa la expresión de control.
#2. Si es verdadera, se ejecuta el cuerpo de la sentencia.
#3. Se vuelve a evaluar la expresión de control y se repite el paso 2 hasta que se evalúe como falso.

#1. E

numero = 10 #la variable
while numero >0:
    print(numero)
    numero-= 1
print("termino el conteo")   

n = 0
while n <=5:
    n+=1
    print("N vale", n)
    
#WHILE condicion :
#  intrucciones de while
#else
#  intrucciones de while-else
#si noce termino con break
#  intrucciones de while-else

chanse =1
while chanse <= 3:
    txt = input("Escribe SI: ")
    if txt == "SI": 
        print("Ok, lo conseguiste en el intento", chanse)
        break
    chanse +1
else:
    print("No lograste en los 3 intentos")