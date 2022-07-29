from nodo import Nodo


class Circular:
    def __init__(self) -> None:
        self.lc = None

    def __repr__(self) -> str:
        pass

    def insertar(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = nuevo

        if self.lc is not None:
            nuevo.siguiente = self.lc.siguiente
            self.lc.siguiente = nuevo

        self.lc = nuevo
