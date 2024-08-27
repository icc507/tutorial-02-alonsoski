#Problema 1  / 8 ptos x4 pruebas / 32 puntos
#Concatenación de listas o tuplas
#--------------------------------
#Confeccione un programa que lea 2 tuplas sean t1 y t2
#La salida debe ser una tupla en el orden t2 t1 t2
#---------------------------------
#Ejemplo de entrada:
#         20 90 hola
#		  mundo 44
#La salida debe ser
#         ('mundo', 44, 20, 90, 'hola', 'mundo', 44)
def convertir_elemento(elemento):
    try:
        return int(elemento)
    except ValueError:
        return elemento

entrada1 = input()
entrada2 = input()

t1 = tuple(convertir_elemento(x) for x in entrada1.split())
t2 = tuple(convertir_elemento(x) for x in entrada2.split())
resultado = t2 + t1 + t2

print(resultado)