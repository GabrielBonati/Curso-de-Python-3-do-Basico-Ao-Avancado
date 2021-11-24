# Funções (def) em Python - Aula 3

def func(*args, **kwargs):
    print(args)

    idade = kwargs.get('idade')

    if idade is not None:
        print(f'{idade} anos')
    else:
        print('Nao colocou idade')

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func(*lista, *lista2, nome='Gabriel', sobrenome = 'Bonati', idade=23)
