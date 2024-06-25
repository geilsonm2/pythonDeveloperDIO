menu = """
    Qual operação deseja realizar?

    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [0] - Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0 
LIMITE_SAQUES = 3

while True:
    operacao = int(input(menu))
    if operacao == 1:
        valor = float(input('Qual o valor que deseja depositar?\n'))
        if valor > 0:
            print(f'R$ {valor:.2f}')
            deposito = f'Foi depositado o valor de {valor} \n'
            saldo += valor
            extrato += deposito
        else: 
            print('Valor Invalido.')
    elif operacao == 2:
        valor = float(input(('Qual valor deseja sacar? ')))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print(f"Saldo insuficiente. Seu saldo atual é de R${saldo}")

        elif excedeu_limite:
            print(f'Valor máximo para saque é de R${limite}')
        
        elif excedeu_saques:
            print('Limite de saques diários excedidos.')
        
        elif valor > 0:
            saldo -= valor
            extrato += f'Realizando saque no valor de R${valor}'
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif operacao == 3:
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f'\nSaldo? R$ {saldo:.2f}:')

    elif operacao == 0:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operações desejada.")