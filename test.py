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
r = 0


env.reset()
step = 0
for _ in range(10000):
    env.render()
    save = env.step(env.action_space.sample())
    image = save[0]
    r += save[1] 
    done = save[2]
    if done:
        # el personaje tiene 3 vidas para usar 
        break
    step += 1

print(r)
env.close()