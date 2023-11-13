import cv2
import numpy as np
from matplotlib import pyplot as plt
plt.style.use('seaborn')
brightness = 7
# contrast = 1.2
# Create the sharpening kernel 
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) 
  
# Sharpen the image 
image = cv2.imread('noisy2.png')
sharpened_image = cv2.filter2D(image, -10, kernel) 
dst = cv2.fastNlMeansDenoisingColored(image, None, 11, 6, 7, 21)

 
row, col = 1, 2
fig, axs = plt.subplots(row, col, figsize=(15, 10))
fig.tight_layout()
axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[0].set_title('Elephant')
axs[1].imshow(cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2RGB))
axs[1].set_title('Fast Means Denoising')
plt.show()