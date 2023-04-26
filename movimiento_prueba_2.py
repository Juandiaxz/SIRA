#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import rospy
from std_msgs.msg import Float64
import math
paseo =30
def talker():
    pub = rospy.Publisher('/rbx1_p1/joint1_position_controller/command', Float64, queue_size=10)
    pub1 = rospy.Publisher('/rbx1_p1/joint2_position_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/rbx1_p1/joint3_position_controller/command', Float64, queue_size=10)
    pub3 = rospy.Publisher('/rbx1_p1/joint4_position_controller/command', Float64, queue_size=10)
    pub4 = rospy.Publisher('/rbx1_p1/joint5_position_controller/command', Float64, queue_size=10)
    pub5 = rospy.Publisher('/rbx1_p1/joint6_position_controller/command', Float64, queue_size=10)
    pub6 = rospy.Publisher('/rbx1_p1/joint7_position_controller/command', Float64, queue_size=10)

    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(8) # 10hz
    for i in range(paseo):
        #hello_str = "hello world %s" % rospy.get_time()
        position = math.pi/2
        rospy.loginfo(position)
        pub.publish(-position)
        #pub1.publish(-position/4)
        #pub2.publish(-position/4)
        #pub3.publish(-position/4)
        #pub4.publish(-position/4)
        #pub5.publish(-position/4)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass