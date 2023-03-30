import os
import cv2
import numpy as np
from shutil import copyfile

# Set the new width and height
new_width = 200
new_height = 200
threshold=10000000
path='D:/crop'
print(path)
subdirectories = [os.path.join(path, f) for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
print(subdirectories)
for subdir in subdirectories:
    # Get a list of all image files in the subdirectory
    image_files = [os.path.join(subdir, f) for f in os.listdir(subdir) if os.path.isfile(os.path.join(subdir, f))]
    print(image_files)
    
    # Split the images into batches of 2000
    num_batches = int(np.ceil(len(image_files)/2000))
    for batch_idx in range(num_batches):
        start_idx = batch_idx * 2000
        end_idx = min((batch_idx+1)*2000, len(image_files))
        batch_files = image_files[start_idx:end_idx]

        # Load the images and resize them
        images = []
        for file in batch_files:
            image = cv2.imread(file)
            image_resized = cv2.resize(image, (new_width, new_height))
            images.append(image_resized)
        # Check that all images have the same size and number of channels
        size_check = all(image.shape == images[0].shape for image in images)
        channel_check = all(image.shape[-1] == images[0].shape[-1] for image in images)
        if not size_check or not channel_check:
            print(f"Not all images in {subdir} have the same size or number of channels. Skipping batch {batch_idx+1}...")
            continue
        # Compute the differences between the images
        diffs = []        
        for i in range(len(images)):
            for j in range(i+1, len(images)):
                diff = cv2.absdiff(images[i], images[j])
                diffs.append(np.sum(diff))
        # Find the image with the highest sum of differences
        odd_index = np.argmax(diffs)
        if odd_index >= len(batch_files):
            print(f"Odd index {odd_index} out of range for batch {batch_idx+1} in {subdir}. Skipping...")
            continue
        odd_image = batch_files[odd_index]
        # Copy all cropped images except the odd one to a new directory
        out_dir = os.path.join(subdir, 'output')
        os.makedirs(out_dir, exist_ok=True)
        for i, file in enumerate(batch_files):
            if i != odd_index:
                out_file = os.path.join(out_dir, os.path.basename(file))
                copyfile(file, out_file)
        # Print the odd image file path
        print(f"Odd image in batch {batch_idx+1} of {subdir}: {odd_image}")