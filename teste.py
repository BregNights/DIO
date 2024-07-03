class Veiculo:
    def __init__(self, cor, placa, nro_rodas):
        self.cor = cor
        self.placa = placa
        self.nro_rodas = nro_rodas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def ligar_motor(self):
        print("ligando o motor")

    def ligar_farol(self):
        print("ligando o farol")

class Moto(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, nro_rodas, carregado):
        super().__init__(cor, placa, nro_rodas)
        self.esta_carregado = carregado

    def esta_carregado(self):
        return f"{'sim' if self.carregado else 'não'} está carregado"

moto = Moto("azul", "abc-1234", 2)
print(moto)
moto.ligar_motor()
moto.ligar_farol()

carro = Carro("branco", "yak-3598", 4)
print(carro)

caminhao = Caminhao("cinza", "jhy-0362", 8, True)
print(caminhao)