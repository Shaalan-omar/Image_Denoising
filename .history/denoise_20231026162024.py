# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
# plt.style.use('seaborn')
# brightness = 7
# # contrast = 1.2
# # Create the sharpening kernel 
# kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) 
  
# # Sharpen the image 
# image = cv2.imread('noisy.png')
# desnoised_image = cv2.fastNlMeansDenoisingColored(image, None, 11, 6, 7, 21)
# sharpened_image = cv2.filter2D(desnoised_image, -1000, kernel) 

import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

brightness = 7
# contrast = 1.2

# Create the sharpening kernel 
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) 

folder_path = 'Canine_Cases_20'  # Replace with the path to your folder containing images
output_folder = 'Output'  # Replace with the path to the folder where you want to save the processed images

image_files = os.listdir(folder_path)
for image_file in image_files:
    print(image_file)
    if image_file.endswith('.JPEG') or image_file.endswith('.JPG'):  # Check if the file is an image
        image_path = os.path.join(folder_path, image_file)  # Create the complete path to the image file
        print(folder_path)
        # Read the image using OpenCV
        image = cv2.imread(image_path)
        
        # Apply the image processing operations
        desnoised_image = cv2.fastNlMeansDenoisingColored(image, None, 11, 6, 7, 21)
        sharpened_image = cv2.filter2D(desnoised_image, -1000, kernel) 
        print('here')
        # Save the processed image to the output folder
        output_path = os.path.join(output_folder, image_file)  # Create the complete output path
      
        cv2.imwrite(output_path, sharpened_image)

# row, col = 1, 3
# fig, axs = plt.subplots(row, col, figsize=(5, 10))
# fig.tight_layout()
# axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# axs[0].set_title('Original')
# axs[1].imshow(cv2.cvtColor(desnoised_image, cv2.COLOR_BGR2RGB))
# axs[1].set_title('Denoised')
# axs[2].imshow(cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2RGB))
# axs[2].set_title('Sharpened')
# plt.savefig('Output/output.png')
# plt.show()