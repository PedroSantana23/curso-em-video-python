# Exercício 5 - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input("Digite um número: "))
ant = num - 1
suc = num + 1

print("O antecessor de {} é {} e o seu sucessor é {}".format(num, ant, suc))