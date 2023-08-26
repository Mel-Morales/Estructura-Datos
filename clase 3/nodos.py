class Nodo:
    dato = None
    apuntador = None
    def__init__(self, dato, apuntador):
        self.dato = dato
        self.apuntador = apuntador
    def__str__(self):
        return f"{self.dato}"

print("="*50)
obj1 = Nodo(5, None)
obj2 = Nodo(5, None)
print(obj1)
