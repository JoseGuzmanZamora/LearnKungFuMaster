import gym
import cv2 as cv
import matplotlib.pyplot as plt 

env = gym.make('KungFuMaster-v0')

print(env.action_space)
# Discrete 14 posibilidades
actions = env.action_space.n

print(env.observation_space)
# una imagen de 210,160,3 shape
dimensions = env.observation_space.shape


env.reset()
for _ in range(1000):
    env.render()
    save = env.step(env.action_space.sample())
    image = save[0]
    reward = save[1] 
    done = save[2]
    if done:
        # el personaje tiene 3 vidas para usar 
        break
env.close()