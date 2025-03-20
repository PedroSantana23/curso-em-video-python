'''
Exercício 11 - Faça um programa que leia a largura e a altura de uma parede em metros e calcule a sua áres e a quantidade de tinta necessária para
pintá-la, sabendo que cada litro de tinta pinta uma área de 2 m quadrados
'''

larg = float(input("Digite a largura da parede em metros(m): "))
alt = float(input("Digite a altura da parede em metros(m): "))

area = larg * alt
quant_tinta_l = area / 2

print("Dimensões da parede = {}m X {}m\nÁrea = {} metros quadrados\nQtd de tinta em Litros(l) = {} Litros".format(alt, larg, area, quant_tinta_l))
