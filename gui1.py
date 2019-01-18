import gym
# import numpy as np 

env = gym.make('CartPole-v0')
env.reset()

for i in range(5000):

	env.render()
	action = env.action_space.sample()
	observation, reward, done, info = env.step(action)
	if done:
		break