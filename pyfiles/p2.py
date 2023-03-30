import os
import shutil
import numpy as np
from keras.preprocessing import image

# Define path of directory containing images
image_dir = "D:/crop/auto"

# Define path of outlier directory
outlier_dir = "D:/crop/outlier"

# Define the size of the clusters
cluster_size = 10

# Load all images from the directory
images = []
for img in os.listdir(image_dir):
    img_path = os.path.join(image_dir, img)
    img = image.load_img(img_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    images.append(img)

# Concatenate all images to form a single array
images = np.concatenate(images)

# Calculate the number of clusters
n_clusters = int(np.ceil(len(images) / cluster_size))

# Loop over each cluster
for i in range(n_clusters):
    # Determine the start and end index of the cluster
    start_idx = i * cluster_size
    end_idx = min((i + 1) * cluster_size, len(images))
    
    # Calculate the average feature vector for the cluster
    avg_feature_vector = np.mean(images[start_idx:end_idx], axis=0)
    
    # Calculate the Euclidean distance between each image and the average feature vector
    distances = np.linalg.norm(images[start_idx:end_idx] - avg_feature_vector, axis=1)
    
    # Identify the index of the dissimilar image using odd/even concept
    outlier_idx = start_idx + np.argmin(distances[::2]) * 2
    
    # Move the dissimilar image to the outlier directory
    img_path = os.path.join(image_dir, os.listdir(image_dir)[outlier_idx])
    shutil.move(img_path, outlier_dir)