import os
import shutil

# Define the function to get the label from the filename
def get_label(filename):
    label = filename.split("-")[0]
    return label

# Define the paths to the directories
grouped_images_dir = "E:/crop/auto"
target_dir = "E:/crop/outlier"

# Loop through each image in the grouped images directory
for filename in os.listdir(grouped_images_dir):
    if filename.endswith(".jpg"):
        # Get the predicted label from the filename
        predicted_label = get_label(filename)
        
        # Get the actual label from the subdirectory name
        actual_label = os.path.basename(grouped_images_dir)
        
        # If the predicted label does not match the actual label, move the image to the target directory
        if predicted_label != actual_label:
            image_path = os.path.join(grouped_images_dir, filename)
            target_path = os.path.join(target_dir, filename)
            shutil.move(image_path, target_path)
            print(f"Moved {filename} to {target_dir}")