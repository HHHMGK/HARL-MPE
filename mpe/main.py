import time
from pettingzoo.mpe import \
    simple_world_comm_v3 \
        as main_env

env = main_env.env(max_cycles = 50, continuous_actions = False, render_mode='human')

env.reset()
for agent in env.agent_iter():
    observation, reward, termination, truncation, info = env.last()
    print(agent)
    # print(observation, observation.shape)
    print(reward)
    if termination or truncation:
        action = None
    else:
        # this is where you would insert your policy
        action = env.action_space(agent).sample() 

    # print(action)
    env.step(action)
    # time.sleep(1)
env.close()