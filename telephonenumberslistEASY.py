def lista_num():
    numeros = []

    while True:
        usernum = int(input('Digite um número de telefone para ser adicionado: ').strip())
        numeros.append(usernum)
        print('Número adicionado! :)')
        cont = input('Deseja continuar? [S/N]: ').upper()
        if cont == 'N':
            break

    print('Números de telefones adicionados: ')
    for numero in numeros:
        print(numero)

lista_num()
