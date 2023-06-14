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

#Monta tabela objetivo
def monta_objetivo(tamanho=16):
	resultado = []
	for i in range(tamanho):
		x = 0
		if i < (tamanho - 1):
			x = i + 1
		resultado.append(x)
	tabela = monta_tabela(resultado)
	return tabela

#gerar tabela aleatória
def gerar_aleatoria(tamanho=16):
	resultado = []
	while len(resultado) < tamanho:
		numero = random.randrange(tamanho)
		insere = True
		for compara in resultado:
			if compara == numero:
				insere = False
		if insere:
			resultado.append(numero)
	tabela = monta_tabela(resultado)
	return tabela

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
	l = 0
	c = 0
	for x in vetor:
		for y in x:
			if y == 0:
				l = vetor.index(x)
				c = x.index(y)
	return l, c

#Função Objetivo: compara_objetivo
def compara_objetivo(atual, objetivo):
	valor_fit = 0
	vetor_atual = desmonta_tabela(atual)
	vetor_objetivo = desmonta_tabela(objetivo)
	for i in range(len(vetor_objetivo)):
		a = vetor_atual[i]
		o = vetor_objetivo[i]
		valor_fit += abs(a - o) * (i + 1)
	return valor_fit

#Função Expandir Vizinhança: expandir_vizinhanca
def expandir_vizinhanca(tabela):
	'''
	Movimento:
	(1) 0 = subir, 1 = descer, 2 = esquerda, 3 = direita
	(2) 4 = subir, 5 = descer, 6 = esquerda, 7 = direita
	(3) 8 = subir, 9 = descer, 10 = esquerda, 11 = direita
	'''
	l, c = acha_zero(tabela)
	#antes = copy.deepcopy(tabela)
	x = l
	y = c
	movimento = -1
	while movimento == -1:
		movimento = random.randrange(12)
		match movimento:
			case 0:
				#subir 1 linha
				if (l - 1) < 0:
					movimento = -1
				else:
					x = x - 1
			case 1:
				#descer 1 linha
				if (l + 1) > 3:
					movimento = -1
				else:
					x = x + 1
			case 2:
				#esquerda 1 coluna
				if (c - 1) < 0:
					movimento = -1
				else:
					y = y - 1
			case 3:
				#direita 1 coluna
				if (c + 1) > 3:
					movimento = -1
				else:
					y = y + 1
			case 4:
				#subir 2 linhas
				if (l - 2) < 0:
					movimento = -1
				else:
					x = x - 2
			case 5:
				#descer 2 linhas
				if (l + 2) > 3:
					movimento = -1
				else:
					x = x + 2
			case 6:
				#esquerda 2 colunas
				if (c - 2) < 0:
					movimento = -1
				else:
					y = y - 2
			case 7:
				#direita 2 colunas
				if (c + 2) > 3:
					movimento = -1
				else:
					y = y + 2
			case 8:
				#subir 3 linhas
				if (l - 3) < 0:
					movimento = -1
				else:
					x = x - 3
			case 9:
				#descer 3 linhas
				if (l + 3) > 3:
					movimento = -1
				else:
					x = x + 3
			case 10:
				#esquerda 3 colunas
				if (c - 3) < 0:
					movimento = -1
				else:
					y = y - 3
			case 11:
				#direita 3 colunas
				if (c + 3) > 3:
					movimento = -1
				else:
					y = y + 3
	if x != l:
		if l > x:
			inc = -1
		else:
			inc = 1
		for v in range(l, x, inc):
			if l > x:
				troca = tabela[(v - 1)][c]
			else:
				troca = tabela[(v + 1)][c]
			tabela[v][c] = troca
		tabela[x][c] = 0
	if y != c:
		if c > y:
			inc = -1
		else:
			inc = 1
		for v in range(c, y, inc):
			if c > y:
				troca = tabela[l][(v - 1)]
			else:
				troca = tabela[l][(v + 1)]
			tabela[l][v] = troca
		tabela[l][y] = 0
	#mostrar_array(antes, tabela)
	#input("Tecle algo para continuar...")
	return tabela

#Principal
tab_destino = monta_objetivo()
tab_atual = gerar_aleatoria()
mostrar_array(tab_atual, tab_destino)
input("Tecle Enter...")
inicio = time.time()
melhor = compara_objetivo(tab_atual, tab_destino)
tentativa = 0
tab_temp = copy.deepcopy(tab_atual)
while melhor > 0:
	tentativa += 1
	tab_vizinha = expandir_vizinhanca(tab_temp)
	novo_melhor = compara_objetivo(tab_vizinha, tab_destino)
	if novo_melhor < melhor:
		print(time.time() - inicio, "Tempo decorrido")
		print("Tentativa: ", tentativa)
		print("Melhor: ", melhor, "Novo Melhor: ", novo_melhor)
		tab_atual = copy.deepcopy(tab_vizinha)
		tab_temp = copy.deepcopy(tab_atual)
		melhor = novo_melhor
		mostrar_array(tab_atual, tab_destino)
		#input("Tecle Enter...")
	else:
		tab_temp = copy.deepcopy(tab_vizinha)
	tab_vizinha = []

print(time.time() - inicio, "Tempo decorrido (Final)")
