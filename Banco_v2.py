'''Função: Sacar, Depositar e Extrato'''
'''Novas funçoes: Criar usuário e Criar conta corrente(vinculada ao usuário)'''
'''Função de saque: Argumento keyword only(*). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno saldo e extrato'''
'''Função de depósito: Argumento positional only(/). Sugestão de argumentos: saldo, valor e extrato. Sugestão de retorno saldo e extrato'''
'''Função extrato: Argumento posicional e keyworld (/,*). Argumento posicional: saldo. Argumentos nomeado: extrato'''
'''Opcional: Criar função listar contas ou listar usuários'''
'''Usuário: Nome, Data de nascimento, CPF e Endereço. O endereço é uma string com o seguinte formato: endereço, numero - bairro - cidade/sigla estado.
Deve ser armazenado somentos os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF'''
'''Conta: O programa deve armazenar contas em uma lista, uma conta é composta por Agência, Número da Conta e Usuário. O número da conta é sequencial, inicando em 1.
O numero da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas a conta pertence somente a um usuário'''
'''Dica: Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista'''

from os import system
from time import sleep

def criar_usuario(usuario):
    cpf = input("Insira seu CPF: ").replace(".","").replace("-","")
    
    cliente = filtrar_cpf(cpf, usuario)
    if cliente:
        print("CPF já existente em nosso banco de dados!")
        return
    
    nome = input("Insira seu nome: ")
    data_nascimento = input("Insira sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Insira seu endereço (endereço, numero - bairro - cidade/sigla estado): ")

    usuario.append({"nome":nome, "cpf":cpf, "data_nascimento":data_nascimento, "endereco":endereco})

    print("Cliente cadastrado...")

def filtrar_cpf(cpf, clientes):
    cpf_filtrado = [usuario for usuario in clientes if usuario["cpf"] == cpf]
    return cpf_filtrado[0] if cpf_filtrado else None

def listar_usuarios(clientes):
    for cliente in clientes:
        mostrar = f'''
        Nome:{cliente['nome']}
        CPF:{cliente['cpf']}
        Nascimento:{cliente['data_nascimento']}
        Endereço:{cliente['endereco']}
        '''
        print(mostrar)

def criar_conta(agencia, numero_conta, usuario):
    cpf = input("Insira seu CPF: ")
    usuario = filtrar_cpf(cpf, usuario)

    if usuario:
        print("Conta criada...")
        return {"agencia":agencia, "numero_conta":numero_conta, "usuario":usuario}
    
    print("Cliente não encontrado no banco de dados")

def listar_contas(contas):
    for conta in contas:
        mostrar = f'''
        Agência:{conta['agencia']}
        Conta:{conta['numero_conta']}
        Titular:{conta['usuario']['nome']}
        '''
        print(mostrar)

def depositar(saldo, deposito, extrato, /):
    if deposito > 0:
        saldo += deposito
        extrato += f"Depósito R${deposito:.2f}\n"
        print(f"\nVocê depositou R${deposito:.2f}")
        sleep(1)
        return saldo, extrato
  
    else:
        print("\nValor inválido")
        sleep(2)
    
def sacar(*, saldo, saque, extrato, LIMITE_VALOR_SAQUE, quantidade_saque, LIMITE_SAQUE):
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

def exibir_extrato(saldo, /, *, extrato):
    print(f"Valor em conta R${saldo:.2f}\n")
    if not extrato:
        print("Nenhum depósito ou saque")
            
    else:
        print("Depósitos e saques\n")
        print(extrato)
        sleep(3)

def menu():
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

def main ():
    AGENCIA = "0001"
    LIMITE_SAQUE = 3
    LIMITE_VALOR_SAQUE = 500

    nome_banco = "Sem Nome"
    saldo = 0
    extrato = ""
    quantidade_saque = 0
    clientes = []
    contas = []

    print(f'''
      Bem vindo ao Banco {nome_banco}''')

    while True:

        operacao = menu()
        system("cls")
        if operacao == 1: # Depósito
            print("Você escolheu a operação de Depósito")
            deposito = float(input("Digite o valor do depósito R$"))

            saldo, extrato = depositar(saldo, deposito, extrato)

        elif operacao == 2: # Saque
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
        
        elif operacao == 3: # Extrato
            print("Você escolheu a operação Extrato\n")

            exibir_extrato(saldo, extrato=extrato)

        elif operacao == 4: # Nova Conta
            numero_conta = len(contas) +1
            conta = criar_conta(AGENCIA, numero_conta, clientes)

            if conta:

                contas.append(conta)

        elif operacao == 5: # Listar Contas
            listar_contas(contas)

        elif operacao == 6: # Novo Usuário
            criar_usuario(clientes)

        elif operacao == 7: # Listar Usuários
            listar_usuarios(clientes)

        elif operacao == 0: # Finalizar operações ou sair
            print(f"\nFinalizando operações, o banco {nome_banco} agradece, tenha um ótimo dia")
            sleep(2)
            break

        else:
            print("\nOperação inexistente, selecione a opção corretamente")
            sleep(2)

main()