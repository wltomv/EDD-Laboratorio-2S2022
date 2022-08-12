#include "busquedas.hpp"
#include <iostream>

Busqueda::Busqueda() {}

int Busqueda::secuencial(int arreglo[], int tamanio, int dato)
{
    int posicion = -1;

    for (int i = 0; i < tamanio; i++)
    {
        if (arreglo[i] == dato)
        {
            posicion = i;
            return posicion;
        }
    }
    return posicion;
}

int Busqueda::binaria(int arreglo[], int tamanio, int dato)
{
    int central, bajo, alto;
    int valorCentral;

    bajo = 0;
    alto = tamanio - 1;

    while (bajo <= alto)
    {
        central = (bajo + alto) / 2;     // índice de elemento central
        valorCentral = arreglo[central]; // valor del índice central
        if (dato == valorCentral)
            return central; // encontrado, devuelve posición
        else if (dato < valorCentral)
            alto = central - 1; // ir a sublista inferior
        else
            bajo = central + 1; // ir a sublista superior
    }
    return -1; // elemento no encontrado
}
