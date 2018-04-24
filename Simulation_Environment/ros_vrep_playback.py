#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from Imitation_Learn import *
import numpy as np
import csv

j0 = []
j1 = []
j2 = []
j3 = []
j4 = []
with open('ik_joint_data.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		lists = row[0].split(',')
		values = [float(i) for i in lists]
		j0.append(values[0])
		j1.append(values[1])
		j2.append(values[2])
		j3.append(values[3])
		j4.append(values[4])


def talker():
	pub = rospy.Publisher('Joints',String, queue_size = 10)
	rospy.init_node('signal', anonymous=True)
	rate = rospy.Rate(50)

	for i in range(len(j0)):
		message = 'j0'+str(j0[i])+' '+'j1'+str(j1[i])+' '+'j2'+str(j2[i])+' '+'j3'+str(j3[i])+' '+'j4'+str(j4[i])
		rospy.loginfo(message)
		pub.publish(message)
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
