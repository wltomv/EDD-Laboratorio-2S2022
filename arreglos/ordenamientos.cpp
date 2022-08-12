#include "ordenamientos.hpp"
#include <iostream>

Ordenamiento::Ordenamiento() {}

void Ordenamiento::mostrar(int arreglo[], int tamanio)
{
    for (int i = 0; i < tamanio; i++)
    {
        std::cout << arreglo[i] << ", ";
    }
    std::cout << std::endl;
}

void Ordenamiento::burbuja(int arreglo[], int tamanio)
{

    int aux;
    for (int i = 0; i < tamanio; i++)
    {
        for (int j = 0; j < tamanio - 1; j++)
        {
            if (arreglo[j] > arreglo[j + 1])
            {
                aux = arreglo[j];
                arreglo[j] = arreglo[j + 1];
                arreglo[j + 1] = aux;
            }
        }
    }
}

void Ordenamiento::seleccion(int arreglo[], int tamanio)
{
    int menor, temp;
    for (int i = 0; i < tamanio; i++)
    {
        menor = i;
        for (int j = i + 1; j < tamanio; j++)
        {
            if (arreglo[j] < arreglo[menor])
            {
                menor = j;
            }

            temp = arreglo[i];
            arreglo[i] = arreglo[menor];
            arreglo[menor] = temp;
        }
    }
}

void Ordenamiento::insercion(int arreglo[], int tamanio)
{
    int actual, pos; // actual es el valor clave
    for (int i = 0; i < tamanio; i++)
    {
        actual = arreglo[i];
        pos = i;

        while (pos > 0 && arreglo[pos - 1] > actual)
        {
            arreglo[pos] = arreglo[pos - 1];
            pos--;
        }

        arreglo[pos] = actual;
    }
}

void Ordenamiento::quicksort(int arreglo[], int primero, int ultimo)
{
    int i, j, central;
    int pivote;
    central = (primero + ultimo) / 2;
    pivote = arreglo[central];

    i = primero;
    j = ultimo;

    do
    {
        while (arreglo[i] < pivote)
            i++;
        while (arreglo[j] > pivote)
            j--;

        if (i <= j)
        {
            intercambiar(arreglo, i, j);
            i++;
            j--;
        }
    } while (i <= j);

    if (primero < j)
        quicksort(arreglo, primero, j); // mismo proceso con sublista izquierda
    if (i < ultimo)
        quicksort(arreglo, i, ultimo); // mismo proceso con sublista derecha
}

void Ordenamiento::intercambiar(int arreglo[], int i, int j)
{
    int aux = arreglo[i];
    arreglo[i] = arreglo[j];
    arreglo[j] = aux;
}

void Ordenamiento::quicksort(int arreglo[], int tamanio)
{
    quicksort(arreglo, 0, tamanio - 1);
}