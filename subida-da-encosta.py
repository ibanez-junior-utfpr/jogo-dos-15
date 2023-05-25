'''
Problema: Implementar um algoritimo subida
da Encosta para descobrir qual string foi
definida pelo usuário 
'''

import string
import random

#gerar-solução
def gerar_solucao(tamanho=5):
    lista = []
    for aux in range(tamanho):
        #Randomiza apenas letras (maiusculas ou minusculas)
        carac = random.choice(string.ascii_letters)
        lista.append(carac)
    return lista

#expandir-vizinhança
def expandir_vizinhanca(solucao, objetivo):
    #Laço para verificar se a posição já está com a letra correta
    ind = -1
    while ind == -1:
        ind = random.randint(0, len(solucao) - 1)
        s = solucao[ind]
        o = objetivo[ind]
        if abs(ord(s) - ord(o)) == 0:
            ind = -1
    #Randomiza apenas letras (maiusculas ou minusculas)
    solucao[ind] = random.choice(string.ascii_letters)
    return solucao

#função-objetivo
def funcao_objetivo(solucao, objetivo):
    valor_fit = 0
    for i in range(len(objetivo)):
        s = solucao[i]
        o = objetivo[i]
        valor_fit += abs(ord(s)-ord(o))
    return valor_fit

#fluxo
objetivo = list(input("Escolha um Objetivo (apenas letras): "))
best = gerar_solucao(len(objetivo))
best_score = funcao_objetivo(best, objetivo)
iterado = 0
while best_score > 0:
    iterado += 1
    nova_solucao = best
    #Na chamada da função expandir_vizinhanca estou passando a solucao e o objetivo
    expandir_vizinhanca(nova_solucao, objetivo)
    #Na chamada da função funcao_objetivo estou passando a solucao e o objetivo
    score_v = funcao_objetivo(nova_solucao, objetivo)
    if score_v < best_score:
        print("Interação: ", iterado)
        print("best: ", best, "best_score: ", best_score)
        print("Vizinho: ", nova_solucao, "Score Vizinho: ", score_v)
        best_score = score_v
        best = nova_solucao
