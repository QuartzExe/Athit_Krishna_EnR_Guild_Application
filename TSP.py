def compute_total_cost(path, dist):
    cost = 0
    n = len(path)
    for i in range(n - 1):
        cost += dist[path[i]][path[i + 1]]
    return cost


def nearest_neighbour(dist, start=0):
    n = len(dist)
    visited = [False] * n
    path = [start]
    visited[start] = True

    current = start

    for step in range(n - 1):
        nearest = None
        min_dist = float('inf')

        for city in range(n):
            if not visited[city] and dist[current][city] < min_dist:
                min_dist = dist[current][city]
                nearest = city

        path.append(nearest)
        visited[nearest] = True
        current = nearest

    # return to start, regardless of the cost
    path.append(start)

    return path


def two_opt(path, dist):
    best_path = path[:]
    best_cost = compute_total_cost(best_path, dist)
    n = len(path)

    improved = True

    while improved:
        improved = False

        # iterating through all possible pair of paths in the current solution
        for i in range(1, n - 2):
            for j in range(i + 1, n - 1):

                new_path = best_path[:]
                
                # cut and reverse the segment between i and j
                new_path[i:j] = reversed(best_path[i:j])

                new_cost = compute_total_cost(new_path, dist)

                if new_cost < best_cost:
                    best_path = new_path
                    best_cost = new_cost
                    improved = True

        path = best_path

    return best_path, best_cost
