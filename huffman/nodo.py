
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Nodo:
    caracter: int
    frecuencia: int
    izquierdo: Nodo
    derecho: Nodo

    def esHoja(self):
        return self.izquierdo is None and self.derecho is None

    def getCodigoGraphviz(self):
        dot = "digraph grafica{\n rankdir=TB;\nnode [shape = record, style=filled, fillcolor=lavender];\n"
        dot += self.getCodigoInterno()
        dot += "}"
        return dot

    def getCodigoInterno(self):
        etiqueta = ""
        if(self.izquierdo is None and self.derecho is None):
            etiqueta = 'nodo{} [ label ="{}"];\n'.format(
                id(self), self.frecuencia)

        else:
            etiqueta = 'nodo{} [ label ="<C0>|{}|<C1>"];\n'.format(
                id(self), self.frecuencia)

        if(self.izquierdo != None):
            st = self.izquierdo.getCodigoInterno()
            etiqueta += "{}nodo{}:C0->nodo{}\n".format(
                self.izquierdo.getCodigoInterno(), id(self), id(self.izquierdo))

        if(self.derecho != None):
            etiqueta += "{}nodo{}:C1->nodo{}\n".format(
                self.derecho.getCodigoInterno(), id(self), id(self.derecho))
        return etiqueta
