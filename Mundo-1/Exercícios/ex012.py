# Exercício 12 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preco = float(input("Digite o preço do produto: R$ "))

preco_desconto = preco - preco * 0.15

print("O preço R$ {} no produto fica por R$ {} ao aplicar 15% de desconto.".format(preco, preco_desconto))