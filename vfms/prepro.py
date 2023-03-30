import os
import cv2

# Define the folder path containing the images
folder_path = "D:/old/chennai/old/Cropped_Images1"
# folder_path = ""
print(folder_path)
# Loop through all subfolders and images in the folder
for root, dirs, files in os.walk(os.path.join(folder_path, '')):
    print("Entering folder:", root)
    print("Subfolders:", dirs)
    print("Files:", files)
    for file in files:
        # print("Processing image:", file)
        
        # Load the image using cv2
        img = cv2.imread(os.path.join(root, file))
        print('Loaded image:', os.path.join(root, file))
        print(f"Loaded image: {file}")
        # Perform preprocessing on the image (e.g., resizing, normalization, feature extraction, etc.)
        new_width = 250
        new_height = 250
        resized_img = cv2.resize(img, (new_width, new_height))

        # Save the preprocessed image to a new folder
        preprocessed_folder = "D:/old/chennai/old/Cropped_Images1/imagesc1"
        if not os.path.exists(preprocessed_folder):
                os.makedirs(preprocessed_folder)
        preprocessed_file = os.path.join(preprocessed_folder, file)
        cv2.imwrite(preprocessed_file, resized_img)

        print("Saved preprocessed file: ", preprocessed_file)
        # cv2.imwrite(os.path.join(preprocessed_folder, file), img)
