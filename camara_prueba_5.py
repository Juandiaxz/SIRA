#!/usr/bin/env python2.7
import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError

bridge = CvBridge()

ruta ='/rbx1_p1/overview_camera/image_raw'
def show_image(img):
  cv2.imshow("Image Window", img)
  cv2.waitKey(3)

def image_callback(img_msg):
  rospy.loginfo(img_msg.header)
  try:

    cv_image = CvBridge().imgsg_to_cv2(img_msg)
    cv_image = cv2.resize(cv_image, dsize=(640, 480))
    cv2.imwrite('/home/santiago/Documentos/catkin_ws/src/tesis_rbx1/scripts/sift_keypoints.jpg',cv_image)
    cv2.imshow("Simulacion",cv_image)
  except CvBridgeError as e:
    print(e)
    #rospy.logerr("CvBridge Error: {0}".format(e))
  #show_image(cv_image)
# Initalize a subscriber to the "/camera/rgb/image_raw" topic with the function "image_callback" as a callback
sub_image = rospy.Subscriber(ruta, Image, image_callback)
cv2.namedWindow("Image Window", 1)


rospy.init_node('opencv_example', anonymous=True)
#rospy.loginfo("Hello ROS!")

while not rospy.is_shutdown():
  rospy.spin()
