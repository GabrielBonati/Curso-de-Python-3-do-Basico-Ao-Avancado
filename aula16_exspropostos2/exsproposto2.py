horario = input('Digite o horário atual (0-23):')

if horario.isdigit():
    horario = int(horario)

    if horario < 0 or horario > 23:
        print('Horário deve estar entre 00 e 23')
    else:
        if horario <= 11:
            print('Bom dia')
        elif horario <= 17:
            print('Boa Tarde')
        else:
            print('Boa noite')

else:
    print('Por favor exiba um horário entre 00 e 23')