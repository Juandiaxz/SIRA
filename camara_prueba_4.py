#!/usr/bin/env python
from ast import While
import rospy
import sys
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import numpy as np


bridge = CvBridge()

def start_node():
    rospy.init_node('image_pub')
    rospy.loginfo('image_pub node started')
    pub = rospy.Publisher('/rbx1_p1/overview_camera/image_raw', Image, queue_size=10)
    rospy.Subscriber("/rbx1_p1/overview_camera/image_raw", Image, process_image)
    rospy.Rate(60).sleep()
    #rospy.Rate(5)

def process_image(msg):
    try:
        rospy.loginfo('In Proccess ...')
        orig = bridge.imgmsg_to_cv2(msg)
        orig = cv2.resize(orig, dsize=(640, 480))
        orig =cv2.cvtColor(orig,cv2.COLOR_BGR2RGB)
        print(np.shape(orig))
        #rospy.Publisher('/rbx1_p1/overview_camera/image_raw', Image, queue_size=10).publish(bridge.cv2_to_imgmsg(orig, "bgr8"))
        cv2.imwrite('/home/santiago/Documentos/catkin_ws/src/tesis_rbx1/scripts/orig.jpg',orig)
        cv2.imshow("image", orig)
        cv2.waitKey(5)

    except Exception as err:
        print(err)
def correr():
    while True:
        try:
            start_node()
        except rospy.ROSInterruptException:
            pass


if __name__ == '__main__':
    correr()
