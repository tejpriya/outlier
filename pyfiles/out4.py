import os,cv2
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.mobilenet import preprocess_input
from tensorflow.keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D
from tensorflow.keras.models import Model
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
        img = img / 255.0  # normalize pixel values to [0, 1]
        images.append(img)
images = np.array(images)

# Define the autoencoder model architecture
input_shape = images[0].shape
encoding_dim = 64
input_img = Input(shape=input_shape)
x = Conv2D(32, (3, 3), activation='relu', padding='same')(input_img)
x = MaxPooling2D((2, 2), padding='same')(x)
x = Conv2D(64, (3, 3), activation='relu', padding='same')(x)
x = MaxPooling2D((2, 2), padding='same')(x)
x = Conv2D(128, (3, 3), activation='relu', padding='same')(x)
x = MaxPooling2D((2, 2), padding='same')(x)
x = Conv2D(encoding_dim, (3, 3), activation='relu', padding='same')(x)
encoded = MaxPooling2D((2, 2), padding='same')(x)
x = Conv2D(encoding_dim, (3, 3), activation='relu', padding='same')(encoded)
x = UpSampling2D((2, 2))(x)
x = Conv2D(128, (3, 3), activation='relu', padding='same')(x)
x = UpSampling2D((2, 2))(x)
x = Conv2D(64, (3, 3), activation='relu', padding='same')(x)
x = UpSampling2D((2, 2))(x)
x = Conv2D(32, (3, 3), activation='relu', padding='same')(x)
x = UpSampling2D((2, 2))(x)
decoded = Conv2D(input_shape[-1], (3, 3), activation='sigmoid', padding='same')(x)
autoencoder = Model(input_img, decoded)
encoder = Model(input_img, encoded)

# Compile the autoencoder model
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

# Train the autoencoder on the image data
autoencoder.fit(images, images, epochs=1, batch_size=32, shuffle=True)

# Extract features from each image using the encoder part of the auto
# Extract features from each image using the encoder part of the autoencoder
features_2d = encoder.predict(images)

# Use cosine distance and k-means clustering to identify outliers
n_samples, w, h, c = features_2d.shape
features_2d = features_2d.reshape(n_samples, w * h * c)
distances = cosine_distances(features_2d)
kmeans = KMeans(n_clusters=2).fit(features_2d)
labels = kmeans.labels_

# Identify the outliers
outlier_indices = np.where(labels == np.argmax(np.bincount(labels)))[0]
outliers = images[outlier_indices]

# Create a directory to store the outlier images and move them to that directory
outlier_dir = 'E:/crop/auto/outlier'
if not os.path.exists(outlier_dir):
    os.makedirs(outlier_dir)
for image_path in os.listdir(image_dir):
    if image_path.endswith('.jpg'):
        image_dir = os.path.join(image_dir, image_path)
        img = load_img(image_dir)
        x = img_to_array(img)
        x = x.reshape((1,) + x.shape)
        x = preprocess_input(x)
        pred = autoencoder.predict(x)
        score = np.sqrt(np.mean(np.square(pred - x)))
        if score > threshold:
            filename = os.path.basename(image_dir)
            outlier_path = os.path.join(outlier_dir, filename)
            os.rename(image_dir, outlier_path)
print(f"Identified and moved outliers to {outlier_dir}.")