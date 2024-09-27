def max_weights(N, M, capacities, items):
    results = []
    
    for capacity in capacities:
        total_weight = 0
        for price, weight in items:
            if price <= capacity:
                total_weight += weight
        results.append(total_weight)

    return results

N, M = 3, 4
capacities = [10, 20, 30]
items = [
    (5, 10),
    (15, 20),
    (10, 25),
    (20, 30)
]

result = max_weights(N, M, capacities, items)

print(" ".join(map(str, result)))  
