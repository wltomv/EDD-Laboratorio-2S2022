#ifndef ORDENAMIENTO_H
#define ORDENAMIENTO_H
class Ordenamiento
{

private:
    void quicksort(int arreglo[], int primero, int ultimo);
    void intercambiar(int arreglo[], int i, int j);

public:
    Ordenamiento();
    void burbuja(int arreglo[], int tamanio);
    void seleccion(int arreglo[], int);
    void mostrar(int arreglo[], int);
    void insercion(int arreglo[], int);
    void quicksort(int arreglo[], int);
};
#endif