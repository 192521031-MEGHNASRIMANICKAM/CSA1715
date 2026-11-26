import random

def fitness(x):
    return x * x

population = [random.randint(0, 31) for _ in range(10)]

for generation in range(20):
    population.sort(key=fitness, reverse=True)

    parents = population[:5]
    new_population = parents.copy()

    while len(new_population) < 10:
        p1, p2 = random.sample(parents, 2)
        child = (p1 + p2) // 2

        if random.random() < 0.1:
            child = random.randint(0, 31)

        new_population.append(child)

    population = new_population

best = max(population, key=fitness)

print("Best Solution:", best)
print("Maximum Fitness:", fitness(best))
