# Implementación simple de blockchain
El código que incluye la presente impletación corresponde únicamente a una aproximación básica de blockchain desde el punto de vista de las estructuras de datos.Aún faltan muchos aspectos que considerar

## Bloque
Definición de un bloque en formato json
```json
{
    "INDEX": 0,
    "TIMESTAMP": "05-06-22::10:34:45",
    "NONCE": 2345,
    "DATA": [
        {
            "FROM": "0x4281ecf07378ee595c564a59048801330f3084ee",
            "SKINS": [
                {
                    "SKIN": 123,
                    "VALUE": 456
                },
                {
                    "SKIN": 21,
                    "VALUE": 789
                }
            ]
        },
        {
            "FROM": "0xb170A3d31c72CB59B1659CFaD83196ed7087c1aB",
            "SKINS": [
                {
                    "SKIN": 1,
                    "VALUE": 45
                }
            ]
        }
    ],
    "PREVIOUSHASH": "0000axwsde...",
    "ROOTMERKLE": "39b923082a194166d8d92989116bd",
    "HASH": "000082b12041cb5a7bac8ec90f86b654af6b1ac8bfc5ed08092e217235df0229"
}
```

**Nota**:la sección *"Data"* contiene un arreglo con todas las transacciones realizadas