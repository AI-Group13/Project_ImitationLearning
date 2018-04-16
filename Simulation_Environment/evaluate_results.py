from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random

class Evaluation:

    def __init__(self):
        self.err_cartesian = []
        self.err_joint = []
        self.p_des, self.p_obt, self.pos_err= [], [], []
        self.a_des, self.a_obt, self.angle_err= [], [], []
        self.plot_param = plt.axis([-np.inf, np.inf,-np.inf, np.inf])

    def calc_cartesian_error(self, pos_desired, pos_obtained):
        '''Calculate the error in Cartesian coordinates'''
        ss = 0
        for (p1,p2) in zip(pos_desired, pos_obtained):
            ss += (p1-p2)**2
        self.err_cartesian.append(np.sqrt(ss))
        return self.err_cartesian[-1]

    def calc_joint_error(self, angle_desired_list, angle_obtained_list):
        '''Calculate the error in joint angles'''

        err  =  [(a1-a2) for (a1,a2) in zip(angle_desired_list, angle_obtained_list)]
        self.err_joint.append(err)
        return self.err_joint[-1]

    def plot_cartesian_error_traj(self, pos_desired, pos_obtained, e):
        '''Plots the errors in desired and observed waypoints over time, in task space
        pos_desired, pos_obtained, e - Lists of 3 x 1 size '''

        # Appending the readings to individual lists
        self.p_des.append(pos_desired)
        self.p_obt.append(pos_obtained)
        self.pos_err.append(e)

        pos_des  = np.asarray(self.p_des)
        pos_obt = np.asarray(self.p_obt)
        pos_error = np.asarray(self.pos_err)

        # print ("\n\nDesired position list", self.p_des, "\n\n" )
        # print ("\n\nObtained position list", self.p_obt, "\n\n" )
        # print ("\n\nError list", self.pos_err, "\n\n" )

        # Plotting for the three cartesian coordinates' desired and observed trajectories and also the correspsonding errors
        plt.subplot(311)
        plt.plot(pos_des[:,0], '-r')
        plt.plot(pos_obt[:,0], '--b')
        plt.plot(pos_error[:,0], '-g')
        plt.ylabel("X coordinate")
        plt.legend(["Desired trajectory", "Observed trajectory", "Trajectory error"])

        plt.subplot(312)
        plt.plot(pos_des[:,1], '-r')
        plt.plot(pos_obt[:,1], '--b')
        plt.plot(pos_error[:,1], '-g')
        plt.ylabel("Y coordinate")

        plt.subplot(313)
        plt.plot(pos_des[:,2], '-r')
        plt.plot(pos_obt[:,2], '--b')
        plt.plot(pos_error[:,2], '-g')
        plt.ylabel("Z coordinate")

        plt.xlabel("Time steps")
        plt.pause(0.0001)

        return 0

    def plot_joint_error_traj(self, angle_desired, angle_obtained, e):
        '''Plots the errors in desired and observed trajectory over time
        angle_obtained, angle_desired and e - Lists of size 5 x 1 '''

        self.a_des.append(angle_desired)
        self.a_obt.append(angle_obtained)
        self.angle_err.append(e)

        angle_des  = np.asarray(self.a_des)
        angle_obt = np.asarray(self.a_obt)
        angle_error = np.asarray(self.angle_err)

        # Plotting for all the joint angles desired and obtained and corresponding errors
        plt.subplot(511)
        plt.plot(angle_des[:,0], '-r')
        plt.plot(angle_obt[:,0], '--b')
        plt.plot(angle_error[:,0], '-g')
        plt.ylabel("Theta 1 ")

        plt.subplot(512)
        plt.plot(angle_des[:,1], '-r')
        plt.plot(angle_obt[:,1], '--b')
        plt.plot(angle_error[:,1], '-g')
        plt.ylabel("Theta 2 ")

        plt.subplot(513)
        plt.plot(angle_des[:,2], '-r')
        plt.plot(angle_obt[:,2], '--b')
        plt.plot(angle_error[:,2], '-g')
        plt.ylabel("Theta 3 ")

        plt.subplot(514)
        plt.plot(angle_des[:,3], '-r')
        plt.plot(angle_obt[:,3], '--b')
        plt.plot(angle_error[:,3], '-g')
        plt.ylabel("Theta 4 ")

        plt.subplot(515)
        plt.plot(angle_des[:,4], '-r')
        plt.plot(angle_obt[:,4], '--b')
        plt.plot(angle_error[:,4], '-g')
        plt.ylabel("Theta 5 ")

        plt.pause(0.0001)

        return 0

    def main(self, condition=0, p_d=0, p_ob=0, a_d=0, a_ob=0):
        '''Decides whether to show results in Cartesian setup or joint angular setup or both'''

        if condition !=0:
            if condition == 1:
                p_e = self.calc_cartesian_error(p_d, p_ob)
                self.plot_cartesian_error_traj(p_d, p_ob, p_e)
            elif condition == 2:
                a_e = self.calc_joint_error(a_d, a_ob)
                self.plot_joint_error_traj(a_d, a_ob, a_e)
            elif condition == 3:
                a_e = self.calc_joint_error(a_d, a_ob)
                p_e = self.calc_cartesian_error(p_d, p_ob)
                self.plot_cartesian_error_traj(p_d, p_ob, p_e)
                self.plot_joint_error_traj(a_d, a_ob, a_e)

# if __name__ == '__main__':
#
#     obj = Evaluation()
#     for i in range(0, 100000):
#         l1 = [ np.random.random()*100 for i in range(0,5)]
#         l2 = [ np.random.random()*100 for i in range(0,5)]
#         ee = [a-b for (a,b) in zip(l2,l1)]
#         obj.main(1, l1, l2, ee)
#     plt.show()



