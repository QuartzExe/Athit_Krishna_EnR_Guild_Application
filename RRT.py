import random
import math
import matplotlib.pyplot as plt


START = (0, 0)
GOAL = (9, 9)
STEP_SIZE = 0.5
MAX_ITER = 1000
GOAL_RADIUS = 0.5


#List of obstacles (rectangular):
OBSTACLES = [
    (3, 3, 2, 2),
    (6, 1, 2, 3)
]


#Our baseline functions to make RRT happen:
def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])


def get_random_point():
    return (random.uniform(0, 10), random.uniform(0, 10))


def nearest(tree, point):
    closest_node = None
    min_dist = float('inf')

    for node in tree:
        d = distance(node, point)
        if d < min_dist:
            min_dist = d
            closest_node = node

    return closest_node


def steer(from_node, to_point, step_size):
    theta = math.atan2(to_point[1] - from_node[1], to_point[0] - from_node[0])
    new_x = from_node[0] + step_size * math.cos(theta)
    new_y = from_node[1] + step_size * math.sin(theta)
    return (new_x, new_y)


def collision(point):
    x, y = point
    for (ox, oy, w, h) in OBSTACLES:
        if ox <= x <= ox + w and oy <= y <= oy + h:
            return True
    return False



#Actual iterations of RRT algorithm
tree = [START]
parent = {START: None}

goal_reached = False
goal_node = None

for i in range(MAX_ITER):
    rand_point = get_random_point()
    nearest_node = nearest(tree, rand_point)
    new_node = steer(nearest_node, rand_point, STEP_SIZE)

    if not collision(new_node):
        tree.append(new_node)
        parent[new_node] = nearest_node

        # Checking if goal reached
        if distance(new_node, GOAL) < GOAL_RADIUS:
            goal_reached = True
            goal_node = new_node
            break



#Getting the path through which the goal node has been attained (to colour the path red in the plot):
path = []
if goal_reached:
    current = goal_node
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()



plt.figure()

# Drawing obstacles in grey:
for (ox, oy, w, h) in OBSTACLES:
    plt.gca().add_patch(plt.Rectangle((ox, oy), w, h, color='gray'))

# Drawing the tree in green:
for node in tree:
    if parent[node] is not None:
        px, py = parent[node]
        nx, ny = node
        plt.plot([px, nx], [py, ny], 'g-', linewidth=0.5)

# Drawing path in red:
if path:
    xs, ys = zip(*path)
    plt.plot(xs, ys, 'r-', linewidth=2, label="Path")


plt.plot(START[0], START[1], 'bo', label="Start")
plt.plot(GOAL[0], GOAL[1], 'ro', label="Goal")

plt.xlim(0, 10)
plt.ylim(0, 10)
plt.legend()
plt.title("RRT Path Planning")
plt.show()
