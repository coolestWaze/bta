try:
    import time

    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite outro valor: '))
    act = 0
    while act != 5:
        time.sleep(0.5)
        print('''Oque deseja fazer com estes números? 
        [ 1 ] - somar
        [ 2 ] - multiplicar
        [ 3 ] - maior
        [ 4 ] - novos números
        [ 5 ] - sair do programa''')
        act = int(input('Digite sua opção: '))
        if act == 1:
            soma = n1 + n2
            print(f'A soma é {soma}')
        elif act == 2:
            mult = n1 * n2
            print(f'A multiplicação é {mult}')
        elif act == 3:
            if n1 > n2:
                print(f'O valor "{n1}" é maior.')
            else:
                print(f'O valor "{n2}" é maior.')
        elif act == 4:
            n1 = int(input('Digite um novo número: '))
            n2 = int(input('Digite outro número: '))
        elif act == 5:
            print('Finalizando...')
            time.sleep(1)
            exit()
        else:
            print('Opção inválida, tente novamente.')
        print('-=' * 10)
    print('Fim.')
except ValueError:
    print('Algo ocorreu de forma errada, tente novamente. ')
    exit()
