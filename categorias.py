class Categorias():
    def __init__(self,row):
        self._id= row[0]
        self._nombre= row[1]
        self._descripcion= row[2]

    def to_json(self):
        return {
            "ID" : self._id,
            "Nombre" : self._nombre,
            "Descripción" : self._descripcion,
        }