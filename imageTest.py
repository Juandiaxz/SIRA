#!/usr/bin/python2.7
#from pylab import ion
import sys
import platform
print(platform.python_version())
import rospy
from sensor_msgs.msg import Image
from sensor_msgs.msg import PointCloud2
import pdb
import cv2
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
bridge = CvBridge()
print ('Code Running 1!')

class TestCamera(object):
    def __init__(self):
        self.image_sub =rospy.Subscriber("/rbx1_p1/overview_camera/image_raw", Image, self.camera_callback)
        self.bridge_object=CvBridge
    def camera_callback(self,data):
        try:
            cv_image=bridge.imgmsg_to_cv2(data, "passthrough")
        except CvBridgeError as e:
            print(e)
        
        height,width,channels=cv_image.shape
        descentre=160
        ros_to_watch=60
        crop_img=cv_image[(height)/2+descentre:(height)/2+(descentre+ros_to_watch)][1:width]
        hsv=cv2.cvtColor(crop_img,cv2.COLOR_BGR2HSV)
        RGBIm=cv2.cvtColor(cv_image,cv2.COLOR_BGR2RGB)
	    #RGBIm = cv2.cvtColor(cv_image,cv2.COLOR_BGR2RGB)
        hsva=cv2.cvtColor(cv_image,cv2.COLOR_BGR2GRAY)
        sift=cv2.xfeatures2d.SIFT_create()
        kp = sift.detect(RGBIm,None)
        img=cv2.drawKeypoints(RGBIm,kp,outImage = None)
        #pdb.set_trace()
        cv2.imwrite('/home/santiago/Documentos/catkin_ws/src/tesis_rbx1/scripts/sift_keypoints.jpg',img)
        cv2.imwrite('/home/santiago/Documentos/catkin_ws/src/tesis_rbx1/scripts/imagetestp.jpg',cv_image)
	    
        cv2.imshow('image',hsva)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()


def main():
    rospy.init_node('camera_test_node',anonymous=True)
    camera_test_object=TestCamera()
    
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting Down")

if __name__ == "__main__":
    main()

	

