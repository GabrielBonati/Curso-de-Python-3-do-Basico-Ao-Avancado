"""
While em python:
*utilizado para realizar ações enquanto uma condição for verdadeira!
Requisitos: Entender condições e operadores

x = 1  # coluna
while x < 5:
    y = 1  # linha
    while y < 5:
        print(f'({x};{y})')
        y += 1
    x += 1  # x = x + 1

print('Acabou')

"""
while True:
    print()
    num_1 = input('Digite um número:')
    num_2 = input('Digite outro número:')
    operador = input('Digite um operador:')
    num_1 = int(num_1)
    num_2 = int(num_2)

    # +-/*
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    else:
        print(num_1 * num_2)
