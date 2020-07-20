# Image-Scaling
Image scaling is the operation used in Digit Image Processing. Image scaling refers to the resizing of a digital image.

Consider a window (a rectangular area) of a given size for the display within which the
zoomed-in or out area is shown when placed on the image.


## Description
The  basic intent of this project is to perform the scaling to an image. The scaling up should be done by

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**<ins>a. Replication :</ins>** It is also known as Nearest neighbor interpolation. As its name suggest , in this method , we just replicate the neighboring pixels. we create new pixels form the already given pixels. Each pixel is replicated in this method n times row wise and column wise and you got a zoomed image.

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**<ins>b. Interpolation :</ins>** Image interpolation occurs when you resize or distort your image from one pixel grid to another. Interpolation works by using known data to estimate values at unknown points. Image interpolation works in two directions, and tries to achieve a best approximation of a pixel's intensity based on the values at surrounding pixels. 
  
  ## Installation and Working
  1. Install openCv in your operating system.
  
  2. Install python
  
  3. Download the source code and test.png in the same folder
  
  4. Run the program using python image_scaling.py
  
  5. 3 windows will open when you will move your mouse pointer in the image
  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a. Original image of particular area for which you want to zoom
  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b. Replicated Image
  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c. Interpolated Image

  
      
  
  
  


