# Exercício 9 - Faça um programa que leia um número qualquer e mostre na tela a sua tabuada
num = int(input("Digite um número para saber sua tabuada: "))

print("Tabuada de {}:".format(num))
for i in range(1, 11, 1):
  result = num * i
  print("{} x {} = {}".format(num, i, result))