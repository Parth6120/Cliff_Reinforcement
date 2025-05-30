from pate1385_lab2_qleaning_cliff_env import Env
import numpy as np
import time
import os

# create environment
env = Env()

# QTable : contains the Q-Values for every (state,action) pair
qtable = np.random.rand(env.stateCount, env.actionCount).tolist()

# hyperparameters
epoch = 50  # episodes
gamma = 0.1 #learning rate
epsilon = 0.1 # exploration rate
decay = 0.1 # reduction in exploration rate in next episode

# training loop
for i in range(epoch):
    state, reward, done = env.reset()
    steps = 0

    while not done:
        os.system('cls')
        print("episode #", i+1, "/", epoch)
        env.render()
        time.sleep(0.05)

        # count steps to finish game
        steps += 1

        # act randomly sometimes to allow exploration
        if np.random.uniform() < epsilon:
            action = env.randomAction()
        # if not select max action in Qtable (act greedy)
        else:
            action = qtable[state].index(max(qtable[state]))

        # take action
        next_state, reward, done = env.step(action)

        # update qtable value with Bellman equation
        qtable[state][action] = reward + gamma * max(qtable[next_state])

        # update state
        state = next_state
    # The more we learn, the less we take random actions
    epsilon -= decay*epsilon

    print("\nDone in", steps, "steps".format(steps))
    time.sleep(0.8)