class Moradia():
    def __init__(self,tipo,comodos,local):
        self.tipo = tipo
        self.comodos = comodos
        self.local = local
        

    def Vender(self):
        return {
            f"{self.tipo} esta à venda com {self.comodos} no {self.local}"
        }
    
    def Alugar(self):
        return {f"{self.tipo} esta disponivel com {self.comodos} no {self.local}"}

class Casa(Moradia):
    def __init__(self, tipo,comodos,local):
        super(). __init__ (tipo,comodos,local)

class Apartamento(Moradia):
    def __init__(self, tipo,comodos,local):
        super(). __init__ (tipo,comodos,local)

class Kitnet(Moradia):
    def __init__(self, tipo,comodos,local):
        super(). __init__ (tipo,comodos,local)


Moradia1 = Moradia("casa", 5, "Jardim Fontális")
Moradia2 = Moradia("Apartamento", 3, "Vila Mazzei")
Moradia3 = Moradia("Kitnet", 4, "Vila Nivi")

print(Moradia1.Vender())
print(Moradia1.Alugar())

print(Moradia2.Vender())
print(Moradia2.Alugar())

print(Moradia3.Vender())
print(Moradia3.Alugar())


