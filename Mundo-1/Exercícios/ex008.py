# Exercício 8 - Escreva um programa que leia um valor em metros e o exiba em centímetro e milímetros
valor = float(input("Digite um valor em metros(m): "))

cent = valor * 100
mili = valor * 1000

print("{} metros é igual a {} centímetros e {} milímetros".format(valor, cent, mili))