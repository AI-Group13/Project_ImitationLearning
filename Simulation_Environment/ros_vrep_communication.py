#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from Imitation_Learn import *

Il = Imitation_Learn()
def iterate(data):
	print(data)
	a = str(data)[7:-2]
	s = a.split(' ')
	joint_list = [float(i) for i in s]
	print(joint_list)
	Il.log_data(joint_list, 'joint_list.csv')

def talker():
	pub = rospy.Publisher('signal',String, queue_size = 10)
	rospy.init_node('signal', anonymous=True)
	rate = rospy.Rate(10)
	
	x = 0.0
	z = 0.0
	for i in range(20):
		message = 'x'+str(x)+' y-0.00 z'+str(z)
		rospy.loginfo(message)
		pub.publish(message)
		rate.sleep()

	for i in range(20):
		message = 'x0.16 y0.0 z0.0'
		rospy.loginfo(message)
		pub.publish(message)
		rate.sleep()
		
	for i in range(20):
		message = 'x0.16 y0.0 z0.20'
		rospy.loginfo(message)
		pub.publish(message)
		rate.sleep()

	for i in range(30):
		message = 'x-0.16 y0.0 z0.20'
		rospy.loginfo(message)
		pub.publish(message)
		rate.sleep()

	for i in range(30):
		message = 'x-0.16 y0.0 z0.00001'
		rospy.loginfo(message)
		pub.publish(message)
		rate.sleep()

	for i in range(30):
		message = 'x0.00001 y0.0 z0.00001'
		rospy.loginfo(message)
		pub.publish(message)
		rate.sleep()

		# Currently not using the subscriber, inbuilt lua function works much better #
		#rospy.Subscriber('/joints', String, iterate)


if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
