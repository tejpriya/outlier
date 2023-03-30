import os
import shutil

# define a dictionary to hold the image paths, grouped by labels
grouped_images = {}
def get_actual_label(filename):
    return filename.split('_')[0]
# recursively search for image files in the "auto" folder and group them by their labels
for root, dirs, files in os.walk('D:/crop/auto'):
    for file in files:
        if file.endswith('.jpg'):  # adjust this to match your file extension
            label = get_actual_label(file)
            if label not in grouped_images:
                grouped_images[label] = []
            grouped_images[label].append(os.path.join(root, file))

# create a directory for misclassified images
misclassified_dir = 'misclassified'
if not os.path.exists(misclassified_dir):
    os.makedirs(misclassified_dir)

# iterate through the grouped images
for label, images in grouped_images.items():
    for image_path in images:
        # check if the image is misclassified
        actual_label = get_actual_label(image_path)
        if label != actual_label:
            # move the misclassified image to the misclassified directory
            image_name = os.path.basename(image_path)
            new_image_path = os.path.join(misclassified_dir, "auto", image_name)
            os.makedirs(os.path.dirname(new_image_path), exist_ok=True)
            shutil.move(image_path, new_image_path)
