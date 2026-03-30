nodes = ['A', 'B', 'C']
paths = [
    ('A', 'B', 4),
    ('A', 'C', 5),
    ('B', 'C', -10)
]


dist = {node: float('inf') for node in nodes}
dist['A'] = 0


# Relaxing paths V-1 times:

for i in range(len(nodes) - 1):
    for u, v, w in paths:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w


# Checking for negative cycles:
    
for u, v, w in paths:
    if dist[u] + w < dist[v]:
        print("Negative weight cycle detected!")
        break
else:
    print("No negative weight cycle.")
    print("\nFinal shortest distances from A:")
    print(dist)

