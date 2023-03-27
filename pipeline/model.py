from tensorflow_loader import CreateDataset

import tensorflow as tf
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Define the model
model = tf.keras.Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 1)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(3, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# This all needs updating
data_dir = r'C:\Users\matth\OneDrive\Documents\COMM032\datasets_wav\mels'
batch_size = 1
train_skew = '50-50'
test_skew = '25-75'


# Create datasets for
train_dataset = tf.data.Dataset.from_generator(
    lambda: CreateDataset(data_dir, batch_size, train_skew),
    output_types=(tf.float32, tf.int32),
    output_shapes=((None, 128, 128, 1), (3,))
)
test_dataset = CreateDataset(data_dir, batch_size, test_skew)
#test_size = int(len(train_dataset) * 0.24)
#reduced_test_dataset = test_dataset.take(test_size)
#print(test_size)

# Train the model
#model.fit(train_dataset, epochs=10)

print(train_dataset)
#print(f'Number of examples: {len(test_dataset)}')

test_loss, test_acc = model.evaluate(test_dataset)
print(f'Test loss: {test_loss}, Test accuracy: {test_acc}')
