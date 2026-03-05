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


def dfs_water_jug(x, y, capA, capB, target, visited, path):
    # If already visited, stop
    if (x, y) in visited:
        return False

    # Mark visited
    visited.add((x, y))
    path.append((x, y))

    # Check goal
    if x == target or y == target:
        return True

    # Explore deeper
    for state in get_next_states(x, y, capA, capB):
        if dfs_water_jug(state[0], state[1], capA, capB, target, visited, path):
            return True

    # Backtrack
    path.pop()
    return False


# MAIN
capA = 4
capB = 3
target = 2

visited = set()
path = []

if dfs_water_jug(0, 0, capA, capB, target, visited, path):
    print("DFS Solution Path:")
    for state in path:
        print(state)
else:
    print("No solution exists")