salario = float(input("Digite seu alário para o cálculo do impostp: "))
base = salario
imposto = 0
if base <= 1000:
    imposto = 0
if base > 1000 and base <= 3000:
    imposto = base * 0.20
if base > 3000:
    imposto = base * 0.35
print("Salário: R$%6.2f Imposto a pagar: R$%6.2f" % (salario, imposto))