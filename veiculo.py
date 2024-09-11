class veiculo:
    def __init__ (self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

        def ligar (self):
            print ("veiculo ligado")

        def desligar (self):
            print("veiculo desligado")

class carro (veiculo):
    def __init__(self, marca, modelo, ano, numeroDePortas):
        super ().__init__(marca, modelo, ano)
        self.numeroDePortas = numeroDePortas

class moto (veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas        

carro1 = carro ("porsche", "cayenne", 2021, 5)
print (carro1.marca)

moto1 = moto ("honda", "horngt", 2001,600)
print (moto1.cilindradas)
