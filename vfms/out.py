import os
import shutil
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
from sklearn.neighbors import LocalOutlierFactor

# Set the number of clusters and the outlier detection parameters
n_clusters = 1
lof_contamination = 0.45
lof_neighbors=15

# Define a function to extract features from an image
def extract_features(image_path):
    # Load the image and resize it
    img = Image.open(image_path)
    img = img.resize((256, 256))

    # Convert the image to a numpy array
    arr = np.array(img)

    # Flatten the array to create a feature vector
    feature_vector = arr.flatten()

    return feature_vector

# Set the path to the directory containing the image folders
image_dir = 'E:/crop'

# Loop through each subdirectory and find outliers within each cluster
for subdir in os.listdir(image_dir):
    subdir_path = os.path.join(image_dir, subdir)
    if os.path.isdir(subdir_path):
        print(f"Finding outliers in {subdir}...")
        
        # Load the images and extract features
        image_paths = [os.path.join(subdir_path, f) for f in os.listdir(subdir_path)]
        features = []
        for image_path in image_paths:
            features.append(extract_features(image_path))
        X = np.array(features)

        # Cluster the images
        kmeans = KMeans(n_clusters=n_clusters)
        labels = kmeans.fit_predict(X)

        # Find outliers within each cluster
        for i in range(n_clusters):
            cluster_indices = np.where(labels == i)[0]
            cluster_features = X[cluster_indices]

            # Use Local Outlier Factor to detect outliers within the cluster
            n_neighbors = min(20, len(cluster_features) - 1)
            lof = LocalOutlierFactor(n_neighbors=lof_neighbors, contamination=lof_contamination)
            lof.fit(cluster_features)
            outlier_indices = np.where(lof.fit_predict(cluster_features) == -1)[0]
            outlier_paths = [image_paths[cluster_indices[j]] for j in outlier_indices]

            # Move the outliers to a separate folder
            if len(outlier_paths) > 0:
                outlier_dir = os.path.join(image_dir, 'outliers', subdir, f'cluster_{i}')
                os.makedirs(outlier_dir, exist_ok=True)
                for path in outlier_paths:
                    shutil.move(path, os.path.join(outlier_dir, os.path.basename(path)))
        
                    print("Done.")