 #!/usr/bin/env python2.7
import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError
import math

L0=79.75
L1=152.75
L2=221.12
L3=354.06

px=5.0
py=6.0
pz=9.0

cos_rho=(px**2+py**2+(pz-L1)**2-L2**2-L3**2)/(2*L2*L3)

q3=(math.atan((math.sqrt(1-cos_rho))/cos_rho))
q3_=q3*180/math.pi
print(q3_)

q2=math.atan((pz-L1)/(math.sqrt(px**2+py**2)))-math.atan((L3*math.sin(q3))/(L2+L3*math.cos(q3)))
q2_=q2*180/math.pi
print(q2_)

q1=math.atan(py/px)
q1_=q1*180/math.pi
print(q1_)


  