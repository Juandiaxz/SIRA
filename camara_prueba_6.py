#! /usr/bin/python
import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import Float64
from cv_bridge import CvBridge, CvBridgeError
import cv2
import time
import math

bridge = CvBridge()
ruta_gazebo = '/rbx1_p1/overview_camera/image_raw'
ruta2_imagen = '/home/santiago/Documentos/catkin_ws/src/tesis_rbx1/scripts/hola.jpg'

def image_callback(msg):
    try:
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
        res = cv2.resize(cv2_img, dsize=(640, 480))
        cv2.imwrite(ruta2_imagen, res)
        cv2.imshow("Simulacion",res)
        cv2.waitKey(5)

    except CvBridgeError as e:
        print(e)

def main():
    rospy.init_node('image_listener')
    image_topic = ruta_gazebo
    rospy.Subscriber(image_topic, Image, image_callback)
    rospy.spin()

if __name__ == '__main__':
    main()
    