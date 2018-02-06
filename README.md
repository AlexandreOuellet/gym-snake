# gym-snake

The snake environment is a single agent environment that plays
the snake game.  Each step requires a discrete movement where
0=up, 1=down, 2=left, 3=right.  It will move the snake's head
in that direction, and the tail will follow.  If you eat a 
fruit, the snake's body will grow by 1.  You get 1 reward for
completing eating a fruit, and -100 for going out of bound, or
hitting yourself

# Installation

```bash
cd gym-snake
pip install -e .
```


# Usage

```python
import gym
from gym import wrappers, logger
import gym_snake
```