import numpy as np

np.random.seed(42)

X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([[0], [1], [1], [0]])

def sigmoid(x):
    return 1 / (1 + np.exp(-np.clip(x, -50, 50)))

def neural_network(weights, X):
    w1 = weights[:8].reshape(2, 4)
    b1 = weights[8:12].reshape(1, 4)
    w2 = weights[12:16].reshape(4, 1)
    b2 = weights[16]

    hidden = sigmoid(np.dot(X, w1) + b1)
    output = sigmoid(np.dot(hidden, w2) + b2)

    return output

def fitness(weights):
    predictions = neural_network(weights, X)
    error = np.mean((y - predictions) ** 2)
    return 1 / (error + 0.001)

population_size = 50
generations = 500
population = np.random.uniform(-5, 5, (population_size, 17))

for generation in range(generations):
    scores = np.array([fitness(ind) for ind in population])

    best_index = np.argmax(scores)
    best = population[best_index]

    new_population = [best.copy()]

    while len(new_population) < population_size:
        parents = population[
            np.random.choice(population_size, 2, replace=False)
        ]

        crossover_point = np.random.randint(1, 17)

        child = np.concatenate((
            parents[0][:crossover_point],
            parents[1][crossover_point:]
        ))

        mutation = np.random.normal(0, 0.2, 17)
        child += mutation

        new_population.append(child)

    population = np.array(new_population)

best_index = np.argmax([fitness(ind) for ind in population])
best_weights = population[best_index]

predictions = neural_network(best_weights, X)

print("Genetic Algorithm Completed")
print("\nXOR Predictions:")

for inputs, output in zip(X, predictions):
    print(inputs, "->", round(float(output[0]), 3))

print("\nFinal Fitness:", round(fitness(best_weights), 4))
