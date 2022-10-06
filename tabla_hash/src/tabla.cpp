#include "tabla.h"

TablaDispersa::TablaDispersa(int n)
{
    tabla = new Empresa *[n];
    M = n;
    for (int j = 0; j < M; j++)
        tabla[j] = NULL;
    numElementos = 0;
    factorCarga = 0.75;
}

void TablaDispersa::insertar(Empresa *empresa)
{
    int posicion;
    posicion = direccion(empresa->id);
    tabla[posicion] = empresa;
    numElementos++;

    // considerar el factor de carga
    double carga = (double)numElementos / M;
    if (carga > factorCarga)
        printf("!Factor de carga supera el %f por ciento!!\nCoviene aumentar el tamaño de la tabla", factorCarga * 100);
}
// Calcula el indice del arreglo en donde se insertará el nuevo elemento
int TablaDispersa::dispersion(long x)
{
    double t;
    int v;
    t = R * x - floor(R * x); // parte decimal
    v = (int)(M * t);
    return v;
}

int TablaDispersa::direccion(long clave)
{
    int pos;
    int i = 0;
    pos = dispersion(clave);
    while (tabla[pos] != NULL && tabla[pos]->id != clave)
    {
        i++;
        pos = pos + i * i;
        pos = pos % M; // considera el array como circular
    }
    return pos;
}

void TablaDispersa::mostrar()
{
    cout << "Numero de elementos: " << numElementos;
    for (int i = 0; i < M; i++)
    {
        if (tabla[i] != NULL)
            cout << i << "\t " << tabla[i]->nombre << endl;
    }
}