import os
import shutil
from PIL import Image
import imagehash

# set the directory paths for car images and wrongly classified images
img_dir = "D:/old/chennai/Cropped_Images/bus"
dup_dir = "D:/old/chennai/Cropped_Images"
if not os.path.exists(dup_dir):
    os.makedirs(dup_dir)
dis_dir = "D:/old/chennai/images_cluster00"   
if not os.path.exists(dis_dir):
    os.makedirs(dis_dir)  
# set the threshold value for image similarity
threshold = 5

# create a dictionary to store image hashes and paths
hash_dict = {}

# loop through all the images in the image directory
for filename in os.listdir(img_dir):
    filepath = os.path.join(img_dir, filename)
    
    # open the image using PIL
    with Image.open(filepath) as img:
        # generate the hash for the image using the dHash algorithm
        hash_value = imagehash.dhash(img)
    
    # check if the hash already exists in the dictionary
    if hash_value in hash_dict:
        # if the hash exists, the image is a duplicate, so move it to the duplicate directory
        shutil.move(filepath, dup_dir)
    else:
        # if the hash does not exist, add it to the dictionary with the file path
        hash_dict[hash_value] = filepath

# loop through all the hashes in the dictionary to find dissimilar images
for i, hash_key in enumerate(hash_dict):
    for j, hash_key_2 in enumerate(hash_dict):
        if i == j:
            continue
        
        # compare the hash keys to see if the images are dissimilar
        diff = hash_key - hash_key_2
        if diff >= threshold:
            # if the difference between the hashes is greater than or equal to the threshold, move the images to the dissimilar directory
            shutil.move(hash_dict[hash_key], dis_dir)
            shutil.move(hash_dict[hash_key_2], dis_dir)
