#Escreva um programa que leia três números e que imprima o maior
#e o menor.
num1 = float(input("Digite o primeiro número..: "))
num2 = float(input("Digite o segundo número...: "))
num3 = float(input("Digite o terceiro número..: "))
if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num1 and num2 > num3:
    maior = num2
else:
    maior = num3
if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num1 and num2 < num3:
    menor = num2
else:
    menor = num3
print("O maior número é: ", maior)
print("O menor número é: ", menor)



