class Productos():
    def __init__(self,row):
        self._id= row[0]
        self._codigo_barra=row[1]
        self._nombre= row[2]
        self._descripcion= row[3]
        self._precio= row[4]
        self._stock= row[5]
        self._categoria= row[6]
        self._proveedor= row[7]
        self._fecha_lanzamiento= row[8]
        self._fecha_vencimiento= row[9]
        self._fecha_modificacion= row[10]
        self._empresa= row[11]
    def to_json(self):
        return {
            "id" : self._id,
            "codigo_barra" : self._codigo_barra,
            "nombre" : self._nombre,
            "descripcion" : self._descripcion,
            "precio" : self._precio,
            "stock" : self._stock,
            "categoria" : self._categoria,
            "proveedor" : self._proveedor,
            "fecha_lanzamiento" : self._fecha_lanzamiento,
            "fecha_vencimiento" : self._fecha_vencimiento,
            "fecha_modificacion" : self._fecha_modificacion,
            "empresa" : self._empresa,
        }