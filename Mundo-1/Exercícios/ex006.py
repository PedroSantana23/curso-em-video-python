from math import sqrt
# Exercício 6 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

num = int(input("Digite um número: "))

double = num * 2
triple = num * 3
raiz = num**(1/2)

print("O número digitado foi: {}\nSeu dobro é {}\nSeu triplo é {}\nSua raiz quadrada é {}".format(num, double, triple, raiz))

# Com a biblioteca Math
raiz_math = sqrt(num)
print("Raiz com math: {}".format(raiz_math))