from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime, date

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []
    
        def realizar_transacao(self, conta, transacao):
            transacao.registrar(conta)

        def adicionar_conta(self, conta):
            self._contas.append(conta)
        
class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento

    # def __str__(self):
    #     return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()


    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor): #recebe um valor e retorna um boleano
        saldo = self.saldo
        saldo_excedido = valor > saldo

        if saldo_excedido:
            print("\nSaldo para saque indisponível, verifique o valor em conta.")

        elif valor > 0:
            self._saldo -= valor
            print(f"\nSaque realizado com sucesso.")
            return True
        
        else:
            print("\nOperação falhou.")
        
        return False

        
    
    def depositar(self, valor): #recebe um valor e retorna um boleano
        if valor > 0:
            self._saldo += valor
            print("\nDepósito realizado com sucesso.")

        else:
            print("\nOperação falhou.")
            return False
        
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

class Historico: 
    def adicionar_transacao():
        pass

class Transacao(ABC):
    def registrar(self, conta=Conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor



banco = Conta(saldo=50, numero=1, agencia=000)
pessoa = PessoaFisica(cpf="123.456,789-00", nome = "User", data_nascimento=date(1996,5,30))
print (pessoa)

# banco.depositar(100)
# print("deposito 100")
# print(banco.saldo())
# banco.sacar(50)
# print("saque 50")
# print(banco.saldo())