from matplotlib import pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import cifar10
import numpy as np
import tensorflow as tf

(X_train, y_train), (X_test, y_test) = cifar10.load_data()

num_classes = 10

X_train_s = X_train.astype("float32") / 255
X_test_s = X_test.astype("float32") / 255

X_train_n = X_train_s
X_test_n = X_test_s

y_train_s = keras.utils.to_categorical(y_train, num_classes)
y_test_s = keras.utils.to_categorical(y_test, num_classes)

print(f"{X_train_n.shape} {X_test_n.shape}")

plt.figure()
for i in range(9):
    plt.subplot(330 + 1 + i)
    plt.xticks([]),plt.yticks([])
    plt.imshow(X_train[i])
plt.show()

mmodel = keras.Sequential([
    layers.Input(shape=(32, 32, 3)),

    layers.Conv2D(32, 3, padding='same', activation='relu'),
    layers.BatchNormalization(),
    layers.Conv2D(32, 3, activation='relu'),
    layers.MaxPooling2D(),
    layers.Dropout(0.25),

    layers.Conv2D(64, 3, padding='same', activation='relu'),
    layers.BatchNormalization(),
    layers.Conv2D(64, 3, activation='relu'),
    layers.MaxPooling2D(),
    layers.Dropout(0.25),

    layers.Conv2D(128, 3, activation='relu'),
    layers.GlobalAveragePooling2D(),

    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),

    layers.Dense(10, activation='softmax')
])

mmodel.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy", ])

my_callbacks = [
    keras.callbacks.EarlyStopping(monitor="val_loss", patience=12, verbose=1),
    keras.callbacks.TensorBoard(log_dir='logs/cnn_dropout', update_freq=100)
]

mmodel.fit(X_train_n, y_train_s, epochs = 50, batch_size = 32, callbacks = my_callbacks, validation_split = 0.1)