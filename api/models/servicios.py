class Servicios():
    def __init__(self,row):
        self._id= row[0]
        self._nombre= row[1]
        self._categoria= row[2]
        self._empresa= row[3]
        self._descripcion= row[4]
        self._precio= row[5]
        self._duracion= row[6]
        self._unidadMedida=row[7]
        self._fechaInicio= row[8]
        self._fechaFinalizacion= row[9]
        self._fechaCreacion= row[10]
        self._fechaModificacion= row[11]
        self._estado= row[12]
    def to_json(self):
        return {
            "id" : self._id,
            "nombre" : self._nombre,
            "categoria" : self._categoria,
            "empresa" : self._empresa,
            "descripcion" : self._descripcion,
            "precio" : self._precio,
            "duracion" : self._duracion,
            "unidadMedida": self._unidadMedida,
            "fechaInicio" : self._fechaInicio,
            "fechaFinalizacion" : self._fechaFinalizacion,
            "fechaCreacion" : self._fechaCreacion,
            "fechaModificacion" : self._fechaModificacion,
            "estado" : self._estado,
        }