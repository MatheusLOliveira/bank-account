def log(nmro_conta, operacao, horario, valor):
    logg = f'---------------------------\n' \
           f'Número da Conta: {nmro_conta}\n' \
           f'Operação: {operacao}\n' \
           f'Horário Realizado: {horario}\n' \
           f'Valor: {valor}\n' \
           f'---------------------------\n\n'.replace('.', ',')

    with open("log.txt", 'a', encoding='utf-8') as file:
        file.write(logg)
