"""
Formatando valores com modificadores:
:s - Texto(strings)
:d - Inteiros(int)
:f - Números de ponto flutuante (float)
:.(Número)f - Quantidade de casas decimais (float) Ex: :.3f
:(CARACTERE)(> OU < OU ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""
num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print(f'{divisao:.2f}')

print('')

num_2 = 10213
print(f'{num_2:0>10.3f}')

print('')

nome = 'Gabriel Bonati'
nome_formatado = '{n:0<20}'.format(n=nome)
print(nome_formatado)

print('')

nome = 'Gabriel Bonati'
print(nome.lower())  # Tudo Minúsculo
print(nome.upper())  # Tudo Maiúsculo
print(nome.title())  # Primeira letra maiuscula
