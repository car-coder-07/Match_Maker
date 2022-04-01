# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 15:32:43 2022

@author: Saivardhan Baddela
"""
import time
import pyautogui
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img_count = 1
Match_found = False
MIN_MATCH_COUNT = 30

while Match_found == False:
    time.sleep(0.35)
    #image from tinder page
    pyautogui.screenshot(r"C:\Users\Saivardhan Baddela\Desktop\Tinder\my_screenshot.jpg", region=(952, 165, 506, 472))
    time.sleep(0.01)
    #comparing the features
    img1 = cv.imread(r"C:\Users\Saivardhan Baddela\Desktop\Tinder\test_1.jpg",0)    # query Image
    img2 = cv.imread(r"C:\Users\Saivardhan Baddela\Desktop\Tinder\my_screenshot.jpg",0) # train Image
    # Initiate SIFT detector
    sift = cv.SIFT_create()
    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks = 50)
    flann = cv.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1,des2,k=2)
    # store all the good matches as per Lowe's ratio test.
    good = []
    for m,n in matches:
        if m.distance < 0.7*n.distance:
            good.append(m)
            
    if len(good)>MIN_MATCH_COUNT:
        src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
        dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
        M, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC,5.0)
        matchesMask = mask.ravel().tolist()
        h,w = img1.shape
        pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
        dst = cv.perspectiveTransform(pts,M)
        img2 = cv.polylines(img2,[np.int32(dst)],True,255,3, cv.LINE_AA)
        print( "Match found - {}/{}".format(len(good), MIN_MATCH_COUNT) )
        matchesMask = None
        
        draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                       singlePointColor = None,
                       matchesMask = matchesMask, # draw only inliers
                       flags = 2)
        img3 = cv.drawMatches(img1,kp1,img2,kp2,good,None,**draw_params)
        plt.imshow(img3, 'gray'),plt.show()
        cv.imwrite(r"C:\Users\Saivardhan Baddela\Desktop\Tinder\Match_made.jpg", img3)
        """
        Code to like
        
        """
        #move cursor to like position
        #pyautogui.moveTo(1302, 828, 0.2)   # moves mouse to X of 1302, Y of 828 over 0.2 seconds
        pyautogui.click(x=1302, y=828)
        pyautogui.click(x=1313, y=986) #redendency when profile opens
        Match_found = True
        
    else:
        print( "Not enough features are found - {}/{}".format(len(good), MIN_MATCH_COUNT) )
        """
        Code to next img
        
        """ 
        #time.sleep(0.25)
        #pyautogui.click(x=1421, y=475) #chrome
        pyautogui.click(x=1450, y=465) #Edge&chrome
        time.sleep(0.1)
        #print('Image_count: ', img_count) 
        img_count = img_count+1  
                
        if img_count == 9 :
            """
            Code to dislike
            
            """
            #time.sleep(0.25)
            #move cursor to dislike position
            #pyautogui.moveTo(1302, 828, 0.2)   # moves mouse to X of 1302, Y of 828 over 0.2 seconds
            pyautogui.click(x=1111, y=819)
            pyautogui.click(x=1097, y=980) #redendency when profile opens
            #time.sleep(1)
            img_count = 1
                