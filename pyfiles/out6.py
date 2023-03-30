import os
import cv2
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Define the number of clusters for K-Means
num_clusters = 2

# Define the path to the directory containing the images
path = 'E:/crop/auto'

# Define the function to preprocess the images
def preprocess_image(image_path):
    # Load the image and resize it to a fixed size
    image = cv2.imread(image_path)
    
    # Convert the image to a NumPy array and normalize the pixel values
    image = np.array(image, dtype=np.float32)
    image /= 255.
    # Reshape the image to a single row of pixels
    image = image.reshape((1, -1))
    return image

# Load all the images in the directory and preprocess them
images = []
for filename in os.listdir(path):
    image_path = os.path.join(path, filename)
    image = preprocess_image(image_path)
    images.append(image)

# Stack all the images into a single NumPy array
images = np.vstack(images)

# Perform PCA on the images to reduce their dimensionality
pca = PCA(n_components=35)
images_pca = pca.fit_transform(images)

# Cluster the images using K-Means
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(images_pca)

# Get the index of the cluster with the smallest centroid distance
distances = kmeans.transform(images_pca)
min_distances = np.min(distances, axis=1)
outlier_index = np.argmax(min_distances)

# Get the filename of the outlier image
outlier_filename = os.listdir(path)[outlier_index]

print('The outlier image is:', outlier_filename)
