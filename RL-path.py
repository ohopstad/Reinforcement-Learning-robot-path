from Environment import Floor
from RL import ReinforcementLearning
import numpy as np


floor = Floor(3, 3)
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
start = 8
end = 5
print("from {} to {}:".format(start, end) + str([actions[i] for i in RL.get_optimal_route(8, 5)]))
