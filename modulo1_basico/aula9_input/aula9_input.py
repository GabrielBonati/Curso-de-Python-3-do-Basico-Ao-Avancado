"""
Entrada de dados
"""
nome = input('Qual o seu nome?')
idade = input('Qual a sua idade?')
ano_atual = 2021
ano_nascimento = (ano_atual - int(idade))
print()
print(f'{nome} tem {idade} anos de idade em {ano_atual}, logo, nasceu em {ano_nascimento}')
