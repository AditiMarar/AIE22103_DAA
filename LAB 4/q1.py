def fractional_knapsack(benefits, weights, capacity):
    items = [(benefits[i], weights[i], benefits[i] / weights[i]) for i in range(len(benefits))]
    items.sort(key=lambda x: x[2], reverse=True)  # Sort items by value per unit weight in descending order

    optimal_vector = [0] * len(benefits)
    total_value = 0

    for value, weight, _ in items:
        if capacity >= weight:
            optimal_vector[benefits.index(value)] = 1
            total_value += value
            capacity -= weight
        else:
            fraction = capacity / weight
            optimal_vector[benefits.index(value)] = fraction
            total_value += fraction * value
            break

    return optimal_vector

benefits = [10, 15, 20]
weights = [2, 5, 4]
capacity = 8

optimal_vector = fractional_knapsack(benefits, weights, capacity)
print(optimal_vector)
max_benefit=0.0
for i in range(len(benefits)):
    max_benefit+=benefits[i]*optimal_vector[i]
print(max_benefit)
