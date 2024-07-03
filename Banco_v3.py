from os import system
from time import sleep
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Banco:

    def __init__(self, nome_banco, AGENCIA):
        self.nome_banco = nome_banco
        self.AGENCIA = AGENCIA

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave.capitalize()}:{valor}' for chave, valor in self.__dict__.items()])}"

    def criar_usuario(self, usuario):
        cpf = input("Insira seu CPF: ").replace(".","").replace("-","")
    
        cliente = self.filtrar_cpf(cpf, usuario)
        if cliente:
            print("CPF já existente em nosso banco de dados!")
            return
    
        nome = input("Insira seu nome: ")
        data_nascimento = input("Insira sua data de nascimento (dd-mm-aaaa): ")
        endereco = input("Insira seu endereço (endereço, numero - bairro - cidade/sigla estado): ")

        usuario.append({"nome":nome, "cpf":cpf, "data_nascimento":data_nascimento, "endereco":endereco})

        print("Cliente cadastrado...")

    def filtrar_cpf(self, cpf, clientes):
        cpf_filtrado = [usuario for usuario in clientes if usuario["cpf"] == cpf]
        return cpf_filtrado[0] if cpf_filtrado else None

    def listar_usuarios(self, clientes):
        for cliente in clientes:
            mostrar = f'''
            Nome:{cliente['nome']}
            CPF:{cliente['cpf']}
            Nascimento:{cliente['data_nascimento']}
            Endereço:{cliente['endereco']}
            '''
            print(mostrar)

    def criar_conta(self, agencia, numero_conta, usuario):
        cpf = input("Insira seu CPF: ")
        usuario = self.filtrar_cpf(cpf, usuario)

        if usuario:
            print("Conta criada...")
            return {"agencia":agencia, "numero_conta":numero_conta, "usuario":usuario}
    
        print("Cliente não encontrado no banco de dados")

    def listar_contas(self, contas):
        for conta in contas:
            mostrar = f'''
            Agência:{conta['agencia']}
            Conta:{conta['numero_conta']}
            Titular:{conta['usuario']['nome']}
            '''
            print(mostrar)

    def depositar(self, saldo, deposito, extrato, /):
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito R${deposito:.2f}\n"
            print(f"\nVocê depositou R${deposito:.2f}")
            sleep(1)
            return saldo, extrato
  
        else:
            print("\nValor inválido")
            sleep(2)
    
    def sacar(self, *, saldo, saque, extrato, LIMITE_VALOR_SAQUE, quantidade_saque, LIMITE_SAQUE):
        saque_excedido = saque > saldo #Verifica se tem saldo para o saque
        saque_limite = saque > LIMITE_VALOR_SAQUE #Verifica se o saque não ultrapassa o limite de valor por saque
        limite_quantidade_saque = LIMITE_SAQUE == quantidade_saque #verifica se a qunatidade de saque é igual ao limite de saque

        if saque_excedido:
            print("\nSaldo para saque indisponível, verifique o valor em conta.")
            sleep(2)

        elif saque_limite:
            print(f"\nValor ultrapassa o limite de R${LIMITE_VALOR_SAQUE:.2f} por saque.")
            sleep(2)

        elif limite_quantidade_saque:
            print("\nQuantidade de saques diários excedido.")
            sleep(2)

        elif saque > 0:
            saldo -= saque
            LIMITE_SAQUE -= 1
            extrato += f"Saque R${saque:.2f}\n"
            print(f"\nVocê sacou: R${saque:.2f}")
            sleep(1)

        else:
            print("\nValor inválido")
            sleep(2)

        return saldo, extrato

    def exibir_extrato(self, saldo, /, *, extrato):
        print(f"Valor em conta R${saldo:.2f}\n")
        if not extrato:
            print("Nenhum depósito ou saque")
            
        else:
            print("Depósitos e saques\n")
            print(extrato)
            sleep(3)

    def menu(self):
        menu = '''
        Selecione uma operação para continuar
        [1] Depósito
        [2] Saque
        [3] Extrato
        [4] Nova Conta
        [5] Listar Contas
        [6] Novo Usuário
        [7] Listar Usuários
        [0] Finalizar operações ou sair
        Operação: '''
        return int(input(menu))

    def main (self):
        LIMITE_SAQUE = 3
        LIMITE_VALOR_SAQUE = 500
        
        saldo = 0
        extrato = ""
        quantidade_saque = 0
        clientes = []
        contas = []

        print(f'''
        Bem vindo ao Banco {self.nome_banco}''')

        while True:

            operacao = self.menu()
            system("cls")
            if operacao == 1: # Depósito
                print("Você escolheu a operação de Depósito")
                deposito = float(input("Digite o valor do depósito R$"))

                saldo, extrato = self.depositar(saldo, deposito, extrato)

            elif operacao == 2: # Saque
                print("Você escolheu a operação Saque")
                saque = float(input("Digite o valor do saque R$"))

                saldo, extrato = self.sacar(
                    saldo=saldo,
                    saque=saque,
                    extrato=extrato,
                    LIMITE_VALOR_SAQUE=LIMITE_VALOR_SAQUE,
                    quantidade_saque=quantidade_saque,
                    LIMITE_SAQUE=LIMITE_SAQUE,
                )
        
            elif operacao == 3: # Extrato
                print("Você escolheu a operação Extrato\n")

                self.exibir_extrato(saldo, extrato=extrato)

            elif operacao == 4: # Nova Conta
                numero_conta = len(contas) +1
                conta = self.criar_conta(self.AGENCIA, numero_conta, clientes)

                if conta:

                    contas.append(conta)

            elif operacao == 5: # Listar Contas
                self.listar_contas(contas)

            elif operacao == 6: # Novo Usuário
                self.criar_usuario(clientes)

            elif operacao == 7: # Listar Usuários
                self.listar_usuarios(clientes)

            elif operacao == 0: # Finalizar operações ou sair
                print(f"\nFinalizando operações, o banco {self.nome_banco} agradece, tenha um ótimo dia")
                sleep(2)
                break

            else:
                print("\nOperação inexistente, selecione a opção corretamente")
                sleep(2)

class Cliente:
    def __init__(self, endereco, contas, ):
        self.endereco = endereco
        self.contas = contas
    
        def realizar_transacao(self, conta=Conta, transacao=Transacao):
            pass

        def adicionar_conta(self, conta=Conta):
            pass
        
class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self, saldo, numero, agencia):
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.cliente = Cliente
        self.historico = Historico

    def saldo():
        #retorna um float
        pass

    def nova_conta(self, cliente=Cliente, numero=int): #rever
        pass

    def sacar(self, valor):
        #recebe um valor e retorna um boleano
        pass
    
    def depositar(self, valor):
        #recebe um valor e retorna um boleano
        pass

class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, limite, limite_saques):
        super().__init__(saldo, numero, agencia)
        self.limite = limite
        self.limite_saques = limite_saques

class Historico: 
    def adicionar_transacao():
        pass

class Transacao(ABC):
    def registrar(self, conta=Conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor




# banco = Banco("Sem Nome", "0001")
# banco.main()