import os, subprocess, time, signal
import gym
from gym import error, spaces
from gym import utils
from gym.utils import seeding

import logging
logger = logging.getLogger(__name__)

class SnakeEnv(gym.Env):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second' : 50
    }

    def __init__(self):
        self.board_size = 18

        self.action_space = spaces.Discrete(4) # up/down left/right
        self.observation_space = spaces.Box(-self.board_size, self.board_size)

        self.seed()
        self.viewer = None
        self.state = None

    def _step(self, action):
        done = False
        return self.state, reward, done, {}

    def _step(self, action):
      pass
    def _reset(self):
      pass
    def _render(self, mode='human', close=False):
        pass
