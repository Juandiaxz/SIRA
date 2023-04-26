#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os
import numpy as np


if __name__ == '__main__':
    rospy.init_node("imagetimer111", anonymous=True)

    def callback(msg):
        rospy.loginfo('Image received...')
        image = br.imgmsg_to_cv2(msg)
        cv2.imshow("Simulation",image)
        cv2.imwrite(filename="eeeeee.jpg", img=image)


    image = None
    br = CvBridge()
    loop_rate = rospy.Rate(1)

    rospy.Subscriber("/rbx1_p1/overview_camera/image_raw",Image,callback) 
