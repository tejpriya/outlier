import cv2
import os
import numpy as np
import pickle
from sklearn.cluster import KMeans

# Define the folder path containing the input images
input_folder_path = "D:/imagesc1"

# Define the number of clusters (K) to use in KMeans
K = 7

# Load all input images and convert them to feature vectors
feature_vectors = []
for root, dirs, files in os.walk(input_folder_path):
    for file in files:
        img = cv2.imread(os.path.join(root, file))
        feature_vector = img.flatten()
        feature_vectors.append(feature_vector)
feature_vectors = np.array(feature_vectors)

# Apply KMeans to cluster the feature vectors
kmeans = KMeans(n_clusters=7, n_init=20)
kmeans.fit(feature_vectors)
print("Number of feature vectors:", len(feature_vectors))

# Save the trained KMeans model
with open('kmeans_model.pkl', 'wb') as f:
    pickle.dump(kmeans, f)
