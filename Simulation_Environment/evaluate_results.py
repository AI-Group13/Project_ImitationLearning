from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random

class Evaluation:

    def __init__(self):
        self.err_cartesian = []
        self.err_joint = []
        self.p_des, self.p_obt, self.err = [], [], []
        self.figure = plt.figure()
        self.plot_param = plt.axis([-np.inf, np.inf,-np.inf, np.inf])

    def calc_cartesian_error(self, pos_desired, pos_obtained):

        ss = 0
        for (p1,p2) in zip(pos_desired, pos_obtained):
            ss += (p1-p2)**2
        self.err_joint.append(np.sqrt(ss))
        return self.err_joint[-1]

    def calc_joint_error(self, angle_desired_list, angle_obtained_list):

        err  =  [(a1-a2) for (a1,a2) in zip(angle_desired_list, angle_obtained_list)]
        self.err_joint.append(err)
        return self.err_joint[-1]

    def plot_cartesian_error_traj(self, pos_desired, pos_obtained, e):
        '''Plots the errors in desired and observed trajectory over time'''

        self.p_des.append(pos_desired)
        self.p_obt.append(pos_obtained)

        plt.subplot(211)
        plt.plot(self.p_des, '-r')
        plt.plot(self.p_obt, '--b')

        self.err.append(e)
        plt.subplot(212)
        plt.plot(self.err, '-r')
        plt.pause(0.0001)


if __name__ == '__main__':

    obj = Evaluation()
    for i in range(0, 100000):
        l1 = np.random.random()*100
        l2 = np.random.random()*100
        obj.plot_cartesian_error_traj(l1, l2, l2-l1)
    plt.show()



