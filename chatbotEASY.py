def chatbot():
    print("Olá! Eu sou um chatbot. Como posso ajudar você hoje?")

    while True:
        useranswer = input('Mensagem chatbot: ').lower()
        if useranswer in ['oi', 'ola', 'olá', 'opa']:
            print('Olá! Eu sou o chatbot criado por Waze! Como vai?')
        elif useranswer in ['vou bem', 'estou bem', 'estou me sentindo bem']:
            print('Ótimo saber!')
        elif useranswer in ['tchau', 'até mais', 'vou indo', 'adeus']:
            print('Até mais, volte sempre!')
            break
        else:
            print('Não entendi, pode repetir?')
chatbot()
