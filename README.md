# CV-LaplacianBlending

# Problem Statement:
Creating the combined image of an apple and orange using Laplacian Blending.

# Description:
1.	Image Pyramids- Image pyramids are set of images with different resolutions. The image with highest resolution is on top and the image with lowest resolution is at the bottom when the images are stacked.
2.	Gaussian Pyramid- A Gaussian Pyramid is a type of image pyramid in which the Higher level (Low resolution) is formed by removing consecutive rows and columns in Lower level (higher resolution) image. Each pixel in higher level is formed by the contribution from 5 pixels in underlying level with gaussian weights. The area thus reduces to one-fourth of original area. 
3.	Laplacian Pyramid- Laplacian Pyramids are formed from the Gaussian Pyramids and are like edge images only. A level in Laplacian Pyramid is formed by the difference between that level in Gaussian Pyramid and expanded version of its upper level in Gaussian Pyramid. 
4.	Image Blending- Image blending is an application of image pyramids where two images can be blended seamlessly using both Gaussian and Laplacian pyramids.

# Working of the Program:
1.	Read the image files, apple.png and orange.png.
2.	Generate a Gaussian pyramid for apple and display it.
3.	Generate a Gaussian pyramid for orange and display it.
4.	Generate a Laplacian pyramid for apple from the Gaussian pyramid of apple and display.
5.	Generate a Laplacian pyramid for orange from the Gaussian pyramid of orange and display.
6.	Create a combined Laplacian pyramid of apple and orange, by taking the left half of apple image and right half of orange image at each level of the corresponding Laplacian pyramids.
7.	Reconstruct the image by upscaling. 
8.	Display the blended image of apple and orange.

(More explanation is included in the comments in code)
