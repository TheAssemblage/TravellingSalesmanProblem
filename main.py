import numpy as np
import random
import matplotlib.pyplot as plt

matrix = np.array([
    [0, 7, 4, 2, 5, 5, 2, 6, 3, 4, 6, 3, 3, 7, 3, 9, 10, 8, 4, 6, 2, 10, 9, 9, 3, 6, 1, 5, 4, 2, 2, 5, 1, 6, 5, 7, 7, 7,
     1, 1, 4, 6, 7, 5, 9, 8, 10, 6, 4, 2],
    [7, 0, 7, 8, 5, 1, 3, 2, 3, 5, 6, 5, 9, 6, 10, 7, 10, 3, 7, 3, 7, 7, 1, 3, 3, 7, 9, 4, 8, 7, 1, 7, 4, 10, 1, 5, 5,
     5, 8, 4, 8, 5, 1, 2, 8, 5, 2, 4, 7, 2],
    [4, 7, 0, 8, 3, 10, 3, 8, 2, 3, 1, 6, 7, 6, 5, 7, 7, 7, 7, 10, 3, 8, 3, 2, 7, 5, 5, 7, 8, 4, 7, 5, 9, 9, 3, 7, 6, 6,
     9, 3, 4, 2, 10, 7, 5, 7, 6, 7, 6, 8],
    [2, 8, 8, 0, 6, 10, 3, 2, 2, 1, 5, 5, 4, 8, 7, 8, 10, 10, 2, 2, 7, 1, 6, 6, 9, 5, 4, 7, 8, 6, 4, 2, 6, 3, 1, 8, 3,
     5, 7, 4, 8, 4, 7, 8, 5, 1, 4, 5, 3, 2],
    [5, 5, 3, 6, 0, 9, 5, 9, 4, 8, 4, 9, 8, 4, 3, 8, 10, 4, 7, 5, 9, 8, 2, 9, 10, 6, 9, 6, 2, 2, 5, 8, 9, 8, 4, 6, 1, 2,
     2, 7, 5, 2, 5, 2, 1, 9, 6, 10, 7, 6],
    [5, 1, 10, 10, 9, 0, 9, 9, 10, 1, 9, 7, 10, 6, 5, 9, 3, 5, 10, 6, 9, 8, 6, 3, 7, 1, 7, 7, 8, 9, 10, 8, 6, 10, 6, 1,
     2, 9, 5, 9, 3, 6, 7, 1, 7, 4, 1, 5, 2, 2],
    [2, 3, 3, 3, 5, 9, 0, 3, 2, 2, 1, 7, 3, 6, 7, 5, 6, 5, 2, 5, 9, 9, 3, 3, 6, 7, 5, 3, 10, 1, 2, 2, 2, 7, 6, 1, 10, 8,
     8, 1, 9, 10, 10, 9, 8, 6, 2, 4, 2, 1],
    [6, 2, 8, 2, 9, 9, 3, 0, 10, 4, 3, 4, 5, 7, 1, 9, 6, 9, 4, 5, 1, 2, 7, 4, 9, 2, 10, 6, 8, 10, 3, 5, 5, 8, 9, 2, 2,
     4, 1, 6, 4, 2, 3, 10, 7, 5, 10, 2, 8, 8],
    [3, 3, 2, 2, 4, 10, 2, 10, 0, 6, 2, 6, 3, 2, 3, 9, 1, 3, 1, 5, 1, 9, 2, 1, 4, 5, 2, 10, 4, 3, 1, 3, 1, 6, 8, 7, 1,
     1, 8, 10, 6, 2, 9, 4, 3, 8, 1, 1, 7, 7],
    [4, 5, 3, 1, 8, 1, 2, 4, 6, 0, 6, 8, 8, 8, 3, 7, 6, 4, 1, 8, 4, 7, 8, 2, 2, 6, 5, 9, 8, 8, 1, 1, 1, 8, 10, 7, 2, 8,
     2, 2, 7, 4, 7, 8, 6, 8, 3, 8, 10, 9],
    [6, 6, 1, 5, 4, 9, 1, 3, 2, 6, 0, 1, 4, 4, 7, 6, 8, 4, 3, 1, 8, 3, 4, 6, 3, 7, 5, 2, 8, 2, 3, 3, 6, 1, 5, 2, 2, 8,
     3, 7, 10, 5, 7, 8, 5, 7, 2, 10, 2, 3],
    [3, 5, 6, 5, 9, 7, 7, 4, 6, 8, 1, 0, 8, 5, 8, 4, 3, 1, 7, 5, 5, 7, 1, 4, 8, 7, 2, 2, 1, 1, 5, 7, 8, 6, 2, 7, 2, 2,
     1, 2, 2, 2, 4, 4, 3, 3, 9, 8, 6, 2],
    [3, 9, 7, 4, 8, 10, 3, 5, 3, 8, 4, 8, 0, 3, 1, 10, 8, 6, 4, 2, 7, 10, 2, 3, 4, 1, 7, 5, 10, 5, 7, 2, 4, 2, 8, 9, 4,
     7, 3, 6, 9, 6, 4, 3, 5, 5, 4, 6, 8, 5],
    [7, 6, 6, 8, 4, 6, 6, 7, 2, 8, 4, 5, 3, 0, 5, 2, 1, 3, 4, 7, 10, 10, 5, 3, 8, 8, 8, 8, 2, 7, 5, 3, 1, 9, 2, 2, 7, 9,
     6, 8, 2, 10, 6, 7, 1, 9, 8, 2, 6, 4],
    [3, 10, 5, 7, 3, 5, 7, 1, 3, 3, 7, 8, 1, 5, 0, 6, 4, 5, 2, 3, 1, 10, 7, 10, 2, 10, 8, 6, 5, 3, 8, 3, 1, 8, 7, 8, 7,
     5, 4, 9, 4, 9, 8, 9, 6, 7, 10, 5, 1, 9],
    [9, 7, 7, 8, 8, 9, 5, 9, 9, 7, 6, 4, 10, 2, 6, 0, 7, 4, 10, 3, 7, 7, 4, 2, 1, 5, 2, 8, 4, 9, 8, 6, 2, 10, 3, 10, 3,
     4, 1, 7, 2, 1, 8, 4, 7, 4, 7, 1, 10, 9],
    [10, 10, 7, 10, 10, 3, 6, 6, 1, 6, 8, 3, 8, 1, 4, 7, 0, 8, 9, 4, 7, 6, 6, 3, 3, 5, 3, 9, 10, 1, 6, 1, 9, 10, 1, 10,
     1, 7, 8, 6, 9, 9, 7, 2, 3, 2, 1, 2, 7, 10],
    [8, 3, 7, 10, 4, 5, 5, 9, 3, 4, 4, 1, 6, 3, 5, 4, 8, 0, 4, 5, 10, 10, 7, 10, 8, 4, 7, 3, 3, 7, 6, 5, 7, 8, 6, 6, 6,
     6, 1, 8, 10, 4, 10, 4, 9, 5, 5, 3, 2, 4],
    [4, 7, 7, 2, 7, 10, 2, 4, 1, 1, 3, 7, 4, 4, 2, 10, 9, 4, 0, 8, 8, 7, 1, 9, 10, 8, 1, 4, 8, 8, 3, 3, 7, 5, 7, 3, 2,
     9, 8, 10, 2, 2, 1, 5, 2, 9, 1, 1, 6, 8],
    [6, 3, 10, 2, 5, 6, 5, 5, 5, 8, 1, 5, 2, 7, 3, 3, 4, 5, 8, 0, 4, 2, 4, 3, 6, 10, 7, 2, 4, 1, 6, 5, 10, 9, 5, 9, 2,
     4, 10, 10, 8, 7, 4, 10, 2, 8, 7, 9, 4, 8],
    [2, 7, 3, 7, 9, 9, 9, 1, 1, 4, 8, 5, 7, 10, 1, 7, 7, 10, 8, 4, 0, 9, 4, 6, 10, 6, 4, 7, 4, 8, 5, 5, 7, 10, 4, 9, 8,
     10, 1, 4, 7, 3, 3, 8, 7, 6, 7, 1, 4, 5],
    [10, 7, 8, 1, 8, 8, 9, 2, 9, 7, 3, 7, 10, 10, 10, 7, 6, 10, 7, 2, 9, 0, 3, 8, 9, 3, 8, 2, 9, 2, 6, 4, 9, 6, 5, 9, 4,
     5, 10, 1, 10, 2, 7, 6, 7, 4, 7, 9, 1, 1],
    [9, 1, 3, 6, 2, 6, 3, 7, 2, 8, 4, 1, 2, 5, 7, 4, 6, 7, 1, 4, 4, 3, 0, 10, 7, 3, 5, 2, 3, 3, 4, 2, 4, 2, 9, 1, 10, 4,
     1, 4, 8, 8, 6, 7, 9, 1, 4, 1, 2, 8],
    [9, 3, 2, 6, 9, 3, 3, 4, 1, 2, 6, 4, 3, 3, 10, 2, 3, 10, 9, 3, 6, 8, 10, 0, 8, 9, 6, 1, 10, 9, 3, 6, 10, 8, 9, 5, 5,
     6, 3, 8, 6, 7, 4, 2, 5, 4, 8, 8, 7, 2],
    [3, 3, 7, 9, 10, 7, 6, 9, 4, 2, 3, 8, 4, 8, 2, 1, 3, 8, 10, 6, 10, 9, 7, 8, 0, 1, 6, 4, 10, 10, 3, 9, 9, 6, 9, 10,
     6, 8, 6, 1, 5, 7, 6, 4, 10, 9, 9, 4, 6, 9],
    [6, 7, 5, 5, 6, 1, 7, 2, 5, 6, 7, 7, 1, 8, 10, 5, 5, 4, 8, 10, 6, 3, 3, 9, 1, 0, 10, 7, 3, 7, 1, 5, 7, 10, 9, 5, 8,
     5, 10, 10, 9, 4, 5, 3, 8, 9, 10, 6, 6, 2],
    [1, 9, 5, 4, 9, 7, 5, 10, 2, 5, 5, 2, 7, 8, 8, 2, 3, 7, 1, 7, 4, 8, 5, 6, 6, 10, 0, 9, 5, 3, 9, 8, 9, 3, 7, 7, 2, 5,
     3, 8, 3, 9, 9, 4, 5, 7, 9, 7, 6, 4],
    [5, 4, 7, 7, 6, 7, 3, 6, 10, 9, 2, 2, 5, 8, 6, 8, 9, 3, 4, 2, 7, 2, 2, 1, 4, 7, 9, 0, 5, 8, 9, 8, 1, 7, 5, 5, 2, 9,
     4, 3, 4, 4, 6, 6, 4, 4, 6, 7, 10, 8],
    [4, 8, 8, 8, 2, 8, 10, 8, 4, 8, 8, 1, 10, 2, 5, 4, 10, 3, 8, 4, 4, 9, 3, 10, 10, 3, 5, 5, 0, 5, 9, 2, 1, 1, 2, 4, 4,
     1, 6, 1, 2, 7, 9, 10, 6, 10, 6, 6, 4, 5],
    [2, 7, 4, 6, 2, 9, 1, 10, 3, 8, 2, 1, 5, 7, 3, 9, 1, 7, 8, 1, 8, 2, 3, 9, 10, 7, 3, 8, 5, 0, 5, 1, 9, 1, 5, 9, 4, 7,
     9, 9, 10, 2, 3, 9, 6, 6, 7, 9, 6, 3],
    [2, 1, 7, 4, 5, 10, 2, 3, 1, 1, 3, 5, 7, 5, 8, 8, 6, 6, 3, 6, 5, 6, 4, 3, 3, 1, 9, 9, 9, 5, 0, 5, 5, 10, 7, 7, 8, 4,
     6, 6, 2, 6, 7, 5, 9, 8, 4, 5, 4, 8],
    [5, 7, 5, 2, 8, 8, 2, 5, 3, 1, 3, 7, 2, 3, 3, 6, 1, 5, 3, 5, 5, 4, 2, 6, 9, 5, 8, 8, 2, 1, 5, 0, 8, 5, 7, 10, 8, 8,
     2, 4, 6, 5, 1, 3, 9, 1, 9, 1, 7, 6],
    [1, 4, 9, 6, 9, 6, 2, 5, 1, 1, 6, 8, 4, 1, 1, 2, 9, 7, 7, 10, 7, 9, 4, 10, 9, 7, 9, 1, 1, 9, 5, 8, 0, 3, 6, 2, 7, 6,
     1, 1, 2, 1, 5, 9, 7, 6, 9, 1, 10, 2],
    [6, 10, 9, 3, 8, 10, 7, 8, 6, 8, 1, 6, 2, 9, 8, 10, 10, 8, 5, 9, 10, 6, 2, 8, 6, 10, 3, 7, 1, 1, 10, 5, 3, 0, 6, 2,
     6, 1, 8, 9, 10, 10, 6, 3, 2, 6, 6, 8, 1, 7],
    [5, 1, 3, 1, 4, 6, 6, 9, 8, 10, 5, 2, 8, 2, 7, 3, 1, 6, 7, 5, 4, 5, 9, 9, 9, 9, 7, 5, 2, 5, 7, 7, 6, 6, 0, 6, 2, 10,
     6, 5, 10, 7, 5, 9, 6, 6, 7, 4, 3, 6],
    [7, 5, 7, 8, 6, 1, 1, 2, 7, 7, 2, 7, 9, 2, 8, 10, 10, 6, 3, 9, 9, 9, 1, 5, 10, 5, 7, 5, 4, 9, 7, 10, 2, 2, 6, 0, 9,
     5, 2, 5, 4, 5, 9, 5, 4, 4, 2, 3, 1, 5],
    [7, 5, 6, 3, 1, 2, 10, 2, 1, 2, 2, 2, 4, 7, 7, 3, 1, 6, 2, 2, 8, 4, 10, 5, 6, 8, 2, 2, 4, 4, 8, 8, 7, 6, 2, 9, 0, 3,
     3, 5, 2, 5, 8, 3, 8, 1, 4, 1, 3, 1],
    [7, 5, 6, 5, 2, 9, 8, 4, 1, 8, 8, 2, 7, 9, 5, 4, 7, 6, 9, 4, 10, 5, 4, 6, 8, 5, 5, 9, 1, 7, 4, 8, 6, 1, 10, 5, 3, 0,
     2, 2, 3, 2, 2, 6, 10, 10, 3, 5, 4, 6],
    [1, 8, 9, 7, 2, 5, 8, 1, 8, 2, 3, 1, 3, 6, 4, 1, 8, 1, 8, 10, 1, 10, 1, 3, 6, 10, 3, 4, 6, 9, 6, 2, 1, 8, 6, 2, 3,
     2, 0, 3, 1, 5, 2, 1, 10, 5, 10, 8, 1, 7],
    [1, 4, 3, 4, 7, 9, 1, 6, 10, 2, 7, 2, 6, 8, 9, 7, 6, 8, 10, 10, 4, 1, 4, 8, 1, 10, 8, 3, 1, 9, 6, 4, 1, 9, 5, 5, 5,
     2, 3, 0, 8, 7, 6, 3, 8, 3, 4, 9, 9, 5],
    [4, 8, 4, 8, 5, 3, 9, 4, 6, 7, 10, 2, 9, 2, 4, 2, 9, 10, 2, 8, 7, 10, 8, 6, 5, 9, 3, 4, 2, 10, 2, 6, 2, 10, 10, 4,
     2, 3, 1, 8, 0, 4, 7, 10, 10, 6, 4, 9, 5, 10],
    [6, 5, 2, 4, 2, 6, 10, 2, 2, 4, 5, 2, 6, 10, 9, 1, 9, 4, 2, 7, 3, 2, 8, 7, 7, 4, 9, 4, 7, 2, 6, 5, 1, 10, 7, 5, 5,
     2, 5, 7, 4, 0, 1, 6, 8, 2, 4, 2, 4, 5],
    [7, 1, 10, 7, 5, 7, 10, 3, 9, 7, 7, 4, 4, 6, 8, 8, 7, 10, 1, 4, 3, 7, 6, 4, 6, 5, 9, 6, 9, 3, 7, 1, 5, 6, 5, 9, 8,
     2, 2, 6, 7, 1, 0, 6, 1, 6, 3, 3, 3, 2],
    [5, 2, 7, 8, 2, 1, 9, 10, 4, 8, 8, 4, 3, 7, 9, 4, 2, 4, 5, 10, 8, 6, 7, 2, 4, 3, 4, 6, 10, 9, 5, 3, 9, 3, 9, 5, 3,
     6, 1, 3, 10, 6, 6, 0, 10, 10, 9, 8, 2, 4],
    [9, 8, 5, 5, 1, 7, 8, 7, 3, 6, 5, 3, 5, 1, 6, 7, 3, 9, 2, 2, 7, 7, 9, 5, 10, 8, 5, 4, 6, 6, 9, 9, 7, 2, 6, 4, 8, 10,
     10, 8, 10, 8, 1, 10, 0, 2, 1, 4, 7, 7],
    [8, 5, 7, 1, 9, 4, 6, 5, 8, 8, 7, 3, 5, 9, 7, 4, 2, 5, 9, 8, 6, 4, 1, 4, 9, 9, 7, 4, 10, 6, 8, 1, 6, 6, 6, 4, 1, 10,
     5, 3, 6, 2, 6, 10, 2, 0, 6, 5, 3, 6],
    [10, 2, 6, 4, 6, 1, 2, 10, 1, 3, 2, 9, 4, 8, 10, 7, 1, 5, 1, 7, 7, 7, 4, 8, 9, 10, 9, 6, 6, 7, 4, 9, 9, 6, 7, 2, 4,
     3, 10, 4, 4, 4, 3, 9, 1, 6, 0, 8, 8, 6],
    [6, 4, 7, 5, 10, 5, 4, 2, 1, 8, 10, 8, 6, 2, 5, 1, 2, 3, 1, 9, 1, 9, 1, 8, 4, 6, 7, 7, 6, 9, 5, 1, 1, 8, 4, 3, 1, 5,
     8, 9, 9, 2, 3, 8, 4, 5, 8, 0, 8, 7],
    [4, 7, 6, 3, 7, 2, 2, 8, 7, 10, 2, 6, 8, 6, 1, 10, 7, 2, 6, 4, 4, 1, 2, 7, 6, 6, 6, 10, 4, 6, 4, 7, 10, 1, 3, 1, 3,
     4, 1, 9, 5, 4, 3, 2, 7, 3, 8, 8, 0, 2],
    [2, 2, 8, 2, 6, 2, 1, 8, 7, 9, 3, 2, 5, 4, 9, 9, 10, 4, 8, 8, 5, 1, 8, 2, 9, 2, 4, 8, 5, 3, 8, 6, 2, 7, 6, 5, 1, 6,
     7, 5, 10, 5, 2, 4, 7, 6, 6, 7, 2, 0]
])


# Step 1: Random Initial Solution

def random_initial_solution(num_cities):
    return random.sample(range(num_cities), num_cities)


# Step 2: Neighborhood Operator (swap two adjacent cities)
def swap_adjacent_cities(path):
    new_path = path[:]
    idx = random.randint(0, len(path) - 2)
    new_path[idx], new_path[idx + 1] = new_path[idx + 1], new_path[idx]
    return new_path


# Step 3: Solution Evaluation
def evaluate_solution(matrix, path):
    cost = 0
    for i in range(len(path) - 1):
        cost += matrix[path[i]][path[i + 1]]
    # Add the cost of returning to the starting city
    cost += matrix[path[-1]][path[0]]
    return cost


# Step 4: Hill-Climbing Algorithm
def hill_climbing(matrix, initial_solution, max_no_improvement=25):
    current_solution = initial_solution
    current_cost = evaluate_solution(matrix, current_solution)

    no_improvement_steps = 0
    cost_history = [current_cost]

    while no_improvement_steps < max_no_improvement:
        new_solution = swap_adjacent_cities(current_solution)
        new_cost = evaluate_solution(matrix, new_solution)

        if new_cost < current_cost:
            current_solution = new_solution
            current_cost = new_cost
            no_improvement_steps = 0  # Reset counter when an improvement is found
        else:
            no_improvement_steps += 1

        cost_history.append(current_cost)

    return current_solution, current_cost, cost_history


# Step 5: Running the Algorithm 10 Times and Plotting the Results
num_runs = 10
results = []

for i in range(num_runs):
    initial_solution = random_initial_solution(len(matrix))
    final_solution, final_cost, cost_history = hill_climbing(matrix, initial_solution)
    results.append((final_solution, final_cost, cost_history))
    print(f"Run {i + 1}: Best distance = {final_cost}, Iterations = {len(cost_history)}")

# Plot the convergence of the cost function
for i, (_, _, cost_history) in enumerate(results):
    plt.plot(cost_history, label=f'Run {i + 1}')

plt.xlabel('Iteration')
plt.ylabel('Cost')
plt.title('Convergence of Cost Function - Random Approach Initial Solution')
plt.legend()
plt.show()
