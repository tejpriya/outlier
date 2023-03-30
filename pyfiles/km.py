import cv2
import numpy as np
import os

# set input and output directories
input_dir = '"D:/old/chennai/images_clustered2'
output_dir = '"D:/old/chennai/images_clustered2/dissimilar_images'

# set threshold for dissimilarity
threshold = 0.8

# loop through each group folder in the input directory
for group_folder in os.listdir(input_dir):
    
    # create a list to store dissimilar images in the group
    dissimilar_images = []
    
    # read in the representative image for the group
    representative_image = cv2.imread(os.path.join(input_dir, group_folder, 'representative_image.jpg'))
    
    # loop through each image in the group folder
    for image_file in os.listdir(os.path.join(input_dir, group_folder)):
        
        # read in the image and resize it to the same size as the representative image
        image = cv2.imread(os.path.join(input_dir, group_folder, image_file))
        image = cv2.resize(image, representative_image.shape[:2])
        
        # calculate the structural similarity index (SSIM) between the image and the representative image
        ssim = cv2.compare_ssim(image, representative_image, multichannel=True)
        
        # if the image is dissimilar to the representative image, add it to the dissimilar images list
        if ssim < threshold:
            dissimilar_images.append(image_file)
    
    # create a new folder for the dissimilar images in the output directory
    os.makedirs(os.path.join(output_dir, group_folder), exist_ok=True)
    
    # move the dissimilar images to the output directory
    for image_file in dissimilar_images:
        os.rename(os.path.join(input_dir, group_folder, image_file), os.path.join(output_dir, group_folder, image_file))
