#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[2]:


def grayscale(img):
    
# rumus gray = sum(b, g, r) / 3
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i, j] = sum(img[i, j]) / 3
    return img

def edge(img):
    
    k= np.array([[-1,0,1], [-1,0,1], [-1,0,1]])
    kernel_w = k.shape[0]//2
    kernel_h = k.shape[1]//2
    
    gray = grayscale(img)
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    outputImg = np.zeros(gray.shape)
    
    for x in range (gray.shape[0]-kernel_w):
        for y in range(gray.shape[1]-kernel_h):
            for k1 in range (k.shape[0]):
                for k2 in range (k.shape[1]):
                     outputImg[x,y] = outputImg[x,y] + k[k1,k2] * gray[x+k1-kernel_w, y+k2-kernel_h]
            
    return outputImg

def edgedet(img):
    k= np.array([[-1,0,1], [-1,0,1], [-1,0,1]])
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    convolve = cv2.filter2D(gray, -1, k)
    
    return convolve


# In[4]:


image1 =  cv2.imread('logo.png')
image =  cv2.imread('logo.png')

gray = grayscale(image1)
res2 = edge(image1)


cv2.imshow('before', image)
cv2.imshow('grayscale', gray)
cv2.imshow('edge detection', res2)
cv2.waitKey()


# In[ ]:




