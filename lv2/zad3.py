import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("road.jpg")
img = img[:,:,0].copy()

img_light = np.clip(img + 50, 0, 255)

h, w = img_light.shape
second_quarter = img[:, w//4 : w//2]

img_rot = np.rot90(img, -1)
img_mirror = np.fliplr(img)

fig, ax = plt.subplots(2, 3, figsize=(10,6))

ax[0,0].imshow(img, cmap="gray")
ax[0,0].set_title("Original")

ax[0,1].imshow(img_light, cmap="gray")
ax[0,1].set_title("Posvijetljena")

ax[0,2].imshow(second_quarter, cmap="gray")
ax[0,2].set_title("Druga četvrtina")

ax[1,0].imshow(img_rot, cmap="gray")
ax[1,0].set_title("Rotirana")

ax[1,1].imshow(img_mirror, cmap="gray")
ax[1,1].set_title("Zrcaljena")



plt.show()