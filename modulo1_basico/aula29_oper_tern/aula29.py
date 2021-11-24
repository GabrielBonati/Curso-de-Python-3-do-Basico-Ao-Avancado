# OPERADOR TERNÁRIO EM PYTHON

#Operador Ternário resume o if e else em 1 linha
#logged_user = True
#msg = 'Usuário logado' if logged_user else 'Usuário precisa logar'
#print(msg)

idade = input('Qual a sua idade:')

if not idade.isnumeric():
    print('Você precisa digitar apenas números')
else:
    idade= int(idade)
    e_de_maior = 'Usuário maior de idade' if idade >= 18 else 'Menor de idade'
    print(e_de_maior)