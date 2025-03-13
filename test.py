import gymnasium as gym, random, logging
import nasimemu, nasimemu.env_utils as env_utils

# In this example, a scenario instance is randomly generated from either 'entry_dmz_one_subnet' or 'entry_dmz_two_subnets' on every new episode. Make sure the path to scenarios is correct.
# To use emulation, setup Vagrant and change emulate=True.
env = gym.make('NASimEmu-v0', emulate=False, scenario_name='NASimEmu/scenarios/corp.v2.yaml:NASimEmu/scenarios/corp.v2.yaml')
s, _ = env.reset()

# To see the emulation logs, uncomment the following:
# logging.basicConfig(level=logging.DEBUG)
# logging.getLogger('urllib3').setLevel(logging.INFO)

# To see the whole network, use (only in simulation):
# env.render_state()

for _ in range(5):
    
    actions = env_utils.get_possible_actions(env.unwrapped, s)

    action = random.choice(actions)
    s, r, terminated, truncated, info = env.step(action)
    print(f"s.shape: {s.shape}\n")
    print(f"s:\n{s}\n")

    # print(f"Possible actions: {actions}\n")

    (action_subnet, action_host), action_id = action
    # print(f"Taken action: {action}; subnet_id={action_subnet}, host_id={action_host}, action={env.unwrapped.action_list[action_id]}\n")
    # print(f"reward: {r}, done: {terminated}\n")