from tensorflow.keras.preprocessing.image import ImageDataGenerator
import pickle
import h5py

# Define the paths to the training and validation data folders
train_data_path = "D:/old/chennai/dataset/test"
val_data_path = "D:/old/chennai/dataset/val"


train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

val_datagen = ImageDataGenerator(rescale=1./255)

# Define the ImageDataGenerator for data augmentation and preprocessing


# Load the training and validation datasets using the ImageDataGenerator
train_dataset = train_datagen.flow_from_directory(
    train_data_path,
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)

val_dataset = val_datagen.flow_from_directory(
    val_data_path,
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)
train_dataset.save('train_dataset.h5')
val_dataset.save('val_dataset.h5')

