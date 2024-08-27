#Problema 2  / 7 ptos x4 pruebas / 28 puntos
#Ingreso de valores en árbol TRI-nario
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios números y cree un árbol trinario con listas
# esto es igual que el binario, pero los elementos que son iguales van en una lista
# centro, de la forma [numero, [subarbol IZQ], [mismo NUM], [subarbol DER] ]
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 30 90 90 8 5 90
#La salida debe ser
#         [20, [8, [5, [], [], []], [], []], [], [30, [], [], [90, [], [90, [], [90, [], [], []], []], []]]]

def arbolTrinario(numero):
    return [numero, [], [], []]

def insertaEnArbolTrinario(arbol, numero):
    if arbol == []:
        arbol += arbolTrinario(numero)
    elif numero < arbol[0]:
        insertaEnArbolTrinario(arbol[1], numero)  # Inserción en el subárbol izquierdo
    elif numero > arbol[0]:
        insertaEnArbolTrinario(arbol[3], numero)  # Inserción en el subárbol derecho
    else:
        insertaEnArbolTrinario(arbol[2], numero)  # Inserción en el subárbol central (mismo número)

lista = input().split()
arbol = arbolTrinario(int(lista[0]))
for x in range(1,len(lista)):
    insertaEnArbolTrinario(arbol,int(lista[x]))

print(arbol)