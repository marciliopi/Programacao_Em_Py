'''Escreva um programa que calcule o preço a pagar pelo fornecimento
de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.'''
consumo = float(input("Digite a quantidade de kW/h consumido: "))
tipo = input("Digite o tipo de instalação (R, C, I): ")
if tipo == "R":
    if consumo <= 500:
        preco = consumo * 0.40
    else:
        preco = consumo * 0.65
if tipo == "C":
    if consumo <= 1000:
        preco = consumo * 0.55
    else:
        preco = consumo * 0.60
if tipo == "I":
    if consumo <= 5000:
        preco = consumo * 0.55
    else:
        preco = consumo * 0.60
print("O preço a pagar é de R$%6.2f" % preco)
