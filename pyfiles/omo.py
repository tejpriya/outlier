import os
import cv2
import numpy as np
from shutil import copyfile


path='D:/crop'
print(path)
new_width = 200
new_height = 200
resized_img = cv2.resize(image, (new_width, new_height))

subdirectories = [os.path.join(path, f) for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
print(subdirectories)
for subdir in subdirectories:
        # Get a list of all image files in the subdirectory
        image_files = [os.path.join(subdir, f) for f in os.listdir(subdir) if os.path.isfile(os.path.join(subdir, f))]
        print(image_files)
        # Load the images and convert them to grayscale
        images = []
        print(images)
        for file in image_files:
            image = cv2.imread(file)
            
            images.append(image)
            # Check that all images have the same size and number of channels
        size_check = all(image.shape == images[0].shape for image in images)
        channel_check = all(image.shape[-1] == images[0].shape[-1] for image in images)
        if not size_check or not channel_check:
            print(f"Not all images in {subdir} have the same size or number of channels. Skipping...")
            continue
        
        # Compute the differences between the images
        diffs = []        
        for i in range(len(images)):
            for j in range(i+1, len(images)):
                diff = cv2.absdiff(images[i], images[j])
                diffs.append(np.sum(diff))
        
        # Find the image with the highest sum of differences
        odd_index = np.argmax(diffs)
        odd_image = image_files[odd_index]
        
        # Copy all cropped images except the odd one to a new director
        out_dir = os.path.join(subdir, 'output')
        os.makedirs(out_dir, exist_ok=True)
        for i, file in enumerate(image_files):
            if i != odd_index:
                out_file = os.path.join(out_dir, os.path.basename(file))
                copyfile(file, out_file)
        
        # Print the odd image file path
        print(f"Odd image in {subdir}: {odd_image}")