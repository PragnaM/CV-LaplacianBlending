# Import open-cv and numpy libraries
import cv2
import numpy as np

# Read apple and orange image using opencv command- imread
apple = cv2.imread('apple.png')
orange = cv2.imread('orange.png')
print(apple.shape)
print(orange.shape)

# Generating Gaussian pyramid for apple

# create a copy of the image
apple_copy = apple.copy()

# add the image copy to a list-This list will contain all images in the Gaussian pyramid
gp_apple = [apple_copy]

# Generate Gaussian Pyramid by using pyrDown command and add each image to the list
for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)
    # display Gaussian Pyramid for Apple with 1.5s delay between images
    cv2.imshow(str(i), apple_copy)
    cv2.waitKey(800)
    cv2.destroyAllWindows()

# Generate Gaussian pyramid for orange

# create a copy of the image
orange_copy = orange.copy()

# add the image copy to a list-This list will contain all images in the Gaussian pyramid
gp_orange = [orange_copy]

# Generate Gaussian Pyramid by using pyrDown command and add each image to the list
for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)
    # display Gaussian Pyramid for Orange with 1.5s delay between images
    cv2.imshow(str(i), orange_copy)
    cv2.waitKey(800)
    cv2.destroyAllWindows()

# Generate Laplacian Pyramid for apple
# Difference between that level in Gaussian Pyramid and expanded version of its upper level in Gaussian pyramid

# Consider the uppermost level - 5 in our case
apple_copy_lp = gp_apple[5]
lp_apple = [apple_copy_lp]

# Decrement from uppermost level to level 0 in the pyramid
for i in range(5, 0, -1):
    # form the expanded version of the image using pyrUp command
    gaussian_apple_expanded = cv2.pyrUp(gp_apple[i])
    # calculate the difference
    laplacian_apple = cv2.subtract(gp_apple[i-1], gaussian_apple_expanded)
    lp_apple.append(laplacian_apple)
    # display Laplacian Pyramid for Orange with 1.5s delay between images
    cv2.imshow(str(i), laplacian_apple)
    cv2.waitKey(800)
    cv2.destroyAllWindows()

# Generate Laplacian Pyramid for orange
# Difference between that level in Gaussian Pyramid and expanded version of its upper level in Gaussian pyramid

# Consider the uppermost level - 5 in our case
orange_copy = gp_orange[5]
lp_orange = [orange_copy]

# Decrement from uppermost level to level 0 in the pyramid
for i in range(5, 0, -1):
    # form the expanded version of the image using pyrUp command
    gaussian_orange_expanded = cv2.pyrUp(gp_orange[i])
    # calculate the difference
    laplacian_orange = cv2.subtract(gp_orange[i-1], gaussian_orange_expanded)
    lp_orange.append(laplacian_orange)
    # display Laplacian Pyramid for Orange with 1.5s delay between images
    cv2.imshow(str(i), laplacian_orange)
    cv2.waitKey(800)
    cv2.destroyAllWindows()

# Combining left half of apple and right half of orange in each level of the corresponding laplacian pyramids
apple_orange_pyramid = []
n = 0

for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n += 1
    cols, rows, channels = apple_lap.shape
    laplacian_apple_orange = np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian_apple_orange)

# Up scaling and reconstructing
apple_orange_blend = apple_orange_pyramid[0]
for i in range(1, 6):
    # form the expanded version of the combined laplacian pyramid
    apple_orange_blend = cv2.pyrUp(apple_orange_blend)
    apple_orange_blend = cv2.add(apple_orange_pyramid[i], apple_orange_blend)
    cv2.imshow("apple-orange", apple_orange_blend)
    cv2.waitKey(800)
    cv2.destroyAllWindows()

# display the final blended image
cv2.imshow("apple-orange", apple_orange_blend)
cv2.waitKey(0)
cv2.destroyAllWindows()
