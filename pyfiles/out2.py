import os
import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.applications.vgg16 import VGG16, preprocess_input
from sklearn.metrics.pairwise import cosine_distances
from sklearn.cluster import KMeans
from alibi_detect.od import OutlierAE
import shutil

# Load the cropped images into memory
image_dir = 'E:/crop/auto'
images = []
for filename in os.listdir(image_dir):
    if filename.endswith('.jpg'):
        img = load_img(os.path.join(image_dir, filename), target_size=(224, 224))
        img = img_to_array(img)
        img = preprocess_input(img)
        images.append(img)
images = np.array(images)

# Extract features from each image using VGG16
base_model = VGG16(weights='imagenet', include_top=False)
features = base_model.predict(images)

# Compute pairwise similarity scores between the feature vectors
distances = cosine_distances(features)

# Cluster the images based on their pairwise similarity scores
kmeans = KMeans(n_clusters=2, random_state=42)
labels = kmeans.fit_predict(distances)

# Identify the cluster(s) containing the dissimilar images as outliers
ae = OutlierAE(threshold=0.1)
outlier_scores = ae.predict(images, outlier_type='instance', return_feature_score=True)
outlier_mask = outlier_scores['data']['is_outlier']

# Move the dissimilar images to a separate folder
outlier_dir = 'E:/crop/auto/outlier'
if not os.path.exists(outlier_dir):
    os.makedirs(outlier_dir)
for i, filename in enumerate(os.listdir(image_dir)):
    if filename.endswith('.jpg') and outlier_mask[i]:
        shutil.move(os.path.join(image_dir, filename), os.path.join(outlier_dir, filename))