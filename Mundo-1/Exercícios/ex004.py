# Exercício 4 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

msg = input('Digite algo: ')

print('Tipo primitivo: {}'.format(type(msg)))
print('Só tem espaços? {}'.format(msg.isspace()))
print('É um número? {}'.format(msg.isnumeric()))
print('É alfabético? {}'.format(msg.isalpha()))
print('É alfanumérico? {}'.format(msg.isalnum()))
print('Está em maiúsculas? {}'.format(msg.isupper()))
print('Está em minúsculas? {}'.format(msg.islower()))
print('Está capitalizada? {}'.format(msg.istitle()))