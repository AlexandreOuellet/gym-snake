import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='Snake-v0',
    entry_point='gym_snake.envs:SnakeEnv',
    timestep_limit=1000,
    reward_threshold=1.0,
    nondeterministic = False,
)
