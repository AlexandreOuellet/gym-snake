"""
Classic snake game
"""

import math
import gym
from gym import spaces, logger
from gym.utils import seeding
import numpy as np
from gym_snake.envs.snake_view import SnakeView
import queue

LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3

EMPTY = 0
BODY = 2
TAIL = 1
HEAD = 3
FRUIT = 4

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (0, 255, 255)
BLUE = (0, 0, 255)

COLORS = {
    EMPTY: BLACK,
    BODY: WHITE,
    TAIL: YELLOW,
    HEAD: BLUE,
    FRUIT: GREEN,
    }

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
class BodyPart(Point):
    def __init__(self, x, y, character, trail_character):
        super().__init__(x, y)
        self.character = character
        self.trail_character = trail_character

class SnakeEnv(gym.Env):
    """
    Winter is here. You and your friends were tossing around a frisbee at the park
    when you made a wild throw that left the frisbee out in the middle of the lake.
    The water is mostly frozen, but there are a few holes where the ice has melted.
    If you step into one of those holes, you'll fall into the freezing water.
    At this time, there's an international frisbee shortage, so it's absolutely imperative that
    you navigate across the lake and retrieve the disc.
    However, the ice is slippery, so you won't always move in the direction you intend.
    The surface is described using a grid like the following

        0000
        0134
        0100
        0T00

    0 : empty space
    1 : body of the snake
    2 : tail of the snake
    3 : head of the snake
    4 : fruit

    The episode ends when you fill the screen with the snake, or the head
    hit anything that is not empty or a fruit.
    The starting position is random
    You receive a reward of 1 if you eat a fruit, -1 if you hit something, zero otherwise.
    """

    metadata = { 'render.modes': ['human', 'ansi'] }

    def __init__(self):
        self.reset()
    
    def reset(self):
        self.seed()

        self.tile_height = self.tile_width = 10
        self.view = SnakeView(self.tile_width, self.tile_height, COLORS)

        self.action_space = spaces.Discrete(4)

        self.state = np.zeros(shape=(self.tile_height, self.tile_width), dtype=np.uint8)

        self.observation_space = spaces.Box(low=0, high=4, shape=(self.tile_height, self.tile_width))
        
        head_x = self.np_random.randint(0, self.tile_width)
        head_y = self.np_random.randint(0, self.tile_height)

        self.tail = BodyPart(head_x, head_y, TAIL, EMPTY)
        self.head = BodyPart(head_x, head_y, HEAD, BODY)
        self.queue = queue.Queue()

        self.state[self.head.y][self.head.x] = HEAD

        self._spawnFruit()
        return self.state

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def render(self):
        self.view.render(self.state)

    def close(self):
        if self.view: self.view.close()

    def step(self, action):
        assert self.action_space.contains(action), "%r (%s) invalid"%(action, type(action))
        self.queue.put(action)

        reward = 0
        canMove, isFruit = self._canMove(self.head, action) # True if you can't move
        if canMove:
            self._move(self.head, action)
            if isFruit:
                reward = 1
            else:
                oldAction = self.queue.get()
                self._move(self.tail, oldAction)
            self.state[self.head.y][self.head.x] = self.head.character
        else:
            reward = -1
        
        if isFruit:
            self._spawnFruit()

        done = not canMove
        return np.array(self.state), reward, done, {}

    def _spawnFruit(self):
        possibilities = []
        for row in range(0, len(self.state)):
            for column in range(0, len(self.state[row])):
                if self.state[row][column] == EMPTY:
                    possibilities.append([row, column])

        index = self.np_random.randint(0, len(possibilities))
        row, column = possibilities[index]

        self.state[row][column] = FRUIT


    def _move(self, bodyPart: BodyPart, action):
        destination = self._getDestination(bodyPart, action)

        self.state[bodyPart.y][bodyPart.x] = bodyPart.trail_character
        self.state[destination.y][destination.x] = bodyPart.character

        bodyPart.x = destination.x
        bodyPart.y = destination.y

    def _canMove(self, bodyPart: BodyPart, action):
        destination = self._getDestination(bodyPart, action)

        if destination.x < 0 or destination.x >= self.tile_width:
            return False, False

        if destination.y < 0 or destination.y >= self.tile_height:
            return False, False

        canMove = self.state[destination.y][destination.x] in [EMPTY, FRUIT]
        isFruit = self.state[destination.y][destination.x] in [FRUIT]

        return canMove, isFruit

    def _getDestination(self, bodyPart: BodyPart, action):
        destination = Point(bodyPart.x, bodyPart.y)

        if action == LEFT:
            destination.x -= 1
        if action == RIGHT:
            destination.x += 1

        if action == UP:
            destination.y -= 1
        if action == DOWN:
            destination.y += 1
        
        return destination
