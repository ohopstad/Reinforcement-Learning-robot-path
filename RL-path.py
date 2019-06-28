from Environment import Floor
from RL import ReinforcementLearning
import numpy as np

RL = ReinforcementLearning()

floor = Floor(9, 9)
states = floor.getStates()
diagram = {u:states[u] for u in [i for i in range(len(states))]}
paths = floor.getPaths()
actions = []
for x in states:
    for u in x:
        actions.append(u)

rewards = np.array([
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0], 
    [0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0], 
    [0, 1, 0, 0, 0, 0, 0, 1, 0], 
    [0, 0, 1, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 1, 0, 0, 0, 1, 0], 
    [0, 0, 0, 0, 1, 0, 1, 0, 1], 
    [0, 0, 0, 0, 0, 0, 0, 1, 0] 
])

RL = ReinforcementLearning(actions, rewards)

print(RL.get_optimal_route(9, 1, rewards))
