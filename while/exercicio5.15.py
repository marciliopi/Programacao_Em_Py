apagar = 0
while True:
    codigo_produto = int(input("Código da mercadoria (Digite 0 para sair): "))
    preco = 0
    if codigo_produto == 0:
        break
    elif codigo_produto == 1:
        preco = 0.50
    elif codigo_produto == 2:
        preco = 1.00
    elif codigo_produto == 3:
        preco = 4.00
    elif codigo_produto == 5:
        preco = 7.00
    elif codigo_produto == 9:
        preco = 8.00
    else:
        print("Código inválido!")
    if preco != 0:
        quantidade_comprada = int(input("Quantidade: "))
        apagar = apagar + (preco * quantidade_comprada)
print(f"Total a pagar R${apagar:8.2f}")
