from collections import deque
def water_jug(jug1, jug2, target):
    visited = set()
    queue = deque()
    queue.append((0, 0, []))
    while queue:
        x, y, path = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        path = path + [(x, y)]
        if x == target or y == target:
            print("Solution:")
            for state in path:
                print(state)
            return
        states = [
            (jug1, y),
            (x, jug2),
            (0, y),
            (x, 0),
            (x - min(x, jug2 - y), y + min(x, jug2 - y)),
            (x + min(y, jug1 - x), y - min(y, jug1 - x))
        ]
        for state in states:
            if state not in visited:
                queue.append((state[0], state[1], path))
    print("No solution")

water_jug(4, 3, 2)
