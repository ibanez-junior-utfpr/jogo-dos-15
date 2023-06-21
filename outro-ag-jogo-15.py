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
    retorno = -1
    if 0 in vetor:
        retorno = vetor.index(0)
    return retorno

#Função Objetivo: compara_objetivo
def compara_objetivo(vetor_atual, vetor_objetivo):
	valor_fit = 0
	for i in range(len(vetor_objetivo)):
		a = vetor_atual[i]
		o = vetor_objetivo[i]
		valor_fit += abs(a - o) * (i + 1)
	return valor_fit

def swap_tiles(board, pos1, pos2):
    new_board = board.copy()
    new_board[pos1], new_board[pos2] = new_board[pos2], new_board[pos1]
    return new_board

def create_population(population_size):
    population = []
    while len(population) < population_size:
        individual = list(range(0, 16))
        random.shuffle(individual)
        if individual not in population:
            population.append(individual)
    return population

def evaluate_population(population, destino):
    fitness_scores = []
    for individual in population:
        fitness_scores.append(compara_objetivo(individual, destino))
    return fitness_scores

def select_parents(population, fitness_scores):
    total_fitness = sum(fitness_scores)
    probabilities = [score / total_fitness for score in fitness_scores]
    parents = random.choices(population, probabilities, k=2)
    return parents

def crossover(parent1, parent2):
    crossover_point = random.randint(0, 15)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(individual, mutation_rate):
    for i in range(16):
        if random.random() < mutation_rate:
            blank_pos = acha_zero(individual)
            if blank_pos >= 0:
                individual[i], individual[blank_pos] = individual[blank_pos], individual[i]
    return individual

def evolve_population(population, fitness_scores, mutation_rate):
    new_population = []
    for _ in range(len(population) // 2):
        parent1, parent2 = select_parents(population, fitness_scores)
        child1, child2 = crossover(parent1, parent2)
        child1 = mutate(child1, mutation_rate)
        child2 = mutate(child2, mutation_rate)
        new_population.extend([child1, child2])
    return new_population

def genetic_algorithm(population_size, mutation_rate, max_generations, destino):
    population = create_population(population_size)
    for _ in range(max_generations):
        fitness_scores = evaluate_population(population, destino)
        best_individual = population[fitness_scores.index(min(fitness_scores))]
        if min(fitness_scores) == 0:
            return best_individual
        population = evolve_population(population, fitness_scores, mutation_rate)
    return best_individual

# Exemplo de uso
inicio = time.time()
population_size = 400
mutation_rate = 0.1
max_generations = 200
destino = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0 ]
solution = genetic_algorithm(population_size, mutation_rate, max_generations, destino)
print("Solução encontrada:")
mostrar_array(monta_tabela(solution), monta_tabela(destino))
print(time.time() - inicio, "Tempo decorrido (Final)")
