import os
from PIL import Image
import numpy as np

# set the directory paths for car images and wrongly classified images
car_dir = "D:/old/chennai/Cropped_Images/Car"
non_car_dir = "D:/old/chennai/Cropped_Images/Non_Car"

# set the threshold value for image similarity
threshold = 5

# create a dictionary to store image hashes and paths
hash_dict = {}

# create a list to store the dissimilar images
dis_list = []

# load the images and their labels
X = []
y = []
for filename in os.listdir(car_dir):
    filepath = os.path.join(car_dir, filename)
    label = "Car"
    with Image.open(filepath) as img:
        # resize the image to a fixed size
        img = img.resize((64, 64))
        # convert the image to grayscale
        img = img.convert("L")
        # convert the image to a numpy array
        img_arr = np.array(img)
        # flatten the image into a 1D array
        img_arr_flat = img_arr.reshape(-1)
        # add the image and label to the X and y lists
        X.append(img_arr_flat)
        y.append(label)

for filename in os.listdir(non_car_dir):
    filepath = os.path.join(non_car_dir, filename)
    label = "Non_Car"
    with Image.open(filepath) as img:
        # resize the image to a fixed size
        img = img.resize((64, 64))
        # convert the image to grayscale
        img = img.convert("L")
        # convert the image to a numpy array
        img_arr = np.array(img)
        # flatten the image into a 1D array
        img_arr_flat = img_arr.reshape(-1)
        # add the image and label to the X and y lists
        X.append(img_arr_flat)
        y.append(label)
