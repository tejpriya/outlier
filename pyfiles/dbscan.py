import cv2
import os
import numpy as np
import pickle
from sklearn.cluster import KMeans,DBSCAN

# Define the folder path containing the preprocessed images
folder_path = "E:/Cropped_Images"
print(folder_path)
# Define the number of clusters (K) to use in KMeans
K = 15

# Load all preprocessed images and convert them to feature vectors
feature_vectors = []
for root, dirs, files in os.walk(os.path.join(folder_path, '')):
    for file in files:
        img = cv2.imread(os.path.join(root, file))
        feature_vector = img.flatten()
        feature_vectors.append(feature_vector)
feature_vectors = np.array(feature_vectors)[:1000]

# Use DBSCAN to identify outlier points and remove them from the dataset
dbscan = DBSCAN(eps=50, min_samples=2)
dbscan_labels = dbscan.fit_predict(feature_vectors)
keep_indices = np.where(dbscan_labels != -1)[0]
feature_vectors = feature_vectors[keep_indices]

# Apply KMeans to cluster the remaining feature vectors
kmeans = KMeans(n_clusters=15, n_init=20)
kmeans.fit(feature_vectors)

# Save the KMeans model to disk
with open('kmeans_model.pkl', 'wb') as f:
    pickle.dump(kmeans, f)

# Create a new folder to store the clustered images
output_folder_path = "D:/imagesc1"
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Loop through all preprocessed images and assign each to a cluster based on its feature vector
for root, dirs, files in os.walk(os.path.join(folder_path, '')):
    for file in files:
        img = cv2.imread(os.path.join(root, file))
        feature_vector = img.flatten()

        # Ignore outlier points identified by DBSCAN
        if feature_vector.shape[0] != feature_vectors.shape[1]:
            continue

        # Assign each point to a cluster based on its feature vector
        cluster_label = kmeans.predict([feature_vector])[0]

        # Save the clustered image to a new folder
        cluster_folder_path = os.path.join(output_folder_path, f"cluster{cluster_label}")
        if not os.path.exists(cluster_folder_path):
            os.makedirs(cluster_folder_path)
        output_file_path = os.path.join(cluster_folder_path, file)
        cv2.imwrite(output_file_path, img)
        
        
        
        
        
        
        
        
        
#         feature_vector = feature_vector[:10000] # limit feature vector length to 10000
#         feature_vectors.append(feature_vector)

# # Reshape feature vectors to have same length
# max_len = max(len(v) for v in feature_vectors)
# for i in range(len(feature_vectors)):
#     feature_vectors[i] = np.pad(feature_vectors[i], (0, max_len - len(feature_vectors[i])), mode='constant')

# feature_vectors = np.array(feature_vectors)




# # Apply KMeans to cluster the feature vectors
# kmeans = KMeans(n_clusters=5, n_init=20)
# kmeans.fit(feature_vectors)
# print("Number of feature vectors:", len(feature_vectors))

# # Save the KMeans model to a file
# with open('kmeans_model.pkl', 'wb') as f:
#     pickle.dump(kmeans, f)

# # Create a new folder to store the clustered images
# output_folder_path = "D:/imagesc1"
# if not os.path.exists(output_folder_path):
#     os.makedirs(output_folder_path)

# # Loop through all preprocessed images and assign each to a cluster based on its feature vector
# for root, dirs, files in os.walk(os.path.join(folder_path, '')):
#     for file in files:
#         img = cv2.imread(os.path.join(root, file))
#         feature_vector = img.flatten()
#         feature_vector = feature_vector[:10000] # limit feature vector length to 10000
#         # Reshape feature vector to have same length as other feature vectors
#         feature_vector = np.pad(feature_vector, (0, max_len - len(feature_vector)), mode='constant')
#         cluster_label = kmeans.predict([feature_vector])[0]

#         # Save the clustered image to a new folder
#         cluster_folder_path = os.path.join(output_folder_path, f"cluster{cluster_label}")
#         if not os.path.exists(cluster_folder_path):
#             os.makedirs(cluster_folder_path)
#         output_file_path = os.path.join(cluster_folder_path, file)
#         cv2.imwrite(output_file_path, img)
