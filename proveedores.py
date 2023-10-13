class Proveedores():
    def __init__(self,row):
        self._id= row[0]
        self._nombre= row[1]
        self._Dirección= row[2]
        self._Teléfono= row[3]
        self._Email= row[4]

    def to_json(self):
        return {
            "ID" : self._id,
            "Nombre" : self._nombre,
            "Dirección" : self._Dirección,
            "Teléfono" : self._Teléfono,
            "Email" : self._Email,
        }