'''Crie um programa que vai gerar cinco números aleatórios
e colocar em uma tupla.

Depois disos, mostre a listagem de números gerados e também
indique o menor e o maior valor'''

from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior número sorteado foi {max(numeros)}!')
print(f'O menor número sorteado foi {min(numeros)}!')


