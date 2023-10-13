class Categorias():
    def __init__(self,row):
        self._id= row[0]
        self._nombre= row[1]
        self._descripcion= row[2]

    def to_json(self):
        return {
            "id" : self._id,
            "nombre" : self._nombre,
            "descripcion" : self._descripcion,
        }