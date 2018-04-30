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
def read_data():
	with open('circular_org.txt', 'r') as datafile:
		dd = csv.reader(datafile)
		for row in dd:
			data.append(row)

def split_data():
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
			rwra[0] = [ ast.literal_eval(data_points[a][i]) for a in range(105, 650)]
			rwra[1] = [ ast.literal_eval(data_points[a][i+1]) for a in range(105, 650)]
			rwra[2] = [ ast.literal_eval(data_points[a][i+2]) for a in range(105, 650)]
			# hndbr[0] = [p*0.4 for p in rwra[0]]
			# hndbr[1] = [p*0.4 for p in rwra[1]]
			# hndbr[2] = [p for p in rwra[2]]

def plot_data():
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	# ax.plot( map(add, lwra[0], lwrb[0]) , map(add, lwra[1],lwrb[1]), map(add, lwra[2], lwrb[2]), 'r-', label=' Averaged Data')
	ax.plot(lwra[0], lwra[1], lwra[2], 'r-', label='Left Wirst Marker A')
	# ax.plot(lwrb[0], lwrb[1], lwrb[2], 'g-', label='Left Wirst Marker B')
	# ax.plot(hndbr[0], hndbr[1], hndbr[2], 'b*', label='Hand B')
	# ax.plot(rwra[0], rwra[1], rwra[2], 'r*', label='Hand B')
	# ax.plot(lwrb[0], lwrb[1], lwrb[2], 'go', label='parametric curve')
	ax.legend()
	plt.show()

def plot2d():
	plt.plot(lwra[0][0:300], lwra[1][0:300])
	plt.grid()
	plt.show()


read_data()		
split_data()
plot_data()
# plot2d()

# ax.plot()