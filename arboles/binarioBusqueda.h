#include <iostream>

using namespace std;

template <class T>
class Nodo
{
public:
    Nodo *izquierdo;
    Nodo *derecho;
    T dato;
    Nodo(T dato)
    {
        this->dato = dato;
        this->izquierdo = NULL;
        this->derecho = NULL;
    }
    Nodo() {}
};

template <class T>
class BST
{
private:
    Nodo<T> *insertarNodo(Nodo<T> *raiz, T dato);
    void inOrden(Nodo<T> *);

public:
    Nodo<T> *raiz;
    BST();
    void insertar(T dato);
    void inOrden();
};