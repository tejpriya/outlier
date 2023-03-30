import pickle

# Load the variables from the file
with open('variables.pkl', 'rb') as f:
    train_dataset, val_dataset = pickle.load(f)

# Build and train the model using the loaded datasets
model.fit(train_dataset, epochs=10, validation_data=val_dataset)