import random

def print_board(board):
    for i in range(4):
        for j in range(4):
            print(board[i*4 + j], end="\t")
        print("\n")

def get_blank_position(board):
    print(board)
    #input("Tecle algo...")
    return board.index(0)

def get_neighbors(board):
    neighbors = []
    blank_pos = get_blank_position(board)
    if blank_pos >= 4:
        neighbors.append(swap_tiles(board, blank_pos, blank_pos-4))
    if blank_pos < 12:
        neighbors.append(swap_tiles(board, blank_pos, blank_pos+4))
    if blank_pos % 4 != 0:
        neighbors.append(swap_tiles(board, blank_pos, blank_pos-1))
    if blank_pos % 4 != 3:
        neighbors.append(swap_tiles(board, blank_pos, blank_pos+1))
    return neighbors

def swap_tiles(board, pos1, pos2):
    new_board = board.copy()
    new_board[pos1], new_board[pos2] = new_board[pos2], new_board[pos1]
    return new_board

def manhattan_distance(board):
    distance = 0
    for i in range(4):
        for j in range(4):
            tile = board[i*4 + j]
            if tile != 0:
                target_row = (tile - 1) // 4
                target_col = (tile - 1) % 4
                distance += abs(i - target_row) + abs(j - target_col)
    return distance

def create_population(population_size):
    population = []
    for _ in range(population_size):
        individual = list(range(1, 16))
        random.shuffle(individual)
        individual.append(0)
        population.append(individual)
    print("population: ", population)
    input("Tecle algo...")
    return population

def evaluate_population(population):
    fitness_scores = []
    for individual in population:
        fitness_scores.append(manhattan_distance(individual))
    return fitness_scores

def select_parents(population, fitness_scores):
    total_fitness = sum(fitness_scores)
    probabilities = [score / total_fitness for score in fitness_scores]
    parents = random.choices(population, probabilities, k=2)
    return parents

def crossover(parent1, parent2):
    print("parent1: ", parent1)
    print("parent2: ", parent2)
    crossover_point = random.randint(0, 15)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    print("child1: ", child1)
    print("child2: ", child2)
    return child1, child2

def mutate(individual, mutation_rate):
    for i in range(16):
        if random.random() < mutation_rate:
            blank_pos = get_blank_position(individual)
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

def genetic_algorithm(population_size, mutation_rate, max_generations):
    population = create_population(population_size)
    for generation in range(max_generations):
        fitness_scores = evaluate_population(population)
        best_individual = population[fitness_scores.index(min(fitness_scores))]
        if min(fitness_scores) == 0:
            return best_individual
        population = evolve_population(population, fitness_scores, mutation_rate)
    return best_individual

# Exemplo de uso
population_size = 100
mutation_rate = 0.1
max_generations = 1000

solution = genetic_algorithm(population_size, mutation_rate, max_generations)
print("Solução encontrada:")
print_board(solution)
