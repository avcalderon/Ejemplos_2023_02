"""
class NombreCortoException(Exception):
    pass
def validar(nombre):
    if len(nombre)>5:
        raise NombreCortoException()
    
nombre = input("Introduce nombre")

try:
    validar(nombre)
except NombreCortoException
    print("Error de Excepcon")
"""

"""
#Codigo correcto...
dividendo = 5
divisor =2
try:
    resultado = dividendo / divisor
except ZeroDivisionError:
    print("Division entre 0")
else:
    print("Ok")
    print("Resultado :", resultado)

