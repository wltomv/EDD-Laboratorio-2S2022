from dataclasses import dataclass, field
import csv


@dataclass
class Adyacente:
    nombre: str
    peso: int


@dataclass
class Vertice:
    id: str
    adyacentes: list = field(default_factory=lambda: [])

    def agregar_adyacente(self, final, peso):
        if final not in self.adyacentes:
            self.adyacentes.append(Adyacente(final, peso))


@dataclass
class Grafo:
    vertices: dict = field(default_factory=lambda: {})

    def agregar_vertice(self, id):
        if id in self.vertices:
            print('El vertice ya se encuentra en el grafo')
            return

        self.vertices[id] = Vertice(id)

    def agregar_arista(self, inicio, final, peso):
        validacion = inicio not in self.vertices or final not in self.vertices

        if validacion:
            print('Alguno de los vertices no se encuentra en el grafo')

        self.vertices[inicio].agregar_adyacente(
            final, int(peso))  # grafo dirigido
        # self.vertices[final].agregar_adyacente(inicio, int(peso)) # grfo no dirigido

    def graficar(self):
        dot = 'strict graph \n{\n\tlayout="fdp"\n'

        for _, vertice in self.vertices.items():
            for adyacente in vertice.adyacentes:
                dot += '\t{} -- {} [label="{}"];\n'.format(
                    str(vertice.id), str(adyacente.nombre), adyacente.peso)

        dot += '}'
        return dot

    def grafo_desde_csv(self, ruta_csv):
        with open(ruta_csv, newline='') as File:
            reader = csv.DictReader(File)
            for row in reader:
                if row['origen'] not in self.vertices:
                    self.agregar_vertice(row['origen'])
                if row['destino'] not in self.vertices:
                    self.agregar_vertice(row['destino'])

                self.agregar_arista(row['origen'], row['destino'], row['peso'])

    def dijkstra(self, origen):
        if origen not in self.vertices:
            print("El nodo de origen no se encuentra en el grafo")
            return {}, {}

        costo = {}
        predecesor = {}
        noVisitados = []
        visitados = []

        costo[origen] = 0
        predecesor[origen] = None

        for v in self.vertices:
            if v is not origen:
                costo[v] = float('inf')
            noVisitados.append(v)

        actual = noVisitados[0]
        while len(noVisitados) > 0:
            for adyacente in self.vertices[actual].adyacentes:
                if adyacente.nombre not in visitados:
                    if costo[actual]+adyacente.peso < costo[adyacente.nombre]:
                        costo[adyacente.nombre] = costo[actual] + \
                            adyacente.peso
                        predecesor[adyacente.nombre] = actual
            visitados.append(actual)
            noVisitados.remove(actual)
            actual = self.elegir_minimo(noVisitados, costo)

        return costo, predecesor

    def elegir_minimo(self, lista, costos):
        if len(lista) > 0:
            minimo = lista[0]
            for v in lista:
                if costos[v] < costos[minimo]:
                    minimo = v
            return minimo
        return None

    def ruta(self, costo, predecesor, destino):
        ruta = []
        actual = destino
        while actual != None:
            ruta.insert(0, actual)
            actual = predecesor[actual]
        return ruta, costo[destino]


grafo = Grafo()
grafo.grafo_desde_csv('grafos/ejemplo_clase.csv')

calculos = grafo.dijkstra('A')
ruta1 = grafo.ruta(calculos[0], calculos[1], 'K')
ruta2 = grafo.ruta(calculos[0], calculos[1], 'E')
print(ruta1)
print(ruta2)

print(grafo.graficar())
