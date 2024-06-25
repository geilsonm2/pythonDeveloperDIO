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
            deposito = f'Foi depositado o valor de {valor:.2f} \n'
            saldo += valor
            extrato += deposito

        else: 
            print('Valor Invalido.')

    elif operacao == 2:

        if numero_saques < LIMITE_SAQUES:
            valor = float(input(('Qual valor deseja sacar? ')))
            if valor > 0:  
                if valor <= saldo:
            
                    if valor <= limite:                
                        print(f'Realizando saque no valor de R${valor:.2f}')
                        numero_saques += 1
                        saldo -= valor
                        print(f'Você pode realizar {3 - numero_saques} saques.\n')
                        extrato += f'Foi realizado saque no valor de R${valor}\n'
            
                    else:
                        print(f'Valor máximo para saque é de R${limite}')
            
                else:
                    print(f"Saldo insuficiente. Seu saldo atual é de R${saldo}")
                    print(f"Seu saldo atual é: R${saldo}")
            else:
                print('Valor inválido.')
        else:
            print('Limite de saques diários excedidos.')
    
    elif operacao == 3:
        print('\n============ EXTRATO ============\n')
        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        print(f'\nO saldo atual é R${saldo:.2f}')
        print('\n====================================')
    
    elif operacao == 0:
        print('Até mais e obrigado por utilizar nossos serviços ! ❤️')
        break
    
    else:
        print("Opção inválida. Tente novamente! ")
        menu

