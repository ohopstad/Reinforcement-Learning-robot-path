import numpy as np


class ReinforcementLearning:
    def __init__(self, actions, rewards):
        # Actions should be the different states that you could find yourself in at any point in time.
        # self.Rewards is a matrix over which reward you get for going from a state to a different one.
        self.actions = actions
        self.rewards = rewards
        self.learning_rate = 0.9        # alpha
        self.discount_factor = 0.75     # gamma

        self.Q = np.array(np.zeros([len(actions), len(actions)]))

    def get_optimal_route(self, start_state, end_state):
        num_actions = len(self.rewards)
        rewards = np.copy(self.rewards)
        rewards[end_state, end_state] = 999

        # -- self.Q-learning --
        for i in range(1000):
            playable_actions = []
            current_state = np.random.randint(0, num_actions)
            for j in range(num_actions):
                if rewards[current_state, j] > 0:
                    playable_actions.append(j)
            next_state = np.random.choice(playable_actions)
            TD = rewards[current_state, next_state] + self.discount_factor * self.Q[next_state, np.argmax(self.Q[next_state, ])] - self.Q[current_state, next_state]

            # Bellman eself.quation:
            self.Q[current_state, next_state] += self.learning_rate * TD
            
        route = [start_state]
        next_state = start_state
        while(next_state != end_state):
            next_state = np.argmax(self.Q[start_state, ])
            route.append(next_state)
            start_state = next_state
        return route