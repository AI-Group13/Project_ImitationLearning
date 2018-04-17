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
	while not rospy.is_shutdown():
		message = 'x-0.018 y-0.096 z0.308'
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
