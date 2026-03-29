import random

Q = {}

actions = [-1, 1]
alpha = 0.1
gamma = 0.9
epsilon = 0.2

goal = 10

def get_Q(state, action):
    return Q.get((state, action), 0.0)

def choose_action(state):
    if random.random() < epsilon:
        return random.choice(actions)
    return max(actions, key=lambda a: get_Q(state, a))

for episode in range(200):
    state = 0

    for step in range(30):
        action = choose_action(state)
        new_state = state + action

        reward = 20 if new_state == goal else -abs(new_state - goal)

        old_q = get_Q(state, action)
        max_next_q = max(get_Q(new_state, a) for a in actions)

        Q[(state, action)] = old_q + alpha * (
            reward + gamma * max_next_q - old_q
        )

        state = new_state

# Test run
state = 0
path = [state]

for _ in range(20):
    action = max(actions, key=lambda a: get_Q(state, a))
    state += action
    path.append(state)

print("Learned path:", path)
