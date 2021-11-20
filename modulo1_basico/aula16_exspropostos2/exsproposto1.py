numero_inteiro = input('Digite um número inteiro:')

if numero_inteiro.isdigit():
    numero_inteiro = int(numero_inteiro)

    if numero_inteiro % 2 == 0:
        print(f'{numero_inteiro} é Par')
    if numero_inteiro % 2 == 1:
        print(f'{numero_inteiro} é Impar')
else:
    print('Isso não é um inteiro:')
