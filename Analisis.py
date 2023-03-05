from Material_Analisis import Material_Analisis

class Analisis:
    def __init__(self,*materiales,codigo = "",mano_de_obra = 0.0,monto_mano_de_obra = 350.0):
        self.codigo = codigo
        self.materiales = materiales
        self.mano_de_obra = mano_de_obra
        self.monto_mano_de_obra = monto_mano_de_obra

    @property
    def listado_materiales(self):
        a = []
        for material in self.materiales:
            a.append(material)
        return a

    
    @property
    def MO(self):
        return self.mano_de_obra * self.monto_mano_de_obra

    @property
    def monto_itbis(self):
        x = 0
        for material in self.materiales:
            x = material.precio_itbism_total + x
        return x

    @property
    def monto_manejo(self):
        x = 0
        for material in self.materiales:
            x = material.precio_manejom_total + x
        return x
    
    @property
    def monto_total_itbis(self):
        x = 0
        for material in self.materiales:
            x = material.precio_total_itbis + x
        return x + self.mano_de_obra * self.monto_mano_de_obra

    @property
    def monto_total_itbis_manejo(self):
        x = 0
        for material in self.materiales:
            x = material.precio_total_itbis_manejo + x
        return x + self.mano_de_obra * self.monto_mano_de_obra

    def __str__(self):
        x = ""
        for material in self.materiales:
            x = x + f"{material.nombre} | {material.cantidad} | {material.unidad} | {material.precio_total_itbis_manejo:.2f} | {material.categoria} \n"
        x = x + f"mano de obra : {self.MO:.2f} \n"
        x = x + f"total : {self.monto_total_itbis_manejo:.2f}"
        return x


        

def main():
    m = Material_Analisis("HN",set("Hierro negro"),"Tubo de Hierro negro","",150,30,"U",5,18,10,"Soporteria")
    n = Material_Analisis("PVC",set("Hierro negro"),"Tubo de PVC","",200,10,"U",3,18,10,"Replanteo")

    z = Analisis(m,n,mano_de_obra = 16*3)
    print(listado(z,z,z,z,z,z,z,z))
    print (z)


def listado(*analisis):
    listado = []
    unicos = []
    total = []
    filtrados = []
    for _ in analisis:
        for x in _.listado_materiales:
            listado.append({"codigo": x.codigo, "cantidad": x.cantidad})
    for _ in listado:
        unicos.append(_["codigo"])

    unicos = list(set(unicos))

    for _ in unicos:
        filtrados = list(filter(lambda codigo: codigo["codigo"] == _,listado))
        total.append({"codigo": _, "cantidad": sum(filtrado["cantidad"] for filtrado in filtrados)})

    return(total)









if __name__ == "__main__":
    main()