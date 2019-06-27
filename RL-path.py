from Environment import Floor
from RL import ReinforcementLearning

floor = Floor(3, 3)
states = floor.getPaths()
diagram = {u:states[u] for u in [i for i in range(len(states))]}
paths = floor.getStates()

actions = [diagram[u] for u in [i for i in states]]
print(actions)