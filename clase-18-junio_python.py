#Clase Martes 18 de Junio 

#NUMEROS ENTEROS = INT o LONG
##LONG 45646545645445L


##NUMERO FLOAT = NUMEROS CON DECIMALES
##EJ : O,32 
#-33,895

# COMPLEX
## 33,8j

# SUMA +
# RESTA -
# MULTIPLICACION *
# POTENCIA **
# DIVICION (conciente) /
# DIVICION (paerte entera) //
# PROMEDIO %

# PROCEDENCIA DE OPERADORES:
# 1- TERMINOS ENTRE PARENTESIS
# 2- POTENCIACION Y RAICES
# 3- MULTIPLICACION Y DIVICION
# 4- SUMA Y RESTA

""" print(15+8)

print(30.5-5)

print(80*2) """




#_______________________________________ STRING = STR (CADENA DE TEXTO)_______________________________________

#COMILLA DOBLE ""
#COMILLAS SIMPLES ''


print("hola, Mundo")

print("Un string \t con tablacion")

print("Otro string pero con \n salto de linea ")


#________________VARIABLES________________
# LAS VARIABLES EN PYTHON SON COMO ETIQUETAS QUE NOS PERMITEN HACER REFERENCIA A OS DATOS.
# POR CADA DATO QUE APARECE EN UN PROGRAMA, PYTHON VA A CREAR UN OBJETO QUE LO CONTIENE.
# CADA OBJETO VA A TENER :
# 1- UN IDENTIFICADOR UNICO (ID)
# 2- UN TIPO DE DATO (ENTERO, DECIMAL, STRING, ECT)
# 3- UN VALOR (EL PROPIO DATO DENTRO)
#LAS VARIABLES EN PYTHON NO GUARDAN LOS DATOS .

dni = 96202294

a = 2
#definir una variable a = 2
print(dni)


mi_variable = 1994

print(mi_variable)

###### EL NOMBRE DE UNA VARIABLE SIEMPRE SE debe EMPEZAR POR UNA LETRA O POR UN GUION BAJO(_) snake_case
#LOS NOMBRES EN LAS VARABLES NO PUEDEN INCLUIR ESPACIOS EN BLANCO

mi_fecha_de_nacimiento = "24 de agosto"

print(mi_fecha_de_nacimiento)

 #METODO DE SAALIDA = PRINT()
 
 #METODO DE ENTADA = INPUT()
 
"""nombre = input("hola! escribi tu nombre:")

print(nombre)"""

print(20+9)

#LA FUNCION INPUT POR DEFECTO CONVIERTE LOS DATOS DE ENTRADA EN UN STRINT (ES UNA CADENA). ANQUE LE ESTEMOS ESCRIBIENDO UN NUMERO

a = 20
b = 30

resultado = a+b

print(resultado)

c = 100
d = 200

print(c+d)

#LOS DATOS DE ENTRADA SE PODRIAN CONVERTIR DE STR (STRING)

e = 30
"""f = input("cual es tu edad?")"""#ESTE ES UN EJEMPLO DE UN DATO DE ENTRADA QUE LO TOMA COMO CADENA DE TEXTO
"""f = int(input("cual es tu edad?"))""" # CONVERSION DE TIPO: de esta forma logramos que python convierta el STR de entrada en un NUMERO


"""print(e*f)"""


cadena_de_texto = "Python SOS LO MEJOR DE MI VIDA TKMMMMMMMMMMMMMMMMMMMMMM YO"
anio_del_curso = "2024"

print(cadena_de_texto + anio_del_curso)

# A LA SUMA DE LOS STRING LO VAMOS A LLAMAR CONCADENACION 

# LOS INDICE VIENEN : 0 (PRIMER CARATER), 1(SEGUNDO CARATER), ECT...
#  P  Y  T  H  O  N
#  0  1  2  3  4  5 INDICES
# -6 -5 -4 -3 -2 -1 INDICE INVERSO
print(cadena_de_texto[-1])