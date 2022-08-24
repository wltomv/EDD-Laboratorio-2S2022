
#include <iostream>
#include "ordenamientos.hpp"
#include "busquedas.hpp"
using namespace std;

int main()
{
    Ordenamiento ordenamiento;
    Busqueda busqueda;

    int arreglo[] = {34, 67, 23, 56, 12};

    int tamanio = sizeof(arreglo) / sizeof(arreglo[0]);

    // ordenamiento.mostrar(arreglo, tamanio);
    cout << "Ordenamiento" << endl;
    // ordenamiento.quicksort(arreglo, tamanio);
    // ordenamiento.mostrar(arreglo, tamanio);
    cout << "Busqueda" << endl;
    int indice = busqueda.secuencial(arreglo, tamanio, 56);
    cout << indice << endl;
    return 0;
}