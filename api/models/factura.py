class Cliente():
    def __init__(self,row):
        self._dni=row[0]
        self._nombre= row[1]
        self._direccion= row[2]
        self._telefono= row[3]
        self._email= row[4]
        self._fechaRegistro= row[5]

    def to_json(self):
        return {
            "dni":self._dni,
            "nombre" : self._nombre,
            "direccion" : self._direccion,
            "telefono" : self._telefono,
            "email" : self._email,
            "fechaRegistro": self._fechaRegistro, 
        }