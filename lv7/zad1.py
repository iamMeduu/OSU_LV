from turtledemo.chaos import plot

import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import dendrogram
from sklearn.datasets import make_blobs, make_circles, make_moons
from sklearn.cluster import KMeans, AgglomerativeClustering


def generate_data(n_samples, flagc):
    # 3 grupe
    if flagc == 1:
        random_state = 365
        X,y = make_blobs(n_samples=n_samples, random_state=random_state)
    
    # 3 grupe
    elif flagc == 2:
        random_state = 148
        X,y = make_blobs(n_samples=n_samples, random_state=random_state)
        transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
        X = np.dot(X, transformation)

    # 4 grupe 
    elif flagc == 3:
        random_state = 148
        X, y = make_blobs(n_samples=n_samples,
                        centers = 4,
                        cluster_std=np.array([1.0, 2.5, 0.5, 3.0]),
                        random_state=random_state)
    # 2 grupe
    elif flagc == 4:
        X, y = make_circles(n_samples=n_samples, factor=.5, noise=.05)
    
    # 2 grupe  
    elif flagc == 5:
        X, y = make_moons(n_samples=n_samples, noise=.05)
    
    else:
        X = []
        
    return X

# generiranje podatkovnih primjera
# prikazi primjere u obliku dijagrama rasprsenja



# init – initialisation of  centara
# ’k-means++’, ’random’, default=’k-means++’


#a)
def do_tasks(n_samples, flagc, k=3):
    X = generate_data(n_samples, flagc)

    km = KMeans(n_clusters= k, init="random", n_init=6,
                random_state=0)

    km.fit(X)

    plt.figure()
    plt.scatter(X[:, 0], X[:, 1], c = km.labels_)
    plt.xlabel('$x_1$')
    plt.ylabel('$x_2$')
    plt.title('podatkovni primjeri')
    plt.show()

X = generate_data(500,1)

plt.figure()
plt.scatter(X[:,0],X[:,1])
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title('podatkovni primjeri')
plt.show()

do_tasks(500,1, 11)
do_tasks(500,2, 3)
do_tasks(500,3, 5)
do_tasks(500,4, 7)
do_tasks(500,5, 4)