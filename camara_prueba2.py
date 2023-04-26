#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os
import numpy as np

global image
global pub

def inicio():
    image = None
    br = CvBridge()
    loop_rate = rospy.Rate(30)
    pub = rospy.Publisher('imagetimer', Image,queue_size=20)
    este = rospy.Subscriber("/rbx1_p1/overview_camera/image_raw",Image,callback)
    


def start(image):
    rospy.loginfo("Timing images")
    loop_rate = rospy.Rate(30)
    while not rospy.is_shutdown():
        rospy.loginfo('publishing image')
        if image is not None:
            pub.publish(br.cv2_to_imgmsg(image))
        loop_rate.sleep()

def __del__(self):
    image.release()
    
def get_frame(self):
    _, frame = image.read()
    return frame
                
def run():
    while not rospy.is_shutdown():
        img = get_frame()
        cv2.imshow('frame',img)
        cv2.waitKey(10)

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    #rospy.loginfo(data.data)
    print(np.shape(data.header))
    rospy.loginfo('Image received...')
    CvBridge().imgmsg_to_cv2(data.data)
    
    #image = CvBridge().imgmsg_to_cv2(data.data, desired_encoding='passthrough')
    #res = cv2.resize(image, dsize=(640, 480))
    #res=cv2.cvtColor(res,cv2.COLOR_BGR2RGB)
    #cv2.imwrite('/home/santiago/Documentos/catkin_ws/src/tesis_rbx1/scripts/sift_keypoints.jpg',res)
    #cv2.imshow("Simulacion",res)
    #cv2.waitKey(30)
    
def listener():

   
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/rbx1_p1/overview_camera/image_raw",Image,callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

