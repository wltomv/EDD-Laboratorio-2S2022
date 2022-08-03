from nodo import Nodo, Nodo_ll


class Lista_listas:
    def __init__(self) -> None:
        self.inicio = None

    def insertarAlInicio(self, dato):
        nuevo = Nodo_ll(dato)
        if self.inicio == None:
            self.inicio = nuevo
        else:
            nuevo.siguiente = self.inicio
            self.inicio = nuevo

    def insertarHijo(self, encabezado, informacion_hijo):
        actual = self.inicio
        while actual is not None:
            if actual.info == encabezado:
                break
            actual = actual.siguiente

        if actual is not None:
            nuevo = Nodo(informacion_hijo)
            if actual.hijo == None:
                actual.hijo = nuevo
            else:
                nuevo.siguiente = actual.hijo
                actual.hijo = nuevo

    def imprimirHijos(self, nodo_encabezado):
        rep = "["
        actual = nodo_encabezado.hijo
        while actual is not None:
            rep += f'{actual},' if actual.siguiente != None else f'{actual}'
            actual = actual.siguiente
        rep += "]"
        return rep

    def imprimir(self):
        actual = self.inicio
        rep = "{"
        while actual is not None:
            rep += f'{actual}:'
            rep += f'{self.imprimirHijos(actual)}, '
            actual = actual.siguiente
        rep += "}"
        return rep

    def graficarHijos(self, nodo_encabezado):
        rep = ""
        enlaces = ""

        actual = nodo_encabezado.hijo
        while actual is not None:
            rep += f'{hash(actual)}[ label= "{actual}"]\n'
            enlaces += f'{hash(actual)} ->{hash(actual.siguiente)}\n' if actual.siguiente != None else ""
            actual = actual.siguiente

        return f'{rep}{enlaces}'

    def graficar(self):
        # variable para almacenar el codigo de graphviz de la estructura de datos
        rep = "digraph G { \nnode [shape=box]\n"
        # variables para almacenar el codigo que relaciona los nodos encabezados
        enlaces = ""
        # establece los nodos encabezados en la misma direccion (horizontal)
        direccion = "\n{ rank = same;"

        # recorrido de la estructura
        actual = self.inicio
        while actual is not None:
            rep += '\n# ---- encabezado e hijos -----\n'
            rep += f'{hash(actual)}[ label= "{actual}"]'
            # retorna el codigo de los nodos hijos y sus enlaces
            rep += f'\n{self.graficarHijos(actual)}'
            # se vincula a un nodo encabezado con su siguiente en la lista
            enlaces += f'{hash(actual)} ->{hash(actual.siguiente)}\n' if actual.siguiente != None else ""
            # enlace del encabezado con el primero de la sublista
            rep += f'\n{hash(actual)} ->{hash(actual.hijo)}\n' if actual.hijo != None else ""
            direccion += f'{hash(actual)};'
            actual = actual.siguiente
        direccion += "}"
        rep += '\n# ---- enlazando los encabezados -----\n'
        rep += f'{enlaces}'
        rep += '\n# ---- estableciendo la misma direccion para los nodos encabezados -----'
        rep += f'{direccion}'
        # final del gráfico
        rep += "\n}"
        return rep
