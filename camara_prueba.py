#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os
import numpy as np

class Nodo(object):
    def __init__(self):
        self.image = None
        self.br = CvBridge()
        self.loop_rate = rospy.Rate(30)
        self.pub = rospy.Publisher('imagetimer', Image,queue_size=20)
        rospy.Subscriber("/rbx1_p1/overview_camera/image_raw",Image,self.callback)

    def callback(self, msg):
        rospy.loginfo('Image received...')
        self.image = self.br.imgmsg_to_cv2(msg)
        res = cv2.resize(self.image, dsize=(640, 480))
        res=cv2.cvtColor(res,cv2.COLOR_BGR2RGB)
        cv2.imwrite('/home/santiago/Documentos/catkin_ws/src/tesis_rbx1/scripts/sift_keypoints.jpg',res)
        cv2.imshow("Simulacion",res)
        cv2.waitKey(30)

    def start(self):
        rospy.loginfo("Timing images")
        while not rospy.is_shutdown():
            rospy.loginfo('publishing image')
            if self.image is not None:
                self.pub.publish(self.br.cv2_to_imgmsg(self.image))
            self.loop_rate.sleep()

    def __del__(self):
        self.image.release()
    
    def get_frame(self):
        _, frame = self.image.read()
        return frame
                
    def run(self):
        while not rospy.is_shutdown():
            img = self.get_frame()
            cv2.imshow('frame',img)
            cv2.waitKey(10)

rospy.init_node("imagetimer111", anonymous=True)
my_node = Nodo()
my_node.start()
