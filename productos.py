class Productos():
    def __init__(self,row):
        self._id= row[0]
        self._nombre= row[1]
        self._descripcion= row[2]
        self._Precio= row[3]
        self._Stock= row[4]
        self._Categoría= row[5]
        self._Proveedor= row[6]
        self._Fecha_Lanzamiento= row[7]
        self._Fecha_Vencimiento= row[8]
        self._Fecha_Modificación= row[9]
    def to_json(self):
        return {
            "ID" : self._id,
            "Nombre" : self._nombre,
            "Descripción" : self._descripcion,
            "Precio" : self._Precio,
            "Stock" : self._Stock,
            "Categoría" : self._Categoría,
            "Proveedor" : self._Proveedor,
            "Fecha_Lanzamiento" : self._Fecha_Lanzamiento,
            "Fecha_Vencimiento" : self._Fecha_Vencimiento,
            "Fecha_Modificación" : self._Fecha_Modificación,
        }