"""
len = quantidade de caracteres
print(usuario, qnt_caract, type(qnt_caract)) --> mostra a qnt de caracteres
usuario = input('user:')
qnt_caract = len(usuario)

if qnt_caract <6:
    print('Você precisa cadastrar pelo menos 6 caracteres')
else:
    print('Você foi cadastrado no sistema')
"""

user = input('Usuário:')
senha = input('Senha:')
qnt_caracteres1 = len(user)
qnt_caracteres2 = len(senha)

if qnt_caracteres1 < 6:
    print('Usuário Incorreto')

else:
    print('Usuário Correto')

if qnt_caracteres2 < 6:
    print('Quantidade insuficiente de caracteres')

else:
    print('Senha segura')
