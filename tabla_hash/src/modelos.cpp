#include <string>

using namespace std;
class Empresa
{
public:
    int id;
    string nombre;
    string direccion;
    string email;
    Empresa() {}
    Empresa(int id, string nombre, string direccion, string email) : id(id), nombre(nombre), direccion(direccion), email(email) {}
};