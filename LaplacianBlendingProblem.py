import cv2

# Read apple and orange image using opencv command- imread
apple = cv2.imread('apple.png')
orange = cv2.imread('orange.png')

# Generating Gaussian pyramid for apple

# create a copy of the image
apple_copy = apple.copy()

# add the image copy to a list-This list will contain all images in the Gaussian pyramid
gp_apple = [apple_copy]

# Generate Gaussian Pyramid by using pyrDown command and add each image to the list
for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)
    # display Gaussian Pyramid for Apple with 3s delay between images
    cv2.imshow(str(i), apple_copy)
    cv2.waitKey(3000)
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
    # display Gaussian Pyramid for Orange with 3s delay between images
    cv2.imshow("orange_copy", orange_copy)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

