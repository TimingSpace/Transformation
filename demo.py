import cv2
import sys
import numpy as np
image_list_file = sys.argv[1]
ground_truth_file =sys.argv[2]
vo_file =sys.argv[3]
scale = 0.5
background_img = np.zeros((1000,1000,3),np.uint8)
cv2.putText(background_img,'DEMO KITTI 00 By Xiangwei',(100,500),5,2,(200,128,0),2)
cv2.imshow('Demo KITTI 00',background_img)
cv2.waitKey()
ground_truth = np.loadtxt(ground_truth_file)
vo_path = np.loadtxt(vo_file)
image_name_list = open(image_list_file)
background_img = np.zeros((1000,1000,3),np.uint8)
for i in range(0,vo_path.shape[0]):
    image_name = image_name_list.readline()
    image_name = image_name[:-1]
    image = cv2.imread(image_name)
    image=cv2.resize(image,(int(image.shape[1]/2),int(image.shape[0]/2)))
    cv2.circle(background_img,(500+int(scale*ground_truth[i,3]),500-int(scale*ground_truth[i,11])),1,(0,0,255),-1)
    cv2.circle(background_img,(500+int(scale*vo_path[i,3]),500-int(scale*vo_path[i,11])),1,(0,255,0),-1)
    background_img[0:image.shape[0],0:image.shape[1]] = image
    cv2.imshow('Demo KITTI 00',background_img)
    cv2.waitKey(1)
