# Dicionários

# Cria Chaves

"""
d1 = {'chave1': 'Valor da Chave ', 'nova_chave': 'valor da nova chave'}
print(d1['chave1'])
"""

# Padrão de Códigos:
'''
d1 = {}
d1['nova_chave'] = 'valor da nova chave'
print(d1)
'''

# Possível utilizar str,int,tuple

"""
d1 = {
    'chave1': 'valor1',
    "chave2'": 'valor2',
    "chave3": 'valor3',
}
"""

# Conferindo se existe a chave no dicionário
"""
d1['naoexiste'] = 'Agora existe'
if d1.get('nomedachave') is not None:
    print(d1.get('nomedachave'))
"""

# Fazendo um 'update' de uma chave
"""
d1.update({'nova_chave':'novo_valor'})

if d1.get('nova_chave') is not None:
    print(d1.get('nova_chave'))
"""

# Excluindo uma chave do dicionário
"""
del d1['str']
print(d1)
"""

# Checando valores:
"""
print('str' in d1)
print('str' in d1.keys())
print('valor' in d1.values())
"""

# Quantos Pares de Chave/Valor:
"""
print(len(d1))
"""

# Usando estrutura de repetição:

"""
for v in d1.values():  # Acessando valores
    print(v)

for k in d1.items():  # Acessa chave e valor
    print(k)

for k,v in d1.items():  # Desempacotando
    print(k, v)
"""
# Criando um dicionário com clientes e usando for in:

"""
clientes = dict(cliente1={
    'nome': 'Gabriel',
    'Sobrenome': 'Bonati',
}, cliente2={
    'nome': 'João',
    'sobrenome': 'Moreira'
}, cliente3={
    'nome': 'Antonio',
    'sobrenome': 'Marcelo'
})

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')
"""

# criando uma cópia
"""
d1 = {1:'a', 2:'b', 3:'c'}
v = d1.copy()

v[1]= 'Gabriel'

print(d1[1])
print(v)
"""

# Transformando Listas em Dicionários (funciona também com tuplas dentro de listas)
lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]

d1 = dict(lista)
d2 = {'a':'b', 'c':'d'}
d1.update(d2) # Unindo d1 e d2

# Usando a função pop (Elimina um item)

# d1.pop('c3')
print(d1)
