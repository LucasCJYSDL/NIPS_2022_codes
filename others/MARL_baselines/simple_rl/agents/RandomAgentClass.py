''' RandomAgentClass.py: Class for a randomly acting RL Agent '''

# Python imports.
import random
import gym

# Other imports
from simple_rl.agents.AgentClass import Agent

class RandomAgent(Agent):
    ''' Class for a random decision maker. '''

    def __init__(self, actions, agent_id, name=""):
        name = "Random" if name is "" else name

        # print('type(actions)', type(actions))
        Agent.__init__(self, name=name, actions=actions, agent_id=agent_id)
        self.actions = actions

    def act(self, state, reward, learning=True, is_final=False, mdp_step=1, continue_sign=False):
        if isinstance(self.actions, gym.spaces.Box):
            return self.actions.sample()
        else:
            return random.choice(self.actions)

    # def train_batch(self, s, a, r, s2, t, duration=0, batch_size=0):
    #     pass
