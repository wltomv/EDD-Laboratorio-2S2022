#include <iostream>
#include <fstream>
#include "../lib/json.hpp"
#include "tabla.h"
using namespace std;
using json = nlohmann::json;

void cargar_datos(TablaDispersa &tabla)
{
	ifstream json_read("empresas.json");
	json dict_json = json::parse(json_read);
	json empresas = dict_json.at("empresas");

	for (auto &empresa : empresas)
	{
		// Empresa ep(id, nombre, direccion, email);
		Empresa *e = new Empresa(empresa["id"], empresa["nombre"], empresa["direccion"], empresa["email"]);
		tabla.insertar(e);
	}
}

int main()
{
	TablaDispersa tabla(37);
	// Empresa *e = new Empresa(3, "Google", "direccion", "correo@correo.com");
	cargar_datos(tabla);
	// tabla.insertar(e);
	tabla.mostrar();
	return 0;
}