class Material:
    def __init__(self ,codigo ,familias = set() , nombre = "" , alias = set() , precio = 0.0 , tasa = 0.0 , unidad = "U"):
        self.codigo = codigo
        self.familias = familias
        self.nombre = nombre
        self.alias = alias
        self.precio = precio
        self.tasa = tasa
        self.unidad = unidad

   
    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, codigo):
        if codigo == "":
            raise ValueError("Codigo no puede estar vacio")
        else:
            self._codigo = codigo

    @property
    def familias(self):
        return self._familias
    
    @familias.setter
    def familias(self, familias=set()):
        self._familias = familias

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        if nombre == "":
            raise ValueError("Nombre no puede estar vacio")
        else:
            self._nombre = nombre

    @property
    def precio(self):
        return self._precio * (1 + self.tasa)
    
    @precio.setter
    def precio(self, precio = 0.0):
        self._precio = precio

    @property
    def tasa(self):
        return self._tasa
    
    @tasa.setter
    def tasa(self, tasa = 0.0):
        self._tasa = tasa/100

    @property
    def unidad(self):
        return self._unidad
    
    @unidad.setter
    def unidad(self, unidad):
        self._unidad = unidad

    def __str__(self):
        return f"Nombre: {self.nombre} \nCodigo: {self.codigo} \nPrecio sin Itbis: {self.precio} \nUnidad: {self.unidad}"
    
    def __add__(self, other):
        return self.precio + other.precio
    

def main():
    m = Material("HN",set("Hierro negro"),"Tubo de Hierro negro","",150,30,"U")
    n = Material("HN",set("Hierro negro"),"Tubo de Hierro negro","",200,10,"U")
    print(m.precio+n.precio)


if __name__ == "__main__":
    main()