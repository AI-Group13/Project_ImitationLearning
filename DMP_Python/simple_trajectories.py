
import numpy as np
import matplotlib.pyplot as plt 

def y_exp_trajectory(dt):    
    t = list(i for i in np.arange(0,1+dt,dt))
    y = list(np.power(t,2))
    y2 = [0]
    y2 = np.append(y2,np.divide(np.diff(y,1),np.power(dt,1)))
    y3 = [0,0]
    y3 = np.append(y3,np.divide(np.diff(y,2),np.power(dt,2)))
    T = []
    T_rec = []
    T_rec.append(y)
    T.append(y)
    T.append(y2)
    T.append(y3)
    return T

def y_lin_trajectory(dt):
    y = list(i for i in np.arange(0,1+dt,dt))
    y2 = [0]
    y2 = np.append(y2,np.divide(np.diff(y,1),np.power(dt,1)))
    y3 = [0,0]
    y3 = np.append(y3,np.divide(np.diff(y,2),np.power(dt,2)))
    T = []
    T_rec = []
    T_rec.append(y)
    T.append(y)
    T.append(y2)
    T.append(y3)
    return T    

def y_step_trajectory(dt):
    y = []
    for i in range(int(1/dt)/2):
        y.append(0)
    for i in range(int(1/dt)/2):
        y.append(1)
    y.append(1)
    y2 = [0]
    y2 = np.append(y2,np.divide(np.diff(y,1),np.power(dt,1)))
    y3 = [0,0]
    y3 = np.append(y3,np.divide(np.diff(y,2),np.power(dt,2)))
    T = []
    T_rec = []
    T_rec.append(y)
    T.append(y)
    T.append(y2)
    T.append(y3)
    return T   

# -----------------------------------------
# -----------------------------------------
# -----------------------------------------


import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import csv
import re
import ast
from operator import add


data = []
data_points = []
lwra, lwrb, hndar, hndbr, rwra, rwrb = [0]*3, [0]*3, [0]*3,[0]*3, [0]*3,[0]*3	
# mpl.rcParams['legend.fontsize'] = 10
def read_data_split():
    with open('circular_org.txt', 'r') as datafile:
        dd = csv.reader(datafile)
        for row in dd:
            data.append(row)

# def split_data():
    for i in range(3, len(data)):
        data_points.append(str(data[i][0]).split("\t"))
    # print (len((data_points[0])))
    for i in range(0, len(data_points[0])): 
        if 'LWRA' in data_points[0][i]:
            lwra[0] = [ ast.literal_eval(data_points[a][i]) for a in range(2, len(data_points))]
            lwra[1] = [ ast.literal_eval(data_points[a][i+1]) for a in range(2, len(data_points))]
            lwra[2] = [ ast.literal_eval(data_points[a][i+2]) for a in range(2, len(data_points))]
        if 'LWRB' in data_points[0][i]:
            lwrb[0] = [ ast.literal_eval(data_points[a][i]) for a in range(2, len(data_points))]
            lwrb[1] = [ ast.literal_eval(data_points[a][i+1]) for a in range(2, len(data_points))]
            lwrb[2] = [ ast.literal_eval(data_points[a][i+2]) for a in range(2, len(data_points))]
        if 'RWRA' in data_points[0][i]:
			rwra[0] = [ ast.literal_eval(data_points[a][i]) for a in range(105, 650)]          # 2, len(data_points))]
		 	rwra[1] = [ ast.literal_eval(data_points[a][i+1]) for a in range(105, 650)]        # 2, len(data_points))]
		 	rwra[2] = [ ast.literal_eval(data_points[a][i+2]) for a in range(105, 650)]        # 2, len(data_points))]
        # if 'HNDB' in data_points[0][i]:
        #     hndbr[0] = [ ast.literal_eval(data_points[a][i]) for a in range(2, len(data_points))]
        #     hndbr[1] = [ ast.literal_eval(data_points[a][i+1]) for a in range(2, len(data_points))]
        #     hndbr[2] = [ ast.literal_eval(data_points[a][i+2]) for a in range(2, len(data_points))]

    return rwra            


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

# -----------------------------------------
# -----------------------------------------
# -----------------------------------------


def demo_trajectory_right(dt):
    t = list(i for i in np.arange(0,1+dt,dt))
    y = read_data_split()[0] 
    y2 = [0]
    y2 = np.append(y2,np.divide(np.diff(y,1),np.power(dt,1)))
    y3 = [0,0]
    y3 = np.append(y3,np.divide(np.diff(y,2),np.power(dt,2)))
    T = []
    T2 = []
    T3 = []
    T_rec = []
    T_rec.append(y)
    T.append(y)
    T.append(y2)
    T.append(y3)
    return T, T2, T3



# plt.plot(y_exp_trajectory(0.001)[0])
# plt.show()