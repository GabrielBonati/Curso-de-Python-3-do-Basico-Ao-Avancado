print('Você responderá um quiz sobre diversidade e '
      'para passar deve no mínimo acertar 60% das questôes:')

perguntas = {
    'Pergunta 1': dict(pergunta='Quanto é 2+2?', respostas=dict(a='1', b='4', c='6', d='9'), resposta_certa='b'),
    'Pergunta 2': dict(pergunta='Quanto é 3*2?', respostas=dict(a='20', b='15', c='6', d='2'), resposta_certa='c'),
    'Pergunta 3': dict(pergunta='Quem descobriu o Brasil?', respostas=dict(a='Pedro Alvares Cabral', b='Cristovao Colombo', c='Americo Vespucio', d='Jesualdo Ferreira'), resposta_certa='a'),
    'Pergunta 4': dict(pergunta='Qual a cor do cavalo brando de Napoleão', respostas=dict(a='Vermelho', b='Azul', c='Marrom', d='Branco'), resposta_certa='d'),
    'Pergunta 5': dict(pergunta='Qual o melhor time do mundo?', respostas=dict(a='Flamengo', b='Palmeiras', c='Corinthians', d='Cruzeiro'), resposta_certa='b'),
    'Pergunta 6': dict(pergunta='Com quantos paus se faz uma favela?', respostas=dict(a='4', b='6', c='10', d='20'), resposta_certa='a'),
    'Pergunta 7': dict(pergunta='Quanto é 950*6?', respostas=dict(a=950*6, b=950*7, c=951*6, d=960*5), resposta_certa='a'),
}
respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}:{pv["pergunta"]}')

    print('Selecione a alternativa correta:')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')


    reposta_usuario = input('Sua resposta:')

    if reposta_usuario == pv['resposta_certa']:
        print('Você Acertou')
        respostas_certas += 1
    else:
        print('Você errou')

    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

if porcentagem_acerto >= 60:
    print(f'Você tirou uma nota {respostas_certas} , que é acima da média')
else:
    print(f'Você tirou uma nota {respostas_certas}, que é abaixo da média')
