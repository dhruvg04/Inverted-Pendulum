import gymnasium as gym
import pygame
import time
class Agent():
    def __init__(self,env,p,i,d):
        self.action_size=env.action_space.n
        self.kp=p
        self.ki=i
        self.kd=d
        self.olderror=0
    def get__action(self,state):
        angle=state[0][2]
        error=-angle
        differror=error-self.olderror
        integralerror=self.olderror+error
        self.olderror=error
        return self.kp*error+self.ki*integralerror+self.kd*differror

env=gym.make("CartPole-v1",render_mode="human")
pid=Agent(env,p=7000,d=2000,i=0)
state=env.reset()
print(state)
for i in range(200):
    action=pid.get__action(state)
    if action>0:
        action=0
    else:
        action=1
    state=env.step(action)
    env.render()
env.close()
