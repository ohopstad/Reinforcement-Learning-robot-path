
class ReinforcementLearning:
    def __init__(self, actions, rewards):
        # Actions should be the different states that you could find yourself in at any point in time.
        # Rewards is a matrix over which reward you get for going from a state to a different one.
        self.actions = actions
        self.rewards = rewards
    