import random

state = 0.0

for i in range(5):
    action = random.uniform(-1, 1)
    state = state + action
    print("Step:", i, "State:", state)
