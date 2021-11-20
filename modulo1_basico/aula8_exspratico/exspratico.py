nome = 'Gabriel Bonati'
idade = 23
altura = 1.79
peso = 103
imc = peso/altura**2
ano_atual = 2021
ano_nascimento = ano_atual - idade

print(f'{nome} tem {idade} anos e pesa {peso}.')
print(f'O imc de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {ano_nascimento}.')
