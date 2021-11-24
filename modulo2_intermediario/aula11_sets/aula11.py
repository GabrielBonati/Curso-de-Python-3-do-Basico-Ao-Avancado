# Sets em Python (conjuntos)
"""
add(adiciona), update(atualiza), clear, discard
union | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos
"""
# Trabalhando com conjuntos, adicionando e retirando elementos
"""
s1 = {1,2,3,4,5}
s2 = set() # conjunto vazio
s2.add(1)
s2.add(2)
s2.discard(2)
s2.update([1,2,3,4,5,6,7])
print(s2)
"""

# Transformando listas em sets, para assim eliminar as duplicatas
"""
l1 = [1,2,1,1,2,4,5,6,6,6,6,3,4,3, 'Gabriel', 'Gabriel']
l1 = set(l1)
l1 = list(l1)
print(l1)
"""
# Operações com Conjuntos
"""
s1 = {1,2,3,4,5,6,7,}
s2 = {4,5,6,6,7,8,9,10}

# União de Conjuntos:
s3 = s1 | s2
print(f'União:{s3}')

# Intersecção de Conjuntos:
s4 = s1 & s2
print(f'Intersecção{s2}')

# Subtração de Conjuntos:
s5 = s1 - s2
s6 = s2 - s1
print(f'Subtração:{s5}')
print(f'Subtração:{s6}')

# Diferença Simétrica:
s7 = s1 ^ s2
print(f'Diferença Simétrica:{s7}')
""" 