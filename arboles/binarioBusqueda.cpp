#include "binarioBusqueda.h"

template <class T>
BST<T>::BST()
{
    raiz = NULL;
}

template <class T>
void BST<T>::insertar(T dato)
{
    raiz = insertarNodo(raiz, dato);
}
template <class T>
Nodo<T> *BST<T>::insertarNodo(Nodo<T> *raiz, T dato)
{
    if (raiz == NULL)
    {
        Nodo<T> *nuevo = new Nodo<T>(dato);
        raiz = nuevo;
    }
    else if (dato < raiz->dato)
    {
        raiz->izquierdo = insertarNodo(raiz->izquierdo, dato);
    }

    else if (dato > raiz->dato)
    {
        raiz->derecho = insertarNodo(raiz->derecho, dato);
    }

    return raiz;
}

template <class T>
void BST<T>::inOrden()
{
    inOrden(raiz);
}

template <class T>
void BST<T>::inOrden(Nodo<T> *raiz)
{
    // IRD
    if (raiz != NULL)
    {
        inOrden(raiz->izquierdo);
        cout << raiz->dato << " ";
        inOrden(raiz->derecho);
    }
}