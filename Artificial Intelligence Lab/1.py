class State:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2

    def __eq__(self, other):
        return self.jug1 == other.jug1 and self.jug2 == other.jug2

    def __hash__(self):
        return hash((self.jug1, self.jug2))

    def __str__(self):
        return f"({self.jug1}, {self.jug2})"

def water_jug_dfs(capacity_jug1, capacity_jug2, target):
    stack = [(State(0, 0), [])]
    visited = set()

    while stack:
        current_state, actions = stack.pop()

        if current_state == target:
            return actions

        if current_state in visited:
            continue

        visited.add(current_state)

        stack.append((State(capacity_jug1, current_state.jug2), actions + ["Fill jug 1"]))

        stack.append((State(current_state.jug1, capacity_jug2), actions + ["Fill jug 2"]))

        stack.append((State(0, current_state.jug2), actions + ["Empty jug 1"]))


        stack.append((State(current_state.jug1, 0), actions + ["Empty jug 2"]))

        pour_to_jug2 = min(current_state.jug1, capacity_jug2 - current_state.jug2)
        stack.append((State(current_state.jug1 - pour_to_jug2, current_state.jug2 + pour_to_jug2),
                      actions + [f"Pour jug 1 to jug 2 ({pour_to_jug2})"]))

        pour_to_jug1 = min(current_state.jug2, capacity_jug1 - current_state.jug1)
        stack.append((State(current_state.jug1 + pour_to_jug1, current_state.jug2 - pour_to_jug1),
                      actions + [f"Pour jug 2 to jug 1 ({pour_to_jug1})"]))

    return "No Solution Found"

jug1_capacity = int(input("Enter Jug 1 capacity: "))
jug2_capacity = int(input("Enter Jug 2 capacity: "))
target_amount = int(input("Enter target amount: "))

result = water_jug_dfs(jug1_capacity, jug2_capacity, State(target_amount, 0))

if result:
    print("Solution found:")
    for action in result:
        print(action)
else:
    print("No solution found.")