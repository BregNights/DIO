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

import os
os.system("cls")
def cadastro_cliente():
    cpf = input("Insira seu CPF: ").replace(".","").replace("-","")
    checar_cpf(cpf)

def criacao_cliente(nome_criacao, cpf_criacao):
    global clientes
    clientes.append(nome_criacao)
    clientes.append(cpf_criacao)
    criacao_conta()
    

def checar_cpf(cpf_cliente):
    global clientes
    for x in clientes:
        if x == cpf_cliente:
            print("CPF em uso, utilize outro CPF ")
            cadastro_cliente()
    else:
        nome = input("Insira seu nome ")
        criacao_cliente(nome, cpf_cliente)

def criacao_conta():
    global conta
    contador = 1
    while conta[-1] > contador:
    # conta[-1] = contador
        contador +=1
    conta.append(contador)
    # conta.remove(0)


clientes = []
conta = [0]

cadastro_cliente()
print(conta)
cadastro_cliente()
print (clientes)
print (conta)