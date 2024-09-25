'''Podemos definir a média aritmética como a soma de vários números divididos
pela quantidade de números somados. Assim, se somarmos três números, 4, 5 e
6, teríamos a média aritmética como (4+5+6) / 3, onde 3 é a quantidade de nú-
meros. Se chamarmos o primeiro número de n1, o segundo de n2, e o terceiro de
n3, teremos (n1 + n2 + n3) / 3.
Vejamos um programa que calcula a média de cinco números digitados pelo usu-
ário na listagem 5.12. Se chamarmos o primeiro valor digitado de n1, o segundo
de n2, e assim sucessivamente, teremos que:
média = (n1+n2+n3+n4+n5)/5 = n1 + n2 + n3 + n4 + n5/5 
Em vez de utilizarmos cinco variáveis, vamos acumular os valores à medida que
são lidos.'''
x = 1
soma = 0
while x <= 5:
    n = int(input("Digite o %dº número:" % x))
    soma = soma + n
    x = x + 1
print("Média: %5.2f" % (soma/5))