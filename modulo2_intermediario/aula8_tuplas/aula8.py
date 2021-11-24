# Tuplas (similar a lista) --> Não é possível editar os itens

# Tupla
t = 1, 2, 3, 4, 5, 6

# Concatenar Tuplas
t1 = 1, 2, 3
t2 = 4, 5, 6
t3 = (t1 + t2)
print(t3)

# Transformar Tupla em Lista
t4 = (1, 2, 3, 4, 5)
t4 = list(t4)
t4[1] = 3000
print(t4)

# Retransformando em Tupla com o item modificado
t4 = tuple(t4)
print(t4)
