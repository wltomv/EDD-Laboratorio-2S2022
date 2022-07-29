from nodo import Nodo


class Simple:
    def __init__(self):
        self.inicio = None

    def __repr__(self):
        rep = "["
        actual = self.inicio
        while actual is not None:
            rep += f'{actual},' if actual.siguiente != None else f'{actual}'
            actual = actual.siguiente
        rep += "]"
        return rep

    def insertarAlInicio(self, dato):
        nuevo = Nodo(dato)
        if self.inicio == None:
            self.inicio = nuevo
        else:
            nuevo.siguiente = self.inicio
            self.inicio = nuevo

    def insertarAlFinal(self, dato):
        nuevo = Nodo(dato)
        if self.inicio == None:
            self.inicio = nuevo
        else:
            aux = self.inicio
            while aux.siguiente != None:
                aux = aux.siguiente
            aux.siguiente = nuevo

    def imprimir():
        print()
