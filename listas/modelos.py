class Usuario:
    def __init__(self, id, nombre, apellido, email, genero) -> None:
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.genero = genero

    def __repr__(self) -> str:
        return f'{{id:{self.id} - nombre:{self.nombre}}}'

    @classmethod
    def nuevo(cls, datos):
        return Usuario(**datos)
