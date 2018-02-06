from setuptools import setup

setup(name="gym_snake",
      version="0.1",
      url="https://github.com/AlexandreOuellet/gym-snake",
      author="Alexandre Ouellet",
      license="MIT",
      packages=["gym_snake", "gym_snake.envs"],
      install_requires = ["gym", "pygame", "numpy"]
)
