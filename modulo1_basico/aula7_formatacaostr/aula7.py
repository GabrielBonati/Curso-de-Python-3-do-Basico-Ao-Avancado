nome = "Gabriel Bonati"
idade = 23
peso = 103
altura = 1.80
imc = peso/(altura*altura)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('Apesar do meu imc ser {2:.2f}, e eu ter {1} anos, meu nome é {0}'.format(nome, idade, imc),)
print('Apesar do meu imc ser {im:.2f}, e eu ter {i} anos, meu nome é {n}'.format(n=nome, i=idade, im=imc),)
