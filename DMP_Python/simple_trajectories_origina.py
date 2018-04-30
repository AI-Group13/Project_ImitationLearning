import numpy as np
import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.pyplot as plt
import csv
import ast

from Simulation_Environment.Imitation_Learn import *

data = []
data_points = []
lwra, lwrb, hndar, hndbr, rwra, rwrb = [0]*3, [0]*3, [0]*3,[0]*3, [0]*3,[0]*3	

filename = 'demo_IDEAL.csv'

def read_data_split(filename):

    Il_obj = Imitation_Learn()
    pathway_jointSpace = Il_obj.parse_demo(filename)

    pathway_jointSpace_swapped = np.swapaxes(np.asarray(pathway_jointSpace), 0, 1)

    # print ("What is pathway_jointSpace", pathway_jointSpace)
    # Il_obj.log_data(avgd_res, 'demo_processed.csv')

    # print (len(pathway_jointSpace_swapped))
    return list(pathway_jointSpace_swapped)

def plot_data():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    # ax.plot( map(add, lwra[0], lwrb[0]) , map(add, lwra[1],lwrb[1]), map(add, lwra[2], lwrb[2]), 'r-', label=' Averaged Data')
    ax.plot(lwra[0], lwra[1], lwra[2], 'r-', label='Left Wirst Marker A')
    ax.plot(lwrb[0], lwrb[1], lwrb[2], 'g-', label='Left Wirst Marker B')
    ax.plot(hndbr[0], hndbr[1], hndbr[2], 'b*', label='Hand B')
    # ax.plot(lwrb[0], lwrb[1], lwrb[2], 'go', label='parametric curve')
    ax.legend()
    plt.show()

def plot2d():
    plt.plot(lwra[0][0:300], lwra[1][0:300])
    plt.grid()
    plt.show()

def demo_trajectory(dt, filename):

    # Joint 1
    t = list(i for i in np.arange(0,1+dt,dt))
    b = read_data_split(filename)
    y = b[0] 
    y2 = [0]
    y2 = np.append(y2,np.divide(np.diff(y,1),np.power(dt,1)))
    y3 = [0,0]
    y3 = np.append(y3,np.divide(np.diff(y,2),np.power(dt,2)))
    T1 = []
    T1_rec = []
    T1_rec.append(y)
    T1.append(y)
    T1.append(y2)
    T1.append(y3)

    # Joint 2
    y = b[1]
    y2 = [0]
    y2 = np.append(y2,np.divide(np.diff(y,1),np.power(dt,1)))
    y3 = [0,0]
    y3 = np.append(y3,np.divide(np.diff(y,2),np.power(dt,2)))
    T2 = []
    T2_rec = []
    T2_rec.append(y)
    T2.append(y)
    T2.append(y2)
    T2.append(y3)

    # Joint 3
    y = b[2]
    y2 = [0]
    y2 = np.append(y2,np.divide(np.diff(y,1),np.power(dt,1)))
    y3 = [0,0]
    y3 = np.append(y3,np.divide(np.diff(y,2),np.power(dt,2)))
    T3 = []
    T3_rec = []
    T3_rec.append(y)
    T3.append(y)
    T3.append(y2)
    T3.append(y3)  

    # Joint 4
    y = b[3]
    y2 = [0]
    y2 = np.append(y2,np.divide(np.diff(y,1),np.power(dt,1)))
    y3 = [0,0]
    y3 = np.append(y3,np.divide(np.diff(y,2),np.power(dt,2)))
    T4 = []
    T4_rec = []
    T4_rec.append(y)
    T4.append(y)
    T4.append(y2)
    T4.append(y3)

    # Joint 5
    y = b[4]
    y2 = [0]
    y2 = np.append(y2,np.divide(np.diff(y,1),np.power(dt,1)))
    y3 = [0,0]
    y3 = np.append(y3,np.divide(np.diff(y,2),np.power(dt,2)))
    T5 = []
    T5_rec = []
    T5_rec.append(y)
    T5.append(y)
    T5.append(y2)
    T5.append(y3)

    # Joint 6 - Gripper - NOT USED !!
    y = b[5]
    y2 = [0]
    y2 = np.append(y2,np.divide(np.diff(y,1),np.power(dt,1)))
    y3 = [0,0]
    y3 = np.append(y3,np.divide(np.diff(y,2),np.power(dt,2)))
    T6 = []
    T6_rec = []
    T6_rec.append(y)
    T6.append(y)
    T6.append(y2)
    T6.append(y3)

    # Joint 7 -  Gripper - NOT USED !!
    y = b[5]
    y2 = [0]
    y2 = np.append(y2,np.divide(np.diff(y,1),np.power(dt,1)))
    y3 = [0,0]
    y3 = np.append(y3,np.divide(np.diff(y,2),np.power(dt,2)))
    T7 = []
    T7_rec = []
    T7_rec.append(y)
    T7.append(y)
    T7.append(y2)
    T7.append(y3)

    # print ("Yep, I work bitches !! ")
    # print (T1[0])
    return T1, T2, T3, T4, T5, T6, T7


if __name__ == '__main__':

    # read_data_split(filename)
    demo_trajectory(0.005, filename)