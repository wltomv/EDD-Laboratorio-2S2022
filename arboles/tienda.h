#include <string>

using namespace std;
class Producto
{
private:
    int id;
    string proveedor;
    string nombre;

public:
    Producto(int id, string proveedor, string nombre) : id(id), proveedor(proveedor), nombre(nombre) {}
};

class Cliente
{
private:
    int dpi;
    string nombre;
    string telefono;
    string email;

public:
    Cliente(int dpi, string nombre, string telefono, string email)
    {
        this->dpi = dpi;
        this->nombre = nombre;
        this->telefono = telefono;
        this->email = email;
    }

    Cliente() {}
    bool operator<(Cliente const &rhs) const
    {
        return dpi < rhs.dpi;
    }
    bool operator>(Cliente const &rhs) const
    {
        return dpi > rhs.dpi;
    }
    friend ostream &operator<<(ostream &os, const Cliente &cl);
};

ostream &operator<<(ostream &os, const Cliente &cl)
{
    os << "Dpi: " << cl.dpi << ", Nombre: " << cl.nombre << endl;
    return os;
}

class Pedido
{
private:
    int codigo;
    string fechaRealizacion;
    bool estado;
    float total;

public:
    Pedido(int codigo, string fechaRealizacion, bool estado, float total)
    {
        this->codigo = codigo;
        this->fechaRealizacion = fechaRealizacion;
        this->estado = estado;
        this->total = total;
    }
};
