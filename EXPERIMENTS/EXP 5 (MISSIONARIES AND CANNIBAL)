from collections import deque
def is_valid(m_left, c_left, m_right, c_right):
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if m_left > 0 and m_left < c_left:
        return False
    if m_right > 0 and m_right < c_right:
        return False
    return True
def missionaries_cannibals():
    start = (3, 3, 0, 0, 0)
    goal = (0, 0, 3, 3, 1)
    queue = deque()
    queue.append((start, []))
    visited = set()
    moves = [
        (1, 0),
        (2, 0),
        (0, 1),
        (0, 2),
        (1, 1)
    ]
    while queue:
        state, path = queue.popleft()
        if state in visited:
            continue
        visited.add(state)
        path = path + [state]
        if state == goal:
            print("Solution:")
            for s in path:
                print(s)
            return
        ml, cl, mr, cr, boat = state
        for m, c in moves:
            if boat == 0:
                new_state = (ml-m, cl-c, mr+m, cr+c, 1)
            else:
                new_state = (ml+m, cl+c, mr-m, cr-c, 0)
            if is_valid(new_state[0], new_state[1],
                        new_state[2], new_state[3]):
                if new_state not in visited:
                    queue.append((new_state, path))
    print("No solution")


missionaries_cannibals
