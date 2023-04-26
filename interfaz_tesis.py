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

# Global Variables
bridge = CvBridge()
ventana = tk.Tk()
ventana.geometry("750x620")
video = None
global video2
global captura_gazebo
video2 = None

def video_stream():
    global video
    video = cv2.VideoCapture(0)
    iniciar()

def iniciar():
    global video
    ret, frame = video.read()
    if(ret == True):
        frame = imutils.resize(frame, width= 700)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = PIL.Image.fromarray(frame)
        image = ImageTk.PhotoImage(image=img)
        etiq_de_video.config(image=image)
        etiq_de_video.image = image
        etiq_de_video.after(10,iniciar)
    

def quitar():
    global video
    video.release()





ventana.title("ROBOT RBX1")
ventana.config(width=500, height=300)

# Colores
fondo_verde= "#7EC94D"
fondo_rojo= "#EC6F3C"


# Botones
boton = tk.Button(ventana, text="Start video", bg=fondo_verde, relief="flat", cursor="hand2", command=video_stream, width=15, height=2, font=(15))
boton.place(x=180, y=550)

boton2 = tk.Button(ventana, text="Stop video", bg=fondo_rojo, relief="flat", cursor="hand2", command=quitar, width=15, height=2, font=(15))
boton2.place(x=380, y=550)

# Etiquetas

etiq_de_video = tk.Label(ventana)
etiq_de_video.place(x=20, y=20)

ventana.mainloop()
