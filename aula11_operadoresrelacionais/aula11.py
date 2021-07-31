"""
Operadores Relacionais:
== igualdade
> maior que
>= maior ou igual a que
< menor que
<= menor ou igual a que
!= diferente
"""

nome = input('Qual o seu nome?')
idade = input('Qual a sua idade?')
idade = int(idade)
idade_menor = 20
idade_maior = 30

if idade >= (idade_menor and idade <= idade_maior):
    print(f'{nome} pode pegar empréstimo')
