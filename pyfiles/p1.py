import os
import shutil
from keras.preprocessing import image
from keras.applications.vgg16 import VGG16, preprocess_input

# Load pre-trained VGG16 model
model = VGG16(weights='imagenet', include_top=True)

# Path to folder containing images
folder_path = "D:/crop/auto"

# Get list of all images in folder
images = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Process each image and move outliers to separate folder
for img_path in images:
    # Load image
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = preprocess_input(x)

    # Predict class of image
    preds = model.predict(np.array([x]))
    class_index = np.argmax(preds)
    class_name = decode_predictions(preds, top=1)[0][0][1]

    # Check if image belongs to the same class as other images in folder
    in_same_class = True
    for other_path in images:
        if other_path != img_path:
            # Load other image and predict class
            other_img = image.load_img(other_path, target_size=(224, 224))
            x_other = image.img_to_array(other_img)
            x_other = preprocess_input(x_other)
            other_preds = model.predict(np.array([x_other]))
            other_class_index = np.argmax(other_preds)
            other_class_name = decode_predictions(other_preds, top=1)[0][0][1]

            # If other image belongs to a different class, set in_same_class to False
            if other_class_name != class_name:
                in_same_class = False
                break

    # If image is not in the same class as other images, move it to separate folder
    if not in_same_class:
        out_folder_path = "D:/crop/outliers"
        if not os.path.exists(out_folder_path):
            os.makedirs(out_folder_path)
        shutil.move(img_path, os.path.join(out_folder_path, os.path.basename(img_path)))