import heapq
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
def heuristic(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            goal_pos = goal.index(state[i])
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal_pos, 3)
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance
def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row, col = divmod(zero, 3)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero = new_row * 3 + new_col
            new_state = list(state)
            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]
            neighbors.append(tuple(new_state))
    return neighbors
def solve(start):
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic(start), 0, start, []))
    visited = set()
    while priority_queue:
        f, cost, state, path = heapq.heappop(priority_queue)
        if state in visited:
            continue
        visited.add(state)
        if state == goal:
            return path + [state]
        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                new_cost = cost + 1
                new_f = new_cost + heuristic(neighbor)
                heapq.heappush(
                    priority_queue,
                    (new_f, new_cost, neighbor, path + [state])
                )
    return None
def display(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)
solution = solve(start)
if solution:
    print("Solution:")
    for step, state in enumerate(solution):
        print("Step", step)
        display(state)
else:
    print("No solution found.")
