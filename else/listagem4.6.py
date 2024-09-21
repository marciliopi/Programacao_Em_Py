minutos = int(input("Qauntos minutos você utilizou este mês: "))
if minutos <= 200:
    preco = 0.20
    print("Você vai pagar este mês: R$%6.2f" % (minutos * preco))
else:
    if minutos >= 201 and minutos <= 400:
        preco = 0.18
    else:
        preco = 0.15
    print("Você vai pagar este mês: R$%6.2f" % (minutos * preco))