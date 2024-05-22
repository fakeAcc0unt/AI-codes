#8 puzzle
from heapq import heappush, heappop

# Define the goal state
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

# Define moves: up, down, left, right
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def misplaced_tiles(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j]:
                count += 1
    return count

def get_neighbors(state, empty_pos):
    neighbors = []
    for move in moves:
        new_pos = (empty_pos[0] + move[0], empty_pos[1] + move[1])
        if 0 <= new_pos[0] < 3 and 0 <= new_pos[1] < 3:
            new_state = [row[:] for row in state]
            new_state[empty_pos[0]][empty_pos[1]], new_state[new_pos[0]][new_pos[1]] = new_state[new_pos[0]][new_pos[1]], new_state[empty_pos[0]][empty_pos[1]]
            neighbors.append((new_state, new_pos))
    return neighbors

def solve_puzzle(initial_state):
    # Priority queue for Best First Search
    pq = [(misplaced_tiles(initial_state), 0, initial_state, (2, 2))]
    visited = set()
    
    while pq:
        _, cost, state, empty_pos = heappop(pq)
        
        if state == goal_state:
            return cost, state
        
        if tuple(map(tuple, state)) in visited:
            continue
        
        visited.add(tuple(map(tuple, state)))
        
        for neighbor_state, neighbor_pos in get_neighbors(state, empty_pos):
            if tuple(map(tuple, neighbor_state)) not in visited:
                new_cost = cost + 1 + misplaced_tiles(neighbor_state)
                heappush(pq, (misplaced_tiles(neighbor_state), new_cost, neighbor_state, neighbor_pos))

    return -1, None

def print_solution(solution):
    if solution is None:
        print("No solution exists!")
    else:
        moves, state = solution
        print("Minimum number of moves required:", moves)
        print("Solution:")
        for row in state:
            print(row)

#main
initial_state = [[1, 2, 3],
                 [5, 6, 0],
                 [7, 8, 4]]

solution = solve_puzzle(initial_state)
print_solution(solution)
