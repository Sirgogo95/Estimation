from Material import Material

class Material_Analisis(Material):
    def __init__(self, codigo, familias = set() , nombre = "" , alias = set() , precio = 0.0 , tasa = 0.0 , unidad = "U", cantidad = 0.0, itbis = 18.0, manejo = 10.0, categoria = ""):
        super().__init__(codigo ,familias, nombre, alias, precio, tasa, unidad)
        self.cantidad = cantidad
        self.itbis = itbis
        self.manejo = manejo
        self.categoria = categoria

    @property
    def cantidad(self):
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self, cantidad = 0.0):
        if cantidad < 0:
            raise ValueError("Cantidad no puede ser negativa")
        else:
            self._cantidad = cantidad
#itbis
    @property
    def itbis(self):
        return self._itbis
    
    @itbis.setter
    def itbis(self, itbis = 0.0):
        self._itbis = itbis/100
#manejo
    @property
    def manejo(self):
        return self._manejo
    
    @manejo.setter
    def manejo(self, manejo = 0.0):
        self._manejo = manejo/100
#categoria
    @property
    def categoria(self):
        return self._categoria
    
    @categoria.setter
    def categoria(self, categoria = ""):
        self._categoria = categoria
###
    @property
    def itbism(self):
        return self._itbis * self.precio

    @property
    def itbism_total(self):
        return self._itbis * self.precio * self.cantidad

    @property
    def manejom(self):
        return self._manejo * self.precio

    @property
    def manejom_total(self):
        return self._manejo * self.precio * self.cantidad

    @property
    def precio_itbis(self):
        return self.precio * (1 + self.itbis)

    @property
    def precio_total(self):
        return self.precio * self.cantidad 

    @property
    def precio_total_itbis(self):
        return self.precio * self.cantidad * (1 + self.itbis)
    
    @property
    def precio_total_itbis_manejo(self):
        return self.precio * self.cantidad * (1 + self.itbis) * (1 + self.manejo)
    

def main():
    m = Material_Analisis("HN",set("Hierro negro"),"Tubo de Hierro negro","",150,30,"U",5,18,10)
    n = Material_Analisis("HN",set("Hierro negro"),"Tubo de Hierro negro","",200,10,"U",3,18,10)
    print(n)


if __name__ == "__main__":
    main()