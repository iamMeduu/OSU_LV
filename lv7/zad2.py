import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as Image
from sklearn.cluster import KMeans

for i in range(1,7):
    img = Image.imread("imgs/test_" + str(i) + ".jpg")

    # pretvori vrijednosti elemenata slike u raspon 0 do 1
    img = img.astype(np.float64) / 255

    # transformiraj sliku u 2D numpy polje
    w, h, d = img.shape
    img_array = np.reshape(img, (w * h, d))

    # KMeans
    k = 5
    km = KMeans(n_clusters=k, init="k-means++", n_init=5, random_state=0)
    labels = km.fit_predict(img_array)
    centers = km.cluster_centers_


    # rekonstrukcija slike
    img_array_aprox = centers[labels]
    img_array_aprox = np.reshape(img_array_aprox, (w, h, d))

    # prikaz original + aproksimacija
    f, axarr = plt.subplots(1, 2)
    axarr[0].imshow(img)
    axarr[0].set_title("Original")
    axarr[1].imshow(img_array_aprox)
    axarr[1].set_title("After clustering")
    plt.tight_layout()
    plt.show()

    # BINARNE SLIKE PO KLASTERIMA
    labels_2D = labels.reshape(w, h)

    fig, axes = plt.subplots(1, k, figsize=(15, 3))
    print(np.unique(labels_2D))
    for j in range(k):
        binary_img = (labels_2D == j)

        axes[j].imshow(binary_img, cmap='viridis')
        axes[j].set_title(f"G{j}")
        axes[j].axis('off')

    plt.suptitle(f"Binarne slike - slika {i}")
    plt.tight_layout()
    plt.show()


    # ELBOW METODA
    J = []
    K_range = range(1, 11)

    for kk in K_range:
        km = KMeans(n_clusters=kk, init="k-means++", random_state=0)
        km.fit(img_array)
        J.append(km.inertia_)

    plt.plot(K_range, J, marker="o")
    plt.xlabel("K")
    plt.ylabel("Inertia (J)")
    plt.title(f"Elbow metoda - slika {i}")
    plt.grid()
    plt.show()