#The coding challenge (probably) will end up having two steps; 1) detect the edge of an object and 2) for an arbitrary point, return which position on the edge of the object is closest.
#image gradients using opencv
import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while(1):

    # Take each frame
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    laplacian = cv2.Laplacian(frame,cv2.CV_64F)
    sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)

    cv2.imshow('Original',frame)
    cv2.imshow('Mask',mask)
    cv2.imshow('laplacian',laplacian)
    cv2.imshow('sobelx',sobelx)
    cv2.imshow('sobely',sobely)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()

#Using the gradients to convert to pure edges by canny edge detection
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('Original',frame)
    edges = cv2.Canny(frame,100,200)
    cv2.imshow('Edges',edges)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()


#for nearest value
row = 5
col = 5
  
# to find the path from  
# top left to bottom right  
def isPath(arr): 
      
    # set arr[0][0] = 1 
    arr[0][0] = 1
  
    # Mark reachable (from top left)  
    # nodes in first row and first column.  
    for i in range(1, row): 
        if (arr[i][0] != -1): 
            arr[i][0] = arr[i-1][0] 
  
    for j in range(1, col): 
        if (arr[0][j] != -1): 
            arr[0][j] = arr[0][j-1] 
              
    # Mark reachable nodes in  
    # remaining matrix.  
    for i in range(1, row): 
        for j in range(1, col): 
            if (arr[i][j] != -1): 
                arr[i][j] = max(arr[i][j - 1],  
                                arr[i - 1][j]) 
                                  
    # return yes if right  
    # bottom index is 1 
    return (arr[row - 1][col - 1] == 1) 
  
# Driver Code  
  
# Given array  
arr = [[ 0, 0, 0, -1, 0 ],  
       [-1, 0, 0, -1, -1],  
       [ 0, 0, 0, -1, 0 ],  
       [-1, 0, -1, 0, -1],  
       [ 0, 0, -1, 0, 0 ]]  
  
# path from arr[0][0] to arr[row][col]  
if (isPath(arr)): 
    print("Yes")  
else: 
    print("No") 
