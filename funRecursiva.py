class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

def construir_lista_enlazada(n):
    if n == 0:
        return None  # Caso base: cuando n llega a 0, retornamos None
    else:
        valor = int(input("Ingrese el valor para el nodo actual: "))
        nodo = Nodo(valor)
        nodo.siguiente = construir_lista_enlazada(n - 1)  # Llamada recursiva con n - 1
        return nodo

def imprimir_lista_enlazada(nodo):
    if nodo is not None:
        print(nodo.valor)
        imprimir_lista_enlazada(nodo.siguiente)

n = int(input("Ingrese el número de nodos: "))
lista_enlazada = construir_lista_enlazada(n)

print("La lista enlazada es:")
imprimir_lista_enlazada(lista_enlazada)


