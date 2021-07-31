"""
Tipos de dados Primitivos:
str (strings) - textos 'Assim' / "Assim"
int (inteiro) - 123456/ 0 / -10 / -20 / 1500
float (real/flutuante) - 10.5 /  9.57 / -8.76 / 0.0
bool (booleano/lógico) - True/False (10 == 10)
print(bool(0)) ou print(bool('')) = false --> pois 0 e uma string vazia
sã0 false
"""
print('Gabriel', type('Gabriel'))
print('Gabriel', type('Gabriel'), bool('Gabriel'))
print('10', type('10'), type(10))
print('10', type('10'), type(int('10')))
print(-10, type(-10))
print(9.57, type(9.57))
print(10 == 10, type(10 == 10))
print(10 == 11, type(10 == 11))
print(bool(0))
print(bool(1))
print(bool(''))
