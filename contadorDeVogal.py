def conta_vogais(texto):

    VOGAIS = ['A','E','I','O','U','a','e','i','o','u']
    contador = 0

    for char in texto:
        if char in VOGAIS:
            contador += 1
        else:
            continue
    return contador

texto = input()

resultado = conta_vogais(texto)
print(f"O número de vogais na string '{texto}' é: {resultado}")
