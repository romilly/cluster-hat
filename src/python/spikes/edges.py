import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load an color image
img = cv2.imread('p2.jpg')

cv2.imshow('image',img)
edges = cv2.Canny(img,50,50)

plt.subplot(121),plt.imshow(img)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
