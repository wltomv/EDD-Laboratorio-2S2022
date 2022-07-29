

class Nodo:
    def __init__(self, info):
        self.info = info
        self.siguiente = None

    def __repr__(self) -> str:
        return f'{self.info}'


class Nodo_doble(Nodo):
    def __init__(self, info):
        super().__init__(info)
        self.anterior = None
