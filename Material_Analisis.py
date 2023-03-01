from Material import Material

class Material_Analisis(Material):
    def __init__(self, codigo, itbis = 0.0, manejo = 0.0):
        super().__init__(self ,codigo ,familias = set() , nombre = "" , alias = set() , precio = 0.0 , tasa = 0.0 , unidad = "U")
        self.itbis = itbis
        self.manejo = manejo