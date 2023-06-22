import random
import time

class Particle:
    def __init__(self, board):
        self.board = board
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        distance = 0
        for i in range(len(self.board)):
            if self.board[i] != i + 1:
                distance += abs((i + 1) - self.board[i])
        return distance

def create_board():
    board = list(range(1, 16))
    random.shuffle(board)
    #board.append(0)
    return board

def initialize_particles(num_particles):
    particles = []
    for _ in range(num_particles):
        board = create_board()
        particle = Particle(board)
        particles.append(particle)
    return particles

def update_velocity(particle, global_best, inertia_weight, cognitive_weight, social_weight):
    velocity = []
    for i in range(15):
        r1 = random.random()
        r2 = random.random()
        cognitive_component = cognitive_weight * r1 * (particle.board[i] - particle.board[i])
        social_component = social_weight * r2 * (global_best[i] - particle.board[i])
        new_velocity = inertia_weight * particle.board[i] + cognitive_component + social_component
        velocity.append(new_velocity)
    return velocity

def update_position(particle, velocity):
    new_board = [0] * 15
    for i in range(15):
        new_pos = int((particle.board[i] + velocity[i]) % 15)
        while new_board[new_pos] != 0:
            new_pos = (new_pos + 1) % 15
        new_board[new_pos] = particle.board[i]
    particle.board = new_board

def update_fitness(particle):
    particle.fitness = particle.calculate_fitness()

def update_global_best(particles):
    global_best_fitness = float('inf')
    global_best_board = None
    for particle in particles:
        if particle.fitness < global_best_fitness:
            global_best_fitness = particle.fitness
            global_best_board = particle.board
    return global_best_board, global_best_fitness

def pso_algorithm(num_particles, num_iterations, inertia_weight, cognitive_weight, social_weight):
    particles = initialize_particles(num_particles)
    global_best, global_fitness = update_global_best(particles)
    for iterator in range(num_iterations):
        for particle in particles:
            velocity = update_velocity(particle, global_best, inertia_weight, cognitive_weight, social_weight)
            update_position(particle, velocity)
            update_fitness(particle)
        global_best, global_fitness = update_global_best(particles)
        if global_fitness == 0:
            break
    print("==============================")
    print("Iteração..: ", iterator)
    print("Melhor....: ", global_fitness)
    return global_best

# Exemplo de uso
num_particles = 500
num_iterations = 1000
inertia_weight = 0.5
cognitive_weight = 1.0
social_weight = 1.0

num_particles = input("Particulas [500]: ")
if num_particles == '': num_particles = '500'
num_particles = int(num_particles)
num_iterations = input("Iterações [1000]: ")
if num_iterations == '': num_iterations = '1000'
num_iterations = int(num_iterations)
inertia_weight = input("Inércia: [0.5]: ")
if inertia_weight == '': inertia_weight = '0.5'
inertia_weight = float(inertia_weight)
cognitive_weight = input("Cognição: [1.0]: ")
if cognitive_weight == '': cognitive_weight = '1.0'
cognitive_weight = float(cognitive_weight)
social_weight = input("Social: [1.0]: ")
if social_weight == '': social_weight = '1.0'
social_weight = float(social_weight)
print("==============================")
print("Particulas: ", num_particles)
print("Iterações.: ", num_iterations)
print("Inércia...: ", inertia_weight)
print("Cognição..: ", cognitive_weight)
print("Social....: ", social_weight)
inicio = time.time()
solution = pso_algorithm(num_particles, num_iterations, inertia_weight, cognitive_weight, social_weight)
solution.append(0)
print("Solução encontrada:")
for i in range(4):
    for j in range(4):
        print(solution[i*4 + j], end="\t")
    print("\n")
print(time.time() - inicio, "Tempo decorrido (Final)")
