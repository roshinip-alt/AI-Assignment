from collections import deque

def get_next_states(x, y, capA, capB):
    states = []

    # Fill jugs
    states.append((capA, y))   # Fill A
    states.append((x, capB))   # Fill B

    # Empty jugs
    states.append((0, y))      # Empty A
    states.append((x, 0))      # Empty B

    # Pour A -> B
    transfer = min(x, capB - y)
    states.append((x - transfer, y + transfer))

    # Pour B -> A
    transfer = min(y, capA - x)
    states.append((x + transfer, y - transfer))

    return states


def bfs_water_jug(capA, capB, target):
    visited = set()
    queue = deque()
    parent = {}

    queue.append((0, 0))
    visited.add((0, 0))
    parent[(0, 0)] = None

    while queue:
        x, y = queue.popleft()

        if x == target or y == target:
            return reconstruct_path(parent, (x, y))

        for state in get_next_states(x, y, capA, capB):
            if state not in visited:
                visited.add(state)
                parent[state] = (x, y)
                queue.append(state)

    return None


def reconstruct_path(parent, state):
    path = []
    while state is not None:
        path.append(state)
        state = parent[state]
    return path[::-1]


# MAIN
capA = 4
capB = 3
target = 2

solution = bfs_water_jug(capA, capB, target)

print("BFS Solution Path:")
for i in solution:
    print(i)