import numpy as np
import ga

# Y = w1x1 + w2x2 + w3x3 + w4x4 + w5x5 + w6x6

# Inputs of the equation.
equation_inputs = [4, -2, 3.5, 5, -11, -4.7]

# Number of the weights we are looking to optimize.
num_weights = 6

# Number of chromosomes (solution or individual) per population
sol_per_pop = 8

# Defining the population size.
# The population will have sol_per_pop chromosome where each chromosome has num_weights genes.
pop_size = (sol_per_pop, num_weights)

# Creating the initial population.
new_population = np.random.uniform(low=-4.0, high=4.0, size=pop_size)

print(new_population)

# Hyperparameters
num_generations = 5

num_parents_mating = 4

for generation in range(num_generations):
    # Measuring the fitness of each chromosome in the population.
    fitness = ga.cal_pop_fitness(equation_inputs, new_population)

    print(f"fitness = \n{fitness}\n")

    # Selecting the best parents in the population for mating.
    parents = ga.select_mating_pool(new_population, fitness,
                                    num_parents_mating)

    # Generating next generation using crossover.
    offspring_crossover = ga.crossover(parents,
                                       offspring_size=(pop_size[0]-parents.shape[0], num_weights))

    # Adding some variations to the offsrping using mutation.
    offspring_mutation = ga.mutation(offspring_crossover)

    # Creating the new population based on the parents and offspring.
    new_population[0:parents.shape[0], :] = parents
    new_population[parents.shape[0]:, :] = offspring_mutation

    print(f"new_population = \n{new_population}")

