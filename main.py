# Comentarios

# Salida(imprimir) de Datos
#
# print("Hola") # imprimira hola normalmente
#
# print("Hola " , "Mundo ") # otra forma de escribir un mensaje normal
#
# # imprime el mensaje completo en una sola linea 'end=" "' omite el salto de linea del print()
#
# print("Hola ",end=" ")
# print("Mundo")
#
# # imprimir mensajes separados por un caracter o cadenas con el operador sep="caracter o cadena"
#
# print("hola","jovenes","campeones",sep="--")
#
# # para hacer salto de linea
# print("Hola","jovenes","\ncomo", "ganador",sep=",")
#
# # mostrar mensaje con valor de la variable dentro del print
# # se realiza con poniendo f antes de la comillas
# a = 6
# b = 8
# suma = a + b
# print(f"Hola esta es la suma : {suma}")
#
# # ejercicio de sep y end
# # sep es para separar
# # end omitir salto de linea
# # \n para saltar linea
# # f" {variable} " para mostrar valores dentro de los print
#
# #ejercicio| deletrar tu nombre usando el operador sep
# # es decir que quede asi J - O - N - A - T - A - N
# # el operador sep se utiliza mientras las cadenas
# # esten separadas por comas en el print ("cad1", "cadn" , sep="caracter que los separa")
# print("practicando el operador sep ")
# print("J","O","N","A","T","A","N",sep="-")
#
# print("-- se deletreo Correctamente --")
#
# print("--- ---- ---- ")
# print("practicando en operador end ")
# print("Hola soy ",end=" ")  # con estas dos intrucciones se une el mensaje de aqui
# print("Jonatan Ing Sistemas") # con el de aca
#
# print("--- --- --- ---")
# print("Hola quiero que saltes ", "\nde linea "," esto debe ir arriba pero estamos usando salto de linea ")
#
# print("--- ---- --")
# totalVentas = int(input("Ingresa tu total de ventas en $ : "))
# comision = 0.08
# ganancia = totalVentas * comision
#
# if ganancia > 1000:
#     print("Vas por buen camino , sigue asi...")
# else:
#     print("no te fue muy bien ,pero sigue trabajando pronto veras los resultados ")
#
#
# print(f"Total de ventas : {totalVentas} || Ganancias : {ganancia}")
#
# print("---")

# Variables(Tipos):
# constrante numerica => PI = 3.1416 su valor no cambia
# Variable  => edad = 34  la edad va cambiando en el tiempo
# Expresion => arimetica ( 3 + 2 ) , logica ( 5 >= 3) devuelve un boolean (true o false)
# Mensaje => mensaje = " guardan cadenas de caracteres"
# Valor logico => se refiere a las variables booleanes (puertaAbierta = false), es decir que la puerta esta cerrada

a = 16 # variable
b = a * 18 * 3 # expresion aritmetica
f = a > 4 # expresion logica

mensaje = "Estas sobrepasando tus limites "
print(f"El mensaje del profesor es {mensaje}")

print(f" ¿ a es mayor que 4 ? => {f}")

print("Ingresa 1. Si cerraste la puerta")
print("Ingresa 2. Si Esta Abierta")
opcion = int(input("Ingresar opcion : "))
if opcion == 1:
    puertAbierta = False
else:
    puertAbierta = True

if puertAbierta == False:
    print("La puerta esta cerrada ")
else:
    print("La pueta esta Abierta ")

print("---- Fin del programa ----")