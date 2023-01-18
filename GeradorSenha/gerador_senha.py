import random

print('Seja bem vindo ao gerador de senhas')

caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%¨&*().,0123456789'

quantidade = input('Quantas senhas você quer gerar? ')
quantidade = int(quantidade)

tamanho = input('Quantos digitos você quer que a senha tenha? ')
tamanho = int(tamanho)

print('\naqui estão suas senhas: ')

for senha in range(quantidade):
    senhas = ''
    for i in range(tamanho):
        senhas += random.choice(caracteres)
    print(senhas)
