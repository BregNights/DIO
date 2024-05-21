from time import sleep

menu = '''
    Selecione uma operação para continuar
    [1] Depósito
    [2] Saque
    [3] Extrato
    [0] Finalizar operações ou sair
    Operação: '''
nome_banco = "Sem Nome"

saldo = 0
extrato = ""
quantidade_saque = 0
LIMITE_SAQUE = 3
LIMITE_VALOR_SAQUE = 500
print(f'''
      Bem vindo ao Banco {nome_banco}''')

while True:

    opcao = int(input(menu))

    if opcao == 1:
        print("Você escolheu a operação de Depósito")

        deposito = float(input("Digite o valor do depósito R$"))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito R${deposito:.2f}\n"
            print(f"\nVocê depositou R${deposito:.2f}")
            sleep(1)
  
        else:
            print("\nValor inválido")
            sleep(2)

    elif opcao == 2:
        print("Você escolheu a operação Saque")

        saque = float(input("Digite o valor do saque R$"))

        saque_excedido = saque > saldo #Verifica se tem saldo para o saque
        saque_limite = saque > LIMITE_VALOR_SAQUE #Verifica se o saque não ultrapassa o limite de valor por saque
        limite_quantidade_saque = LIMITE_SAQUE == quantidade_saque

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
        
    elif opcao == 3:
        print("Você escolheu a operação Extrato\n")

        print(f"Valor em conta R${saldo:.2f}\n")
        if not extrato:
            print("Nenhum depósito ou saque")
            
        else:
            print("Depósitos e saques\n")
            print(extrato)
            sleep(5)

    elif opcao == 0:
        print(f"\nFinalizando operações, o banco {nome_banco} agradece, tenha um ótimo dia")
        sleep(2)
        break

    else:
        print("\nOperação inexistente, selecione a opção corretamente")
        sleep(2)