from swarm_prompt.robot_api_prompt import robot_api
from swarm_prompt.user_requirements import get_user_commands

task_name = "crossing"

TASK_DES = """Hello!
There is a mobile ground robot that has the capability to control its own speed, acquire its location, and sense the positions and speeds of other robots.
Now, multiple AI assistants are implementing user commands through collaborative coding.
You are one of these assistants, and you need to understand this context and then carry out your work accordingly.
""".strip()

UserRequirement = get_user_commands(task_name)[0]

ENV_DES = """
Environment:
    bounds:{'x_min':-2.5, 'x_max': 2.5, 'y_min': -2.5, 'y_max': 2.5}

Robot:
    max_speed: 0.2m/s (constant)
    Control Method: Omnidirectional speed control
    Initial position: random position in the environment
    Initial speed: np.array([0, 0])
""".strip()

swarm_system_prompt = f"""
## These are the environment description:
These are the basic descriptions of the environment.
{ENV_DES}

## These APIs can be directly called by you.
```python
{robot_api.get_prompt(task_name)}
```

## Interface Constraints:
The function in main.py must be def main()
And you cannot use ros.
You don't need to design UI.
"""

swarm_system_prompt_GPT = f"""
{TASK_DES}

## These are the environment description:
These are the basic descriptions of the environment.
{ENV_DES}

## These APIs can be directly called by you.
```python
{robot_api.get_prompt(task_name)}
```

## Interface Constraints:
The main function must be def main()
And you cannot use ros.

## This is the user's requirement:
{UserRequirement}
""".strip()
