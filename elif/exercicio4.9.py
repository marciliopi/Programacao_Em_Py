'''Escreva um programa para aprovar o empréstimo bancário para
compra de uma casa. O programa deve perguntar o valor da casa a comprar, o
salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.'''
valor_da_casa = float(input("Digite o valor da casa a comprar: "))
salario = float(input("Digite o seu salário: "))
anos = int(input("Digite a quantidade de anos a pagar: "))
meses = anos * 12
prestacao = valor_da_casa / meses
if prestacao > salario * 0.3:
    print("Empréstimo não aprovado.")
else:
    print("Empréstimo aprovado.")
    print("Valor da prestação é: R$%6.2f" % prestacao)



