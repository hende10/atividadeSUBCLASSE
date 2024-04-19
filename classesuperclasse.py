class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def freiar(self):
        return(f"você freiou!")
    def acelerar(self):
        return(f"você acelerou!")
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor
    def abrir_porta(self):
        return(f"você abriu a porta do seu carro!")
    
class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada
    def empinar(self):
        return (f"você empinou a moto!")
    
if __name__ == '__main__':
    carro1 = Carro("Renault", "Sandeiro", "Prata")
    moto1 = Moto("Yamara", "XJ6", "600")
    print(F'Marca: {carro1.marca}\n Modelo: {carro1.modelo}\n Cor: {carro1.cor}')
    print(F'Marca: {moto1.marca}\n Modelo: {moto1.modelo}\n Cilindrda: {moto1.cilindrada}')
    print(moto1.empinar())
    print(carro1.abrir_porta())
    print(carro1.acelerar())
    print(carro1.freiar())
    print(moto1.freiar())
    print(moto1.acelerar())