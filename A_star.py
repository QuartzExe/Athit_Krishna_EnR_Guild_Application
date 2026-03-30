import heapq

ROWS, COLS = 3, 3

start = (0, 0)
goal = (2, 2)

# Heuristic function (standard Manhattan distance)
def h(node):
    x, y = node
    gx, gy = goal
    return abs(gx - x) + abs(gy - y)


# The below function gives us a list of a given node's neighbours
def get_neighbors(node):
    x, y = node
    neighbors = []

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < ROWS and 0 <= ny < COLS:
            neighbors.append(((nx, ny), 1))

    return neighbors


def a_star():
    minheap = []
    heapq.heappush(minheap, (0, start))

    g = {(i, j): float('inf') for i in range(ROWS) for j in range(COLS)}
    g[start] = 0

    parent = {start: None}

    while minheap:
        _, current = heapq.heappop(minheap)

        if current == goal:  # incase the goal has been reached
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for neighbor, cost in get_neighbors(current):
            new_g = g[current] + cost

            if new_g < g[neighbor]:
                g[neighbor] = new_g
                f = new_g + h(neighbor)
                heapq.heappush(minheap, (f, neighbor))
                parent[neighbor] = current

    return None


path = a_star()
print("Path:", path)
