# Exercício 14 - Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

grau_celsius = float(input("Digite uma temperatura em graus °C: "))

grau_fahrenheit = (grau_celsius * 9/5) + 32

print("A temperatura {}°C é igual a {}°F".format(grau_celsius, grau_fahrenheit))

