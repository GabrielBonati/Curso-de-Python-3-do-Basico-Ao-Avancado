# Exs 1

def ola_mundo():
    return 'Olá mundo!'


def mestre(funcao):
    return funcao()


executando = mestre(ola_mundo)
print(executando)


# Exs 2

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


executando = mestre(fala_oi, 'Gabriel')
executando2 = mestre(saudacao, 'Gabriel', saudacao = 'Bom dia!')
print(executando)
print(executando2)
