'''
Exercício 15 - Escreva um programa que pergunte a quantidade de Km
percorridos por um carro alugado e a quantidade de dias pelos quais 
ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa
R$ 60,00 por dia e R$ 0.15 por Km rodado.
'''

qtd_km = float(input("Quantos quilômetros foram percorridos: "))
qtd_dias = int(input("Quantos dias o carro foi alugado: "))

valor = (qtd_dias * 60) + (qtd_km * 0.15)

print("O valor a ser pago é de R$ {}".format(valor))
