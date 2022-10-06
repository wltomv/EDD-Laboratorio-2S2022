
#include <iostream>
#include "modelos.cpp"
#include <math.h>

using namespace std;
class TablaDispersa
{
private:
    int M;
    int numElementos;
    const float R = 0.618034;
    double factorCarga;
    Empresa **tabla;
    int direccion(long clave);
    int dispersion(long clave);

public:
    TablaDispersa(int n);
    void insertar(Empresa *e);
    void mostrar();
};