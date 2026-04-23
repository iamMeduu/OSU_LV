import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
import matplotlib.image as Image
from keras.models import load_model

model = load_model('zadatak_1_model.keras')

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)

x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

x_train_s = np.expand_dims(x_train_s, -1)
x_test_s = np.expand_dims(x_test_s, -1)

predictions = model.predict(x_test_s)
prediction_labels = np.argmax(predictions, axis=1)
wrong_labels = np.where(prediction_labels != y_test)[0]

fig, axes = plt.subplots(4, 4, figsize=(10, 10))

for i, ax in enumerate(axes.flat):
    index = wrong_labels[i]

    ax.imshow(x_test[index], cmap="gray")
    ax.set_title(
        f"True: {y_test[index]}\nPred: {prediction_labels[index]}",
        fontsize=10
    )
    ax.axis("off")

plt.tight_layout()
plt.subplots_adjust(wspace=0.3, hspace=0.5)
plt.suptitle("Misclassified Digits", fontsize=16)
plt.show()

print('===============')
print(f"Wrong labels: {wrong_labels.shape[0]} / {prediction_labels.shape[0]}")
print(f"Accuracy: {(prediction_labels.shape[0] - wrong_labels.shape[0]) / prediction_labels.shape[0]}")
print('===============')