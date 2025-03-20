# Exercício 10 - Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
num = float(input("Digite quanto você tem na carteira: R$ "))

dolar = num/5.68

print("Com R$ {} na carteia você consegue comprar US$ {} dólares".format(num, dolar))