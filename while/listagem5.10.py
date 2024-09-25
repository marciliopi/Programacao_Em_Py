'''Vejamos um programa para corrigir um teste de múltipla escolha com
três questões. A resposta da primeira é “b”; da segunda, “a”; e da terceira, “d”. O programa da listagem 5.10 conta um ponto a cada resposta correta.'''
pontos = 0
questao = 1
while questao <= 3:
    resposta = input("resposta da questão %d: " % questao)
    if questao == 1 and (resposta == "b" or resposta == "B"):
        pontos = pontos + 1
    if questao == 2 and (resposta == "a" or resposta == "A"):
        pontos = pontos + 1
    if questao == 3 and (resposta == "c"or resposta == "C"):
        pontos = pontos + 1
    questao += 1
print("O aluno fez %d ponto(s)" % pontos)