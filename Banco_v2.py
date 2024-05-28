'''Função: Sacar, Depositar e Extrato'''
'''Novas funçoes: Criar usuário e Criar conta corrente(vinculada ao usuário)'''
'''Função de saque: Argumento keyword only(**). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno saldo e extrato'''
'''Função de depósito: Argumento positional only(*). Sugestão de argumentos: saldo, valor e extrato. Sugestão de retorno saldo e extrato'''
'''Função extrato: Argumento posicional only e keworld only (*/**). Argumento posicional: saldo. Argumentos nomeado: extrato'''
'''Opcional: Criar função listar contas ou listar usuários'''
'''Usuário: Nome, Data de nascimento, CPF e Endereço. O endereço é uma string com o seguinte formato: endereço, numero - bairro - cidade/sigla estado.
Deve ser armazenado somentos os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF'''
'''Conta: O programa deve armazenar contas em uma lista, uma conta é composta por Agência, Número da Conta e Usuário. O número da conta é sequencial, inicando em 1.
O numero da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas a conta pertence somente a um usuário'''
'''Dica: Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista'''

from os import system
from time import sleep

system("cls")

def cadastro_cliente():
    cpf = input("Insira seu CPF: ").replace(".","").replace("-","")
    filtrar_cpf(cpf)

def criacao_cliente(nome_criacao, cpf_criacao):
    clientes.append(nome_criacao)
    clientes.append(cpf_criacao)
    

def filtrar_cpf(cpf_cliente):
    global clientes
    for cpf in clientes:
        if cpf == cpf_cliente:
            print("CPF em uso, utilize outro CPF ")
            cadastro_cliente()
    else:
        nome = input("Insira seu nome ")
        criacao_cliente(nome, cpf_cliente)

# def criacao_conta():
#     global conta
#     contador = 1
#     while conta[-1] > contador:
#     # conta[-1] = contador
#         contador +=1
#     conta.append(contador)
#     # conta.remove(0)


def depositar(saldo, deposito, extrato): #ok
    if deposito > 0:
        saldo += deposito
        extrato += f"Depósito R${deposito:.2f}\n"
        print(f"\nVocê depositou R${deposito:.2f}")
        sleep(1)
        return saldo, extrato
  
    else:
        print("\nValor inválido")
        sleep(2)
    
def sacar(saldo, saque, extrato, LIMITE_VALOR_SAQUE, quantidade_saque, LIMITE_SAQUE): #ok
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

def exibir_extrato(saldo, extrato):#ok
    print(f"Valor em conta R${saldo:.2f}\n")
    if not extrato:
        print("Nenhum depósito ou saque")
            
    else:
        print("Depósitos e saques\n")
        print(extrato)
        sleep(3)

def menu(): #ok
    menu = '''
    Selecione uma operação para continuar
    [1] Depósito
    [2] Saque
    [3] Extrato
    [4] Nova Conta
    [5] Contas Ativas
    [6] Novo Usuário
    [7] Listar Usuários
    [0] Finalizar operações ou sair
    Operação: '''
    return int(input(menu))

def main ():
    AGENCIA = "0001"
    LIMITE_SAQUE = 3
    LIMITE_VALOR_SAQUE = 500

    nome_banco = "Sem Nome"
    saldo = 0
    extrato = ""
    quantidade_saque = 0

    print(f'''
      Bem vindo ao Banco {nome_banco}''')

    while True:

        operacao = menu()

        if operacao == 1:
            print("Você escolheu a operação de Depósito")
            deposito = float(input("Digite o valor do depósito R$"))

            saldo, extrato = depositar(saldo, deposito, extrato)

        elif operacao == 2:
            print("Você escolheu a operação Saque")
            saque = float(input("Digite o valor do saque R$"))

            saldo, extrato = sacar(
                saldo=saldo,
                saque=saque,
                extrato=extrato,
                LIMITE_VALOR_SAQUE=LIMITE_VALOR_SAQUE,
                quantidade_saque=quantidade_saque,
                LIMITE_SAQUE=LIMITE_SAQUE,
            )
        
        elif operacao == 3:
            print("Você escolheu a operação Extrato\n")

            exibir_extrato(saldo, extrato)

        elif operacao == 4:
            pass

        elif operacao == 5:
            pass

        elif operacao == 6:
            pass

        elif operacao == 7:
            pass

        elif operacao == 0:
            print(f"\nFinalizando operações, o banco {nome_banco} agradece, tenha um ótimo dia")
            sleep(2)
            break

        else:
            print("\nOperação inexistente, selecione a opção corretamente")
            sleep(2)

main()