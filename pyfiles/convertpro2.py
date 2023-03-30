import cv2
import os
import numpy as np
import pickle
from sklearn.cluster import KMeans

# Define the folder path containing the preprocessed images
folder_path = "D:/old/chennai/old/Cropped_Images1/car"
print(folder_path)
# Define the number of clusters (K) to use in KMeans
K = 4

# Load all preprocessed images and convert them to feature vectors
feature_vectors = []
print(feature_vectors)
for root, dirs, files in os.walk(os.path.join(folder_path, '')):
    for file in files:
        img = cv2.imread(os.path.join(root, file))
        feature_vector = img.flatten()
        feature_vectors.append(feature_vector)
feature_vectors = np.array(feature_vectors).reshape(-1, 1)

# Apply KMeans to cluster the feature vectors
kmeans = KMeans(n_clusters=4, n_init=20)
kmeans.fit(feature_vectors)
print("Number of feature vectors:", len(feature_vectors))

with open('kmeans_model.pkl', 'wb') as f:
    pickle.dump(kmeans, f)

# Create a new folder to store the clustered images
output_folder_path = "D:/old/chennai/Cropped_Images/clus1"
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Loop through all preprocessed images and assign each to a cluster based on its feature vector
for root, dirs, files in os.walk(os.path.join(folder_path, '')):
    for file in files:
        img = cv2.imread(os.path.join(root, file))
        feature_vector = img.flatten().reshape(1, -1)
        cluster_label = kmeans.predict(feature_vector)[0]

        # Save the clustered image to a new folder
        cluster_folder_path = os.path.join(output_folder_path, f"cluster{cluster_label}")
        if not os.path.exists(cluster_folder_path):
            os.makedirs(cluster_folder_path)
        output_file_path = os.path.join(cluster_folder_path, file)
        cv2.imwrite(output_file_path, img)