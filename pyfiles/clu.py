from undouble import Undouble

# Initialize model
model = Undouble(method='phash', hash_size=8)

# Import example data
targetdir = './D:/old/chennai/crop' 
print(targetdir)
subfolders = ['Two Wheeler','car','lcv','van','multi axle','bus','other']
for subfolder in subfolders:
    subfolder_path = f"{targetdir}/{subfolder}"
    model.import_data(subfolder_path)

# Replace with path to your folder containing PNG images
#model.import_data(targetdir)

# Compute image-hash
model.compute_hash()

# Cluster similar images
model.group(threshold=2)

# Move the files to their respective clusters
model.move()

# To predict the cluster for a new image, use the predict() function
new_image_path = './D:/imagesc1'
predicted_cluster = model.predict(new_image_path)
print('Predicted cluster:', predicted_cluster)
