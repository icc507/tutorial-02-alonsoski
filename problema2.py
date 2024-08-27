#Problema 2  / 9 ptos x4 pruebas / 36 puntos
#Concatenación de listas o tuplas
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios elementos y los entregue de manera inversa
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 90 hola jiji 77
#La salida debe ser
#         (77, 'jiji', 'hola', 90, 20)
def convertir_elemento(elemento):
    try:
        return int(elemento)
    except ValueError:
        return elemento

entrada1 = input().split()[::-1]


t1 = tuple(convertir_elemento(x) for x in entrada1)


print(t1)