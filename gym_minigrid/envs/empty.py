from gym_minigrid.minigrid import *
from gym_minigrid.register import register

import random

class EmptyEnv(MiniGridEnv):
    """
    Empty grid environment, no obstacles, sparse reward
    """

    def __init__(
        self,
        size=8,
        agent_start_pos=(1,1),
        agent_start_dir=0,
    ):
        self.agent_start_pos = agent_start_pos
        self.agent_start_dir = agent_start_dir
        self.number_of_goals = 1
        self.random_goals = False
        self.goals_collected = 0
        self.living_reward = 0

        if not self.random_goals:
            self.goal_positions = [(random.random(), random.random()) for _ in range(100)]

        super().__init__(
            grid_size=size,
            max_steps=4*size*size,
            # Set this to True for maximum speed
            see_through_walls=True
        )

    def _gen_grid(self, width, height):
        # Create an empty grid
        self.grid = Grid(width, height)

        # Generate the surrounding walls
        self.grid.wall_rect(0, 0, width, height)

        # Place goals in each position in goal_positions
        i = 0
        while i < self.number_of_goals:
            if self.random_goals:
                x = random.randint(1, width - 2)
                y = random.randint(1, height - 2)
            else:
                x = round(1 + (width - 3) * self.goal_positions[i][0])
                y = round(1 + (height - 3) * self.goal_positions[i][1])
            if self.grid.get(x, y) != Goal():
                self.grid.set(x, y, Goal())
                i += 1

        # Place the agent
        if self.agent_start_pos is not None:
            self.agent_pos = self.agent_start_pos
            self.agent_dir = self.agent_start_dir
        else:
            self.place_agent()

        self.mission = "get to the green goal square"

class EmptyEnv5x5(EmptyEnv):
    def __init__(self):
        super().__init__(size=5)

class EmptyRandomEnv5x5(EmptyEnv):
    def __init__(self):
        super().__init__(size=5, agent_start_pos=None)

class EmptyEnv6x6(EmptyEnv):
    def __init__(self):
        super().__init__(size=6)

class EmptyRandomEnv6x6(EmptyEnv):
    def __init__(self):
        super().__init__(size=6, agent_start_pos=None)

class EmptyEnv16x16(EmptyEnv):
    def __init__(self):
        super().__init__(size=16)

class EmptyEnvMultiGoals(EmptyEnv):
    def __init__(self):
        super().__init__(size=5)

class EmptyEnvMultiGoalsRandomSpawn(EmptyEnv):
    def __init__(self):
        super().__init__(size=5, agent_start_pos=None)

register(
    id='MiniGrid-Empty-5x5-v0',
    entry_point='gym_minigrid.envs:EmptyEnv5x5'
)

register(
    id='MiniGrid-Empty-Random-5x5-v0',
    entry_point='gym_minigrid.envs:EmptyRandomEnv5x5'
)

register(
    id='MiniGrid-Empty-6x6-v0',
    entry_point='gym_minigrid.envs:EmptyEnv6x6'
)

register(
    id='MiniGrid-Empty-Random-6x6-v0',
    entry_point='gym_minigrid.envs:EmptyRandomEnv6x6'
)

register(
    id='MiniGrid-Empty-8x8-v0',
    entry_point='gym_minigrid.envs:EmptyEnv'
)

register(
    id='MiniGrid-Empty-16x16-v0',
    entry_point='gym_minigrid.envs:EmptyEnv16x16'
)

register(
    id='MiniGrid-EmptyMultiGoals-v0',
    entry_point='gym_minigrid.envs:EmptyEnvMultiGoals'
)

register(
    id='MiniGrid-EmptyMultiGoalsRandomSpawn-v0',
    entry_point='gym_minigrid.envs:EmptyEnvMultiGoalsRandomSpawn'
)