
from circular import Circular
from simple import Simple
from doble import Doble
from modelos import Usuario
from lista_listas import Lista_listas
from pila import Pila
from cola import Cola
import json


def cargar_datos(ruta):
    with open(ruta) as contenido:
        datos = json.load(contenido)
    return datos


if __name__ == "__main__":
    datos = cargar_datos("usuarios.json")

    # lista = Simple()
    # lista_doble = Doble()
    # lista_circular = Circular()
    # lista_circular.insertar(1)
    # lista_circular.insertar(2)
    # lista_circular.insertar(3)
    # for e in datos:
    #     lista_doble.insertarAlFinal(Usuario.nuevo(e))

    # print(lista)

    # ----- ejemplo de lista de listas ------
    departamentos_municipios = Lista_listas()
    departamentos_municipios.insertarAlInicio("Alta Verapaz")
    departamentos_municipios.insertarAlInicio("Baja Verapaz")
    departamentos_municipios.insertarAlInicio("Peten")
    departamentos_municipios.insertarAlInicio("Guatemala")

    departamentos_municipios.insertarHijo("Alta Verapaz", "Coban")
    departamentos_municipios.insertarHijo("Alta Verapaz", "Santa Cruz Verapaz")
    departamentos_municipios.insertarHijo("Alta Verapaz", "Tactic")

    departamentos_municipios.insertarHijo("Peten", "Flores")
    departamentos_municipios.insertarHijo("Peten", "San Jose")
    departamentos_municipios.insertarHijo("Peten", "San Benito")
    print(departamentos_municipios.graficar())

    # # ----- Ejemplo de pila -------
    # pila = Pila()
    # pila.push(1)
    # pila.push(2)
    # pila.push(3)

    # pila.visualizar()
    # pila.pop()
    # pila.visualizar()
    # print(pila.peek())
    # # ----- Ejemplo de cola -------
    # cola = Cola()
    # cola.enqueue(1)
    # cola.enqueue(2)
    # cola.enqueue(3)
    # cola.visualizar()
    # cola.dequeue()
    # cola.dequeue()
    # cola.visualizar()
