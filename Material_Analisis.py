from Material import Material

class Material_Analisis(Material):
    def __init__(self, codigo, familias = set() , nombre = "" , alias = set() , precio = 0.0 , tasa = 0.0 , unidad = "U", itbis = 0.0, manejo = 0.0):
        super().__init__(codigo ,familias, nombre, alias, precio, tasa, unidad)
        self.itbis = itbis
        self.manejo = manejo

    @property
    def itbis(self):
        return self._itbis
    
    @itbis.setter
    def itbis(self, itbis = 0.0):
        self._itbis = itbis/100

    @property
    def manejo(self):
        return self._manejo
    
    @manejo.setter
    def manejo(self, manejo = 0.0):
        self._manejo = manejo/100



m = Material_Analisis("HN",set("Hierro negro"),"Tubo de Hierro negro","",150,30,"U",18,10)
n = Material_Analisis("HN",set("Hierro negro"),"Tubo de Hierro negro","",200,10,"U",18,10)
print(m.itbis)
