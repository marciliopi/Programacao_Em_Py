'''Escreva um programa que leia dois números e que pergunte qual
operação você deseja realizar. Você deve poder calcular a soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.'''
# -*- coding: utf-8 -*-
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
op = input('Qual operação você deseja realizar? (+, -, *, /): ')
if op == '+':
    resultado = n1 + n2
elif op == '-':
    resultado = n1 - n2   
elif op == '*':
    resultado = n1 * n2   
elif op == '/':
    resultado = n1 / n2
else:
    print('Operação inválida, digite números válidos')
print("O resultado da operação é ", resultado)