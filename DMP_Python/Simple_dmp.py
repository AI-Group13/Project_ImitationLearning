
import numpy as np
from Simulation_Environment.Imitation_Learn import Imitation_Learn
import matplotlib.pyplot as plt
from DMP_runner import DMP_runner
import simple_trajectories_origina
from train_dmp import *

#Name of the file
name = 'Simple_dmps.xml'
f_name = 'demo_IDEAL.csv'

#Set no. of basis functions
n_rfs = 300

#Set the time-step
dt = 0.005

tau = 1
# time = np.arange(0,tau+dt,dt)

Il_object = Imitation_Learn()


def joint_DMP(joint_number):

    #Obtain w, c & D (in that order) from below function, and generate XML file
    Tl_j1, Tl_j2, Tl_j3, Tl_j4, Tl_j5, Tl_g1, Tl_g2 = simple_trajectories_origina.demo_trajectory(dt, f_name)
    T_all = [Tl_j1, Tl_j2, Tl_j3, Tl_j4, Tl_j5, Tl_g1, Tl_g2]

    T = T_all[joint_number]

    train_dmp(name, n_rfs, T, dt)

    start = T[0][0]
    goal = T[0][len(T[0])-1]
    my_runner = DMP_runner(name,start,goal)

    Y, Yd, Ydd = [], [], []
    for i in np.arange(0, int(tau/dt)+1):
        a, b, c = my_runner.step(tau,dt)
        Y.append(my_runner.y)
        # Y.append(a)
        Yd.append(b)
        Ydd.append(c)

    return T, Y, Yd, Ydd

def feed_pose(joint_num):

    a,joint_pos,c,d = joint_DMP(joint_num)
    print (joint_pos)

    return a,joint_pos,c,d


# Two subplots, the axes array is 1-d

def plotting(T, Y, Yd, Ydd):
    f, axarr = plt.subplots(1, sharex=True)
    axarr.plot(T[0], 'r')
    axarr.plot(Y, 'b')
    axarr.set_title("Original Trajectory - Red \n Dynamic Movement Generated Trajectory - Blue \n JOINT NUMBER - ")
    plt.show()

def main(index):

    p,jp,r,s = feed_pose(index)
    plotting(p,jp,r,s)

    return p,jp,r,s
