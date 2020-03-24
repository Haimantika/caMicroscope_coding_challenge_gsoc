# caMicroscope_coding_challenge_gsoc
# MACHINE LEARNING SMARTPENS
## Code Challenge: Create a page or tool which performs edge detection on a given image and, given a point,returns the distance from that point to the closest edge
---
## Using OpenCV
For edge detection OpenCV has an inbuilt function 'canny edge detection'
Theory
Canny Edge Detection is a popular edge detection algorithm. It was developed by John F. Canny in 1986. It is a multi-stage algorithm and we will go through each stages.

1. Noise Reduction
Since edge detection is susceptible to noise in the image, first step is to remove the noise in the image with a 5x5 Gaussian filter. We have already seen this in previous chapters.

2. Finding Intensity Gradient of the Image
Smoothened image is then filtered with a Sobel kernel in both horizontal and vertical direction to get first derivative in horizontal direction (G_x) and vertical direction (G_y). 
Gradient direction is always perpendicular to edges. It is rounded to one of four angles representing vertical, horizontal and two diagonal directions.

3. Non-maximum Suppression
After getting gradient magnitude and direction, a full scan of image is done to remove any unwanted pixels which may not constitute the edge. For this, at every pixel, pixel is checked if it is a local maximum in its neighborhood in the direction of gradient. Check the image below:


Point A is on the edge ( in vertical direction). Gradient direction is normal to the edge. Point B and C are in gradient directions. So point A is checked with point B and C to see if it forms a local maximum. If so, it is considered for next stage, otherwise, it is suppressed ( put to zero).
In short, the result you get is a binary image with “thin edges”.

4. Hysteresis Thresholding
This stage decides which are all edges are really edges and which are not. For this, we need two threshold values, minVal and maxVal. Any edges with intensity gradient more than maxVal are sure to be edges and those below minVal are sure to be non-edges, so discarded. Those who lie between these two thresholds are classified edges or non-edges based on their connectivity. If they are connected to “sure-edge” pixels, they are considered to be part of edges.
This stage also removes small pixels noises on the assumption that edges are long lines.
So what we finally get is strong edges in the image.

For more info visit: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_canny/py_canny.html

## Nearest path in 2D matrix
A simple solution is to do BFS or DFS to find if there is a path.

A better solution is to mark all accessible nodes by changing their value to 1. First, change the value of the first top left element value to 1. Then get the next (current) value in the first row and compare to the previous value. Set this current value equal to the previous value only if it is reachable (not equal to -1). Similarly, do the same for column values, by comparing and setting the current with the previous column’s value if it is reachable.
Then start from the first-row & first column and take the values of previous row & the previous column. Find the max between them, and set the current index to that max. If the current index value is -1 then there’s no change.
In the end, if the final index at right bottom is 1 then return yes else return no.
