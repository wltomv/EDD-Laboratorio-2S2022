
from circular import Circular
from simple import Simple
from doble import Doble
from modelos import Usuario
import json


def cargar_datos(ruta):
    with open(ruta) as contenido:
        datos = json.load(contenido)
    return datos


if __name__ == "__main__":
    datos = cargar_datos("usuarios.json")

    lista = Simple()
    lista_doble = Doble()
    lista_circular = Circular()
    lista_circular.insertar(1)
    lista_circular.insertar(2)
    lista_circular.insertar(3)
    # for e in datos:
    #     lista_doble.insertarAlFinal(Usuario.nuevo(e))

    # print(lista)
