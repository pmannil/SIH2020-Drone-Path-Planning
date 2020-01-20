import numpy as np
import cv2

def cropImage(img,top,bottom,right,left):
    return img[top:bottom,left:right]


def readNcrop(path,name):
    inimg=cv2.imread(path+name+"grid.png")
    cv2.threshold(inimg,200,255,cv2.THRESH_BINARY) 
    left = 0 
    right = 0 
    top = 0 
    bottom = 0  
    sh0 = sh[0]//2 
    sh1 = sh[1]//2
    leng = []
    wid = []
    for i in range(len(inimg)): 
        if(thresh1[sh0][i] == 0):
            leng.append(i)
    trans= thresh1.transpose()
    for j in range(len(trans)):
        if(trans[sh1][j] == 0):
            wid.append(j)  
    left=leng[0]
    right=leng[-1]
    bottom=wid[-1] 
    top=wid[0] 
    outimg=cropImage(cv.imread(path+name+"out.png"),top,bottom,right,left)
    h,w=outimg.shape
    scaledw=(w//h)*1080
    resized=cv2.resize(outimg,(scaledw,1080),interpolation = cv2.INTER_AREA) 
    cv2.imwrite(path+name+"real.png",resized)   




        