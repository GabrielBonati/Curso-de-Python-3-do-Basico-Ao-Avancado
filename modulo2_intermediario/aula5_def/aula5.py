# aula 5 - DEF parte 4
"""
variavel = 'valor'


def func():
    print(variavel)


def func2(arg=None):
    arg = arg.replace('v', 'c')
    return arg


func()
outra_variavel = func2(arg = variavel)

print(outra_variavel)
"""

variavel = 'valor'


def func():
    outra_variavel = 'valor'
    return outra_variavel

def func2(arg):
    print(arg)

var = func()
func()
