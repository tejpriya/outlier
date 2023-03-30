import os
import shutil
from PIL import Image
import imagehash
from pathlib import Path
# set the directory paths for car images and wrongly classified images
img_dir = Path("E:/Cropped_Images")
dup_dir = "E:/old/chennai/cro"
if not os.path.exists(dup_dir):
    os.makedirs(dup_dir)
dis_dir = Path("E:/old/chennai/crop/crp1")
dis_dir.mkdir(parents=True, exist_ok=True)   
if not os.path.exists(dis_dir):
    os.makedirs(dis_dir)  
# set the threshold value for image similarity
threshold = 5

# create a dictionary to store image hashes and paths
hash_dict = {}

# create a list to store the dissimilar images
dis_list = []
image_lists = []
# loop through all the images in the image directory
for filename in os.listdir(str(img_dir)):
    filepath = img_dir / filename
    # filepath = os.path.join(img_dir, filename)
    print(filepath)
    for im_path in os.listdir(str(filepath)):
        e_im_path = filepath / im_path
        image_lists.append(str(e_im_path))
        # open the image using PIL
        
for im_path1 in image_lists:
        with Image.open(str(e_im_path)) as img:
            # generate the hash for the image using the dHash algorithm
            hash_value = imagehash.dhash(img)
        
        # save_path = e_im_path.parent / "test" / e_im_path.name
        # save_path.mkdir(parents=True, exist_ok=True)
        # check if the hash already exists in the dictionary
        save_file = dis_dir / e_im_path.name
        print("#####",str(e_im_path), str(save_file))
        if hash_value in hash_dict:
            # if the hash exists, the image is a duplicate, so move it to the duplicate directory
           
            shutil.move(str(e_im_path), str(save_file))
        else:
            # if the hash does not exist, add it to the dictionary with the file path
            hash_dict[hash_value] = str(e_im_path)

# loop through all the hashes in the dictionary to find dissimilar images
for i, hash_key in enumerate(hash_dict):
    for j, hash_key_2 in list(enumerate(hash_dict))[i+1:]:
        # compare the hash keys to see if the images are dissimilar
        diff = hash_key - hash_key_2
        if diff >= threshold:
            # if the difference between the hashes is greater than or equal to the threshold, add the images to the dissimilar list
            dis_list.append(hash_dict[hash_key])
            dis_list.append(hash_dict[hash_key_2])

# # move all the dissimilar images to the dissimilar directory
for filepath1 in dis_list:
    try:
        shutil.move(filepath1, str(dis_dir))
    except Exception as e:
        print(e)
