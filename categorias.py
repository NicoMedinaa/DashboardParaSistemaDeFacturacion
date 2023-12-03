class Categorias():
    def __init__(self,row):
        self._nombre= row[0]
        self._descripcion= row[1]

    def to_json(self):
        return {
            "nombre" : self._nombre,
            "descripcion" : self._descripcion,
        }