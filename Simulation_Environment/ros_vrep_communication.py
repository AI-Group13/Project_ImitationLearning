#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Pose
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
	pub = rospy.Publisher('signal',Pose, queue_size = 10)
	rospy.init_node('signal', anonymous=True)
	rate = rospy.Rate(10)
	pos = Pose()	

	for i in range(20):
		pos.position.x = 0.0
		pos.position.y = 0.0
		pos.position.z = 0.0
		rospy.loginfo(pos)
		pub.publish(pos)
		rate.sleep()

	for i in range(20):
		pos.position.x = 0.10
		pos.position.y = 0.0
		pos.position.z = 0.0
		rospy.loginfo(pos)
		pub.publish(pos)
		rate.sleep()
		
	for i in range(20):
		pos.position.x = 0.10
		pos.position.y = 0.0
		pos.position.z = 0.20
		rospy.loginfo(pos)
		pub.publish(pos)
		rate.sleep()

	for i in range(30):
		pos.position.x = -0.10
		pos.position.y = 0.0
		pos.position.z = 0.20
		rospy.loginfo(pos)
		pub.publish(pos)
		rate.sleep()

	for i in range(30):
		pos.position.x = -0.10
		pos.position.y = 0.0
		pos.position.z = 0.0001
		rospy.loginfo(pos)
		pub.publish(pos)
		rate.sleep()
	for i in range(30):
		pos.position.x = 0.0001
		pos.position.y = 0.0
		pos.position.z = 0.0001
		rospy.loginfo(pos)
		pub.publish(pos)
		rate.sleep()


if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
