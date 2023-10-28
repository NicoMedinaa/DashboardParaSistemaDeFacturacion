class Proveedores():
    def __init__(self,row):
        self._nombre= row[0]
        self._direccion= row[1]
        self._telefono= row[2]
        self._email= row[3]
        self._descripcion= row[4]

    def to_json(self):
        return {
            "nombre" : self._nombre,
            "direccion" : self._direccion,
            "telefono" : self._telefono,
            "email" : self._email,
            "descripcion" : self._descripcion,
        }