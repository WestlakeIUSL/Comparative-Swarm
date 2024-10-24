import os
import yaml


from swarm_prompt.robot_api_prompt import GLOBAL_ROBOT_API, LOCAL_ROBOT_API
from swarm_prompt.user_requirements import get_user_commands
from swarm_prompt.env_description_prompt import ENV_DES
from swarm_prompt.task_description import TASK_DES

script_dir = os.path.dirname(os.path.abspath(__file__))
yaml_file_path = os.path.join(script_dir, "../config/", "experiment_config.yaml")

with open(yaml_file_path, "r", encoding="utf-8") as file:
    data = yaml.safe_load(file)
task_name = data["arguments"]["--run_experiment_name"]["default"][0]

UserRequirement = get_user_commands(task_name)[0]

swarm_system_prompt = f"""
## These are the environment description:
These are the basic descriptions of the environment.
{ENV_DES}

## These APIs can be directly called by you.
where local APIs can only be called by the robot itself, and global APIs can be called by an centralized controller.
Local APIs:
{LOCAL_ROBOT_API}
Global APIs:
{GLOBAL_ROBOT_API}


## Interface Constraints:
The function in main.py must be def main()
And you cannot use ros.
You don't need to design UI.
The global APIs can only called in task_allocator;
The local APIs can only called in robot_controller;
"""


swarm_system_prompt_GPT = f"""
{TASK_DES}

## These are the environment description:
These are the basic descriptions of the environment.
{ENV_DES}

```

## Interface Constraints:
The main function must be def main()
And you cannot use ros.

## This is the user's requirement:
{UserRequirement}
""".strip()
