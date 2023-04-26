#!/usr/bin/python2.7
from Tkinter import *
import Tkinter as tk
import ctypes
from matplotlib import image
import numpy as np #
import cv2 #
from PIL import Image #
from PIL import ImageTk 
import imutils #
import PIL.Image
import socket
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import os
import rospy
import time
from std_msgs.msg import Float64
import math

app = tk.Tk()
app.geometry("700x250")
fondo_verde= "#7EC94D"
bridge = CvBridge()
ruta_gazebo = '/rbx1_p1/overview_camera/image_raw'
ruta2_imagen = '/home/santiago/Documentos/catkin_ws/src/tesis_rbx1/scripts/hola.jpg'
rospy.init_node('talker', anonymous=True)
host = "172.18.8.242"
port = 8000
objsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
objsocket.connect((host, port))

def guardar():
    j1 = -entry1.get()
    j2 = entry2.get()
    j3 = entry3.get()
    j4 = entry4.get()
    j5 = entry5.get()
    j6 = entry6.get()
    pub = rospy.Publisher('/rbx1_p1/joint1_position_controller/command', Float64, queue_size=10)
    pub1 = rospy.Publisher('/rbx1_p1/joint2_position_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/rbx1_p1/joint3_position_controller/command', Float64, queue_size=10)
    listado_letras = str(j1) + "," + str(j2) + "," + str(j3) + "," + str(j4) + "," + str(j5) + "," + str(j6) + ","
    print(listado_letras)
    objsocket.send(listado_letras.encode(encoding="ascii", errors="ignore"))
    rate = rospy.Rate(8)
    for i in range(20):
        pub.publish(-math.pi*j1/180)
        pub1.publish(math.pi*j2/180)
        pub2.publish(math.pi*j3/180)
        rate.sleep()
        
    print("Iniciamos la comunicacion")
    
def talker1():
    try:
        guardar()
    except rospy.ROSInterruptException:
        pass

label1 = tk.Label(app, text="Join1: ", font=(15))
label1.place(x=10, y=10)

label2 = tk.Label(app, text="Join2: ", font=(15))
label2.place(x=10, y=50)

label3 = tk.Label(app, text="Join3: ", font=(15))
label3.place(x=10, y=90)

entry1 = IntVar()
textfield1 = tk.Entry(app, textvariable=entry1, font=(16)).place(x=70, y=10)

entry2 = IntVar()
textfield2 = tk.Entry(app, textvariable=entry2, font=(16)).place(x=70, y=50)

entry3 = IntVar()
textfield3 = tk.Entry(app, textvariable=entry3, font=(16)).place(x=70, y=90)

entry4 = IntVar()
textfield4 = tk.Entry(app, textvariable=entry4, font=(16)).place(x=350, y=10)

entry5 = IntVar()
textfield5 = tk.Entry(app, textvariable=entry5, font=(16)).place(x=350, y=50)

entry6 = IntVar()
textfield6 = tk.Entry(app, textvariable=entry6, font=(16)).place(x=350, y=90)

boton = tk.Button(app, text="Save Data", bg=fondo_verde, relief="flat", cursor="hand2", command=talker1, width=15, height=2, font=(15))
boton.place(x=250, y=130)

label1 = tk.Label(app, text="P_x: ", font=(15))
label1.place(x=10, y=10)

label1 = tk.Label(app, text="P_y: ", font=(15))
label1.place(x=10, y=50)

label1 = tk.Label(app, text="P_z: ", font=(15))
label1.place(x=10, y=90)

label1 = tk.Label(app, text="Vel 1: ", font=(15))
label1.place(x=300, y=10)

label1 = tk.Label(app, text="Vel 2: ", font=(15))
label1.place(x=300, y=50)

label1 = tk.Label(app, text="Vel 3: ", font=(15))
label1.place(x=300, y=90)

app.mainloop()




