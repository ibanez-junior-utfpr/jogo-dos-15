import random

class Particle:
    def __init__(self, board):
        self.board = board
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        distance = 0
        for i in range(4):
            for j in range(4):
                tile = self.board[i*4 + j]
                if tile != 0:
                    target_row = (tile - 1) // 4
                    target_col = (tile - 1) % 4
                    distance += abs(i - target_row) + abs(j - target_col)
        return distance

def create_board():
    board = list(range(1, 16))
    random.shuffle(board)
    board.append(0)
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
    for i in range(16):
        r1 = random.random()
        r2 = random.random()
        cognitive_component = cognitive_weight * r1 * (particle.board[i] - particle.board[i])
        social_component = social_weight * r2 * (global_best[i] - particle.board[i])
        new_velocity = inertia_weight * particle.board[i] + cognitive_component + social_component
        velocity.append(new_velocity)
    return velocity

def update_position(particle, velocity):
    new_board = [0] * 16
    for i in range(16):
        new_pos = (particle.board[i] + velocity[i]) % 16
        while new_board[new_pos] != 0:
            new_pos = (new_pos + 1) % 16
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
    return global_best_board

def pso_algorithm(num_particles, num_iterations, inertia_weight, cognitive_weight, social_weight):
    particles = initialize_particles(num_particles)
    global_best = update_global_best(particles)
    for _ in range(num_iterations):
        for particle in particles:
            velocity = update_velocity(particle, global_best, inertia_weight, cognitive_weight, social_weight)
            update_position(particle, velocity)
            update_fitness(particle)
        global_best = update_global_best(particles)
    return global_best

# Exemplo de uso
num_particles = 20
num_iterations = 100
inertia_weight = 0.5
cognitive_weight = 1.0
social_weight = 1.0

solution = pso_algorithm(num_particles, num_iterations, inertia_weight, cognitive_weight, social_weight)
print("Solução encontrada:")
for i in range(4):
    for j in range(4):
        print(solution[i*4 + j], end="\t")
    print("\n")
