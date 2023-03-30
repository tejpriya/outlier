import cv2
import os
import numpy as np
import pickle

# Define the folder path containing the preprocessed images
folder_path = "D:/old/chennai/imagesc"

# Define the number of clusters (K) to use in KMeans
K = 12

# Load the KMeans model from file

# Define the output folder path for the clustered images
output_folder_path = "D:/old/chennai/images_clustered"
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Loop through all preprocessed images and assign each to a cluster based on its feature vector
for root, dirs, files in os.walk(os.path.join(folder_path, '')):
    for file in files:
        img = cv2.imread(os.path.join(root, file))
        if img is None:
            print(f"Skipping invalid image: {os.path.join(root, file)}")
            continue
        feature_vector = img.flatten()
        cluster_label = kmeans.predict([feature_vector])[0]
        if cluster_label < 0 or cluster_label >= K:
            print(f"Invalid cluster label {cluster_label} for image {os.path.join(root, file)}")
            continue
        cluster_folder_path = os.path.join(output_folder_path, f"cluster{cluster_label}")
        if not os.path.exists(cluster_folder_path):
            os.makedirs(cluster_folder_path)
        output_file_path = os.path.join(cluster_folder_path, file)
        cv2.imwrite(output_file_path, img)
