# Aula 7 - Lambda

"""
a = lambda x, y: x * y
print(a(2,2))

Fez a mesma função que a 'def' de forma anonima
"""

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

#Ordenação em uma linha:
print(sorted(lista, key=lambda item: item[1], reverse=True))


'''
# Forma de ordenar com a função lambda:
lista.sort(key=lambda item: item[1], reverse=True)
print(lista)
'''

"""
Forma de fazer a ordenação da lista com a função def
def func(item):
    return item[1]

lista.sort(key = func, reverse=True)
print(lista)
"""