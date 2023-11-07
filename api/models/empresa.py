class Empresa():
    def __init__(self,row):
        self._nombre= row[0]
        self._direccion= row[1]
        self._telefono= row[2]
        self._email= row[3]
        self._fechaIngreso= row[4]
        self._CUIT_CUIL= row[5]

    def to_json(self):
        return {
            "nombre" : self._nombre,
            "direccion" : self._direccion,
            "telefono" : self._telefono,
            "email" : self._email,
            "fechaIngreso": self._fechaIngreso,
            "CUIT_CUIL": self._CUIT_CUIL, 
        }