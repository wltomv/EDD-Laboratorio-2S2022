
from nodo import Nodo


class Huffman:

    def __init__(self, contenido) -> None:
        self.frec = self.construirTablaFrecuencias(contenido)
        self.raiz = self.construirArbolHuffman(self.frec)
        self.tablaCodigos = self.tablaBusqueda(self.raiz)

    def construirTablaFrecuencias(self, contenido):
        frecuencias = {}
        for caracter in contenido:
            if frecuencias.get(caracter):
                frecuencias[caracter] += 1
            else:
                frecuencias[caracter] = 1

        return frecuencias

    def construirArbolHuffman(self, frecuencias):
        nodos = []

        for caracter, frec in frecuencias.items():
            nodos.append(Nodo(caracter, frec, None, None))

        nodos.sort(key=lambda char: (
            int(char.frecuencia), ord(char.caracter)))

        while len(nodos) > 1:
            izquierdo = nodos.pop(0)
            derecho = nodos.pop(0)

            padre = Nodo("{}{}".format(izquierdo.caracter, derecho.caracter), izquierdo.frecuencia +
                         derecho.frecuencia, izquierdo, derecho)
            nodos.append(padre)
            nodos.sort(key=lambda char: (
                int(char.frecuencia), ord(char.caracter[0])))

        return nodos.pop(0)

    def construirTablaBusqueda(self, raiz, cadena, tablaB):
        if not raiz.esHoja():
            self.construirTablaBusqueda(raiz.izquierdo, cadena+"0", tablaB)
            self.construirTablaBusqueda(raiz.derecho, cadena+"1", tablaB)
        else:
            tablaB[raiz.caracter] = cadena

    def tablaBusqueda(self, raiz):
        tablaB = {}
        self.construirTablaBusqueda(raiz, "", tablaB)
        return tablaB

    def graficar(self):
        dot = self.raiz.getCodigoGraphviz()
        f = open('./huffman/huffman.dot', 'w')
        f.write(dot)
        f.close()

    def descomprimir(self, contenidoComprimido):
        resultado = ""
        actual = self.raiz
        i = 0
        while i < len(contenidoComprimido):
            while(not actual.esHoja()):
                c = contenidoComprimido[i]
                if(c == '1'):
                    actual = actual.derecho
                elif c == '0':
                    actual = actual.izquierdo
                else:
                    print('caracter invalido: ' + c)
                i += 1
            resultado += actual.caracter
            actual = self.raiz
        return resultado

    def comprimir(self, contenido):
        salida = ""
        for char in contenido:
            salida += self.tablaCodigos[char]

        return salida
