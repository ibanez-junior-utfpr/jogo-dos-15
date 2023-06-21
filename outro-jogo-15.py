import random
import copy
import time

#Montar Tabela a partir de um vetor
def monta_tabela(vetor):
	l1 = [ vetor[0], vetor[1], vetor[2], vetor[3] ]
	l2 = [ vetor[4], vetor[5], vetor[6], vetor[7] ]
	l3 = [ vetor[8], vetor[9], vetor[10], vetor[11] ]
	l4 = [ vetor[12], vetor[13], vetor[14], vetor[15] ]
	tabela = [ l1, l2, l3, l4 ]
	return tabela

#Desmontar a Tabela e criar um vetor
def desmonta_tabela(tabela):
	vetor = []
	for x in tabela:
		for y in x:
			vetor.append(y)
	return vetor

#mostrar array 4x4 lado a lado
def mostrar_array(atual, destino):
	l1 = []
	l2 = []
	txt = "{:>5}"
	for x in atual:
		det = ""
		for y in x:
			det += txt.format(str(y))
		l1.append(det)
	for x in destino:
		det = ""
		for y in x:
			det += txt.format(str(y))
		l2.append(det)
	print("--------------------\t--------------------")
	for x in range(0, len(l1)):
		det = l1[x] + "\t" + l2[x]
		print(det)
	print("--------------------\t--------------------")

#Onde está o zero
def acha_zero(vetor):
	return vetor.index(0)

#Função Objetivo: compara_objetivo
def compara_objetivo(vetor_atual, vetor_objetivo):
	valor_fit = 0
	for i in range(len(vetor_objetivo)):
		a = vetor_atual[i]
		o = vetor_objetivo[i]
		valor_fit += abs(a - o) * (i + 1)
	return valor_fit

#Função Expandir Vizinhança: expandir_vizinhanca
def expandir_vizinhanca(vetor, final):
	movimento = -1
	posicao = acha_zero(vetor)
	while movimento == -1:
		movimento = random.randrange(16)
		if movimento != posicao:
			if vetor[movimento] - final[movimento] == 0:
				movimento = -1
			else:
				novo = movimento
		else:
			movimento = -1
	antigo = vetor[novo]
	vetor[posicao] = antigo
	vetor[novo] = 0
	return vetor

#Principal
vetor_destino = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
vetor_atual = copy.deepcopy(vetor_destino)
random.shuffle(vetor_atual)
print(vetor_destino)
print(vetor_atual)
mostrar_array(monta_tabela(vetor_atual), monta_tabela(vetor_destino))
input("Tecle Enter...")
inicio = time.time()
tentativa = 0
melhor = compara_objetivo(vetor_atual, vetor_destino)
while melhor > 0:
	tentativa += 1
	vetor_vizinho = expandir_vizinhanca(vetor_atual, vetor_destino)
	vetor_atual = copy.deepcopy(vetor_vizinho)
	novo_melhor = compara_objetivo(vetor_atual, vetor_destino)
	if novo_melhor < melhor:
		print(time.time() - inicio, "Tempo decorrido")
		print("Tentativa: ", tentativa)
		print("Melhor: ", melhor, "Novo Melhor: ", novo_melhor)
		melhor = novo_melhor
		mostrar_array(monta_tabela(vetor_atual), monta_tabela(vetor_destino))
		#input("Tecle Enter...")

print(time.time() - inicio, "Tempo decorrido (Final)")
