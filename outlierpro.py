import shutil,sys
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
from sklearn.neighbors import LocalOutlierFactor
def extract_features(image_path):
   
    img = Image.open(image_path)
    img = img.resize((256, 256))
    arr = np.array(img)
    feature_vector = arr.flatten()
    return feature_vector

    
  
def clust1(request):
  if request.method == 'POST':
        form = dupl(request.POST)
        if form.is_valid():
        # Get the directory path from the form data
         image_dir = form.cleaned_data['image_dir']
         print("image_dir",image_dir)
        # Set the number of clusters and the outlier detection parameters
        n_clusters = 1
        lof_contamination = 0.1

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
                    lof = LocalOutlierFactor(contamination=lof_contamination)
                    lof.fit(cluster_features)
                    outlier_indices = np.where(lof.fit_predict(cluster_features) == -1)[0]
                    outlier_paths = [image_paths[cluster_indices[j]] for j in outlier_indices]

                    # Move the outliers to a separate folder
                    if len(outlier_paths) > 0:
                        outlier_dir = os.path.join(image_dir, 'outliers', subdir, f'cluster_{i}')
                        os.makedirs(outlier_dir, exist_ok=True)
                        for path in outlier_paths:
                            shutil.move(path, os.path.join(outlier_dir, os.path.basename(path)))
                        
           form.save()
        return HttpResponse(f'<div style="background-color:#4CAF22;color:white;padding:20px;border-radius:5px;text-align:center;font-size:20px;font-weight:bold;">Outliers moved successfully</div>') 
        
  else:
    form = dupl()
    
  context = {'form': form}
  
  return render(request, 'templates/clust1.html',context)

