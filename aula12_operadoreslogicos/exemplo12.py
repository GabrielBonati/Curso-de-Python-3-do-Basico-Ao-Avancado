usuario = input('Nome de Usuário:')
senha = input('Senha:')

usuario_bd = 'gbonati'
senha_bd = 'gbd980403'

if usuario_bd == usuario and senha_bd == senha:
    print('Usuário Logado')
else:
    print('Usuário ou Senha incorretos')