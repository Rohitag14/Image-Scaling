#    imagescaling.py
#    This program demonstrate the scaling operation
#    to an image using INTERPOLATION and REPLICATION

import cv2
import numpy as np
import math
 
 
def mouseRGB(event,x,y,flags,param):  
    if (event == cv2.EVENT_MOUSEMOVE): #checks mouse move condition
        a=np.zeros([100,100,3])     #creating numpy array for croping
        
        row=image.shape[0]        #image height
        c=image.shape[1]          #image width
        t1=0
        t2=0
    
        for i in range(max(0,x-50),min(c,x+50)):      #croppig image
            t2=0
            for j in range(max(0,y-50),min(row,y+50)):
                a[t1][t2] = image[j,i]
                t2+=1
            t1+=1
        
        cv2.imwrite('img_window.jpg', a)
        a1 = cv2.flip(a,1)
        a3 = cv2.rotate(a1,cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imwrite('img_window.jpg',a3)
        
        ip=np.zeros([199,199,3])               #numpy array for interpolated image
        for i in range(0,100):                 #implementing interpolation for zooming in
            for j in range(0,100):
                ip[i*2][j*2]=a3[i][j]
                if(j<99):
                    ip[i*2][j*2+1]=(a3[i][j]+a3[i][j+1])/2
                    if(i<99):
                        ip[i*2+1][j*2+1]=(a3[i][j]+a3[i+1][j+1])/2
                if(i<99):
                    ip[i*2+1][j*2]=(a3[i][j]+a3[i+1][j])/2

        cv2.imwrite('interpolated.jpg', ip)
        img1 = cv2.imread('interpolated.jpg')
        cv2.imshow("interpolated",img1)

        rc=np.zeros([200,200,3])             #numpy array for replicated image
        for i in range(0,100):               #implementing replication for zooming in
            for j in range(0,100):
                rc[i*2][j*2]=a3[i][j]
                if(j<99):
                    rc[i*2][j*2+1]=a3[i][j]
                    if(i<99):
                        rc[i*2+1][j*2+1]=a3[i][j]
                if(i<99):
                    rc[i*2+1][j*2]=a3[i][j][0]
                if(i==99 or j==99):
                    rc[i*2+1][j*2+1]=a3[i][j]
                    rc[i*2][j*2+1]=a3[i][j]
                    rc[i*2+1][j*2]=a3[i][j]      
        
        cv2.imwrite('replicated.jpg', rc)
        img2 = cv2.imread('replicated.jpg')
        cv2.imshow("replicated",img2)
        
        zo=np.zeros([50,50,3])          #numpy arry for zoomed out image
        for i in range (0,50):          #implementing zooming out
            for j in range (0,50):
                zo[i][j]=a3[2*i][2*j]

        cv2.imwrite('zout.jpg', zo)
        img3 = cv2.imread('zout.jpg')
        cv2.imshow('zout',img3)
        
       
image = cv2.imread("test1.webp")     #reading image
cv2.namedWindow('mouseRGB')
cv2.setMouseCallback('mouseRGB',mouseRGB)
 
while 1: #Do until esc pressed
    cv2.imshow('mouseRGB',image)
    if cv2.waitKey(20) & 0xFF == 27:
        break
#if esc pressed, finish.
cv2.destroyAllWindows()