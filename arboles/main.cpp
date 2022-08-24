#include "binarioBusqueda.cpp"

int main()
{
    BST<int> *enteros = new BST<int>();
    enteros->insertar(8);
    enteros->insertar(3);
    enteros->insertar(10);

    enteros->inOrden();
}