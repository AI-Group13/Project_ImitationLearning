#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Pose
from Imitation_Learn import *
from sensor_msgs.msg import Joy


pub = rospy.Publisher('signal',Pose, queue_size = 10)

def callback(data):
    rospy.loginfo(data)
    pos = Pose()
    pos.position.x = data.axes[0]*0.3
    pos.position.z = data.axes[4]*0.3
    pub.publish(pos)

def talker():

    rospy.init_node('Control', anonymous=True)
    rospy.Subscriber("/joy",Joy,callback)
    rospy.spin()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
