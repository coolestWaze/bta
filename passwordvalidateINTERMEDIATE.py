#Validador de Senhas
# // - //
#Escreva uma função que valide senhas. A senha deve ter pelo
#menos 8 caracteres, incluindo
#pelo menos uma letra maiúscula, uma letra minúscula, um número e um símbolo especial (por exemplo, @, #, $, etc.).
user_password = str(input('Digite sua senha: '))
char_upper = char_down = num = special = 0
charsize = len(user_password)
if charsize < 8:
    print('Senha recusada, deve haver mais de 8 caracteres.')
    exit()

for charup in user_password:
    if charup.isupper():
        char_upper+=1
    elif charup.islower():
        char_down+=1
for number in user_password:
    if number.isnumeric():
        num+=1
for specialchar in user_password:
    if not specialchar. isalnum():
        special+=1
if charsize > 8 and char_upper > 0 and char_down > 0 and num > 0 and special > 0:
    print('Senha aceita!')
else:
    print('Senha recusada, esta deve conter caracteres especiais, números, letra minuscula e maiuscula.')
