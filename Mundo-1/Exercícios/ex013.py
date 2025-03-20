# Exercício 13 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario_funcionario = float(input("Informe o salário do funcionário: R$ "))

salario_aumento = salario_funcionario + salario_funcionario * 0.15

print("O salário inidal de R$ {} do funcionário com aumento de 15% vai para R$ {}".format(salario_funcionario, salario_aumento))