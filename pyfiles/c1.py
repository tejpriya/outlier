import cv2
import os
import numpy as np
from sklearn.cluster import KMeans

# Define the folder path containing the preprocessed images
folder_path = "D:/old/chennai/Cropped_Images"

# Define the number of clusters (K) to use in KMeans
K = 12

# Load all preprocessed images and convert them to feature vectors
feature_vectors = []
class_names = []
for class_name in os.listdir(folder_path):
    class_path = os.path.join(folder_path, class_name)
    if os.path.isdir(class_path):
        for file_name in os.listdir(class_path):
            file_path = os.path.join(class_path, file_name)
            img = cv2.imread(file_path)
            feature_vector = img.flatten()
            print(feature_vector.shape)
            feature_vectors.append(feature_vector)
            class_names.append(class_name)

feature_vectors = np.array(feature_vectors)

# Apply KMeans to cluster the feature vectors
kmeans = KMeans(n_clusters=K, n_init=10, random_state=42)
kmeans.fit(feature_vectors)

# Create a new folder to store the clustered images
output_folder_path = "D:/old/chennai/images_clustered2"
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Loop through all preprocessed images and assign each to a cluster based on its feature vector
for i, class_name in enumerate(class_names):
    feature_vector = feature_vectors[i]
    cluster_label = kmeans.predict([feature_vector])[0]

    # Save the clustered image to a new folder based on the class name
    output_class_path = os.path.join(output_folder_path, class_name)
    if not os.path.exists(output_class_path):
        os.makedirs(output_class_path)
    output_file_path = os.path.join(output_class_path, f"cluster{cluster_label}.jpg")
    img = cv2.imread(os.path.join(folder_path, class_name, f"{i}.jpg"))
    cv2.imwrite(output_file_path, img)
