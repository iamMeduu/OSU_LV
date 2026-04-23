import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from PIL import Image
from keras.models import load_model

model = keras.models.load_model('zadatak_1_model.keras')

def do_prediction(path):
    image = Image.open(path).convert("L")  # grayscale
    image = image.resize((28, 28))

    image_array = np.asarray(image)

    image_array = 255 - image_array

    image_array = image_array.astype('float32') / 255

    # shape: (28, 28) → (1, 28, 28, 1)
    image_array = np.expand_dims(image_array, axis=0)
    image_array = np.expand_dims(image_array, axis=-1)

    prediction = model.predict(image_array, verbose=0)
    predicted_label = np.argmax(prediction)

    plt.imshow(image_array[0])
    plt.show()

    return predicted_label

accurate = 0

for i in range(10):
    print("===================")
    print(f"Testing on number {i}")
    prediction = do_prediction(f"test/test_{i}.png")

    print(f"Prediction: {prediction}")
    print(f"Good prediction {prediction == i}")
    if prediction == i:
        accurate += 1
    print("===================")


print("===================")
print(f"Accurate: {accurate/10}")
print("===================")
