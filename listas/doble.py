from nodo import Nodo_doble


class Doble:
    def __init__(self) -> None:
        self.primero = self.ultimo = None

    def __repr__(self) -> str:
        rep = "["
        actual = self.primero
        while actual is not None:
            rep += f'{actual},' if actual.siguiente != None else f'{actual}'
            actual = actual.siguiente
        rep += "]"
        return rep

    def estaVacia(self):
        return self.primero == None

    def insertarAlInicio(self, dato):
        nuevo = Nodo_doble(dato)
        if self.estaVacia():
            self.primero = nuevo
        else:
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
            self.primero = nuevo

    def insertarAlFinal(self, dato):
        nuevo = Nodo_doble(dato)
        if self.estaVacia():
            self.primero = self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            nuevo.anterior = self.ultimo
            self.ultimo = nuevo

    def eliminar(self, dato):
        encontrado = False
        actual = self.primero
        while actual is not None and not encontrado:
            encontrado = actual.info == dato
            if not encontrado:
                actual = actual.siguiente

        if actual is not None:
            if actual == self.primero:
                self.primero = actual.siguiente
                if actual.siguiente is not None:
                    actual.siguiente.anterior = None
            elif actual.siguiente is not None:
                actual.anterior.siguiente = actual.siguiente
                actual.siguiente.anterior = actual.anterior
            else:
                actual.anterior.siguiente = None
                self.ultimo = actual.anterior
