# Um ano é bissexto se:
# 1. Ele é divisível por 4 e não é divisível por 100.
# 2. Ou ele é divisível por 400.

def verificador_ano_bissexto():
    ano = int(input())
    if ano % 4 == 0 and ano % 100 != 0:
      bissexto = 'Ano Bissexto' 
      print(f'{ano} é um {bissexto}')
    else:
        print(f'{ano} Ano comum')
verificador_ano_bissexto()