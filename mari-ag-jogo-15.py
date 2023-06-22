import random
import time

# Função de Avaliação
def avaliar_individuo(individuo):
    aptidao = 0
    for i in range(len(individuo)):
        if individuo[i] != i + 1:
            aptidao += abs((i + 1) - individuo[i])
    return aptidao

# Função de Crossover (Recombinação)
def crossover(individuo1, individuo2):
    ponto_corte = random.randint(1, len(individuo1) - 2)
    filho1 = individuo1[:ponto_corte] + individuo2[ponto_corte:]
    filho2 = individuo2[:ponto_corte] + individuo1[ponto_corte:]
    return filho1, filho2

# Função de Mutação
def mutacao(individuo):
    gene1 = random.randint(0, len(individuo) - 1)
    gene2 = random.randint(0, len(individuo) - 1)
    individuo[gene1], individuo[gene2] = individuo[gene2], individuo[gene1]
    return individuo

# Algoritmo Genético
def algoritmo_genetico(tamanho_populacao, geracoes):
    populacao = []
    for _ in range(tamanho_populacao):
        individuo = list(range(1, 16))
        random.shuffle(individuo)
        populacao.append(individuo)

    for geracao in range(geracoes):
        populacao = sorted(populacao, key=lambda x: avaliar_individuo(x))
        if avaliar_individuo(populacao[0]) == 0:
            break

        proxima_geracao = populacao[:int(tamanho_populacao/2)]

        for _ in range(int(tamanho_populacao/2)):
            pai1 = random.choice(populacao[:int(tamanho_populacao/2)])
            pai2 = random.choice(populacao[:int(tamanho_populacao/2)])
            filho1, filho2 = crossover(pai1, pai2)
            proxima_geracao.append(mutacao(filho1))
            proxima_geracao.append(mutacao(filho2))

        populacao = proxima_geracao

    print("Geração: ", geracao)
    return populacao[0]

# Testando o algoritmo genético
tamanho_populacao = input("População [200]: ")
if tamanho_populacao == '': tamanho_populacao = '200'
tamanho_populacao = int(tamanho_populacao)
geracoes = input("Gerações [100]: ")
if geracoes == '': geracoes = '100'
geracoes = int(geracoes)
print("==============================")
print("População: ", tamanho_populacao)
print("Gerações.: ", geracoes)
inicio = time.time()
solucao = algoritmo_genetico(tamanho_populacao, geracoes)
print("Avaliação: ", avaliar_individuo(solucao))
solucao.append(0)
print("Solução encontrada:", solucao)
# Exibindo os números aleatórios gerados em forma de grade
print("\nNúmeros gerados em forma de grade:")
for i in range(4):
    for j in range(4):
        print(solucao[i*4 + j], end="\t")
    print()
print(time.time() - inicio, "Tempo decorrido (Final)")
