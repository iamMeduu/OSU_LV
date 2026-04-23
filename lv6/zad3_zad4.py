import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC


def plot_decision_regions(X, y, classifier, resolution=0.02):
    plt.figure()
    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    # plot class examples
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0],
                    y=X[y == cl, 1],
                    alpha=0.8,
                    c=colors[idx],
                    marker=markers[idx],
                    label=cl)


# ucitaj podatke
data = pd.read_csv("Social_Network_Ads.csv")
print(data.info())

data.hist()
plt.show()

# dataframe u numpy
X = data[["Age", "EstimatedSalary"]].to_numpy()
y = data["Purchased"].to_numpy()

# podijeli podatke u omjeru 80-20%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=10)

# skaliraj ulazne velicine
sc = StandardScaler()
X_train_n = sc.fit_transform(X_train)
X_test_n = sc.transform((X_test))

# Model logisticke regresije
LogReg_model = LogisticRegression(penalty=None)
LogReg_model.fit(X_train_n, y_train)

# Evaluacija modela logisticke regresije
y_train_p = LogReg_model.predict(X_train_n)
y_test_p = LogReg_model.predict(X_test_n)

print("Logisticka regresija: ")
print("Tocnost train: " + "{:0.3f}".format((accuracy_score(y_train, y_train_p))))
print("Tocnost test: " + "{:0.3f}".format((accuracy_score(y_test, y_test_p))))

# granica odluke pomocu logisticke regresije
plot_decision_regions(X_train_n, y_train, classifier=LogReg_model)
plt.xlabel('x_1')
plt.ylabel('x_2')
plt.legend(loc='upper left')
plt.title("Tocnost: " + "{:0.3f}".format((accuracy_score(y_train, y_train_p))))
plt.tight_layout()
plt.show()

def do_svm(c,gama,kernel):
    svm_model = svm.SVC(kernel = kernel, C=c, gamma=gama)
    svm_model.fit(X_train_n, y_train)

    y_test_p_svm = svm_model.predict(X_test_n)
    y_train_p_svm = svm_model.predict(X_train_n)

    print(f"SVM: C = {c}, gamma = {gama}")
    print(f"Accuracy train SVM: {accuracy_score(y_train, y_train_p_svm)}")
    print(f"Accuracy test SVM: {accuracy_score(y_test, y_test_p_svm)}")

    plot_decision_regions(X_train_n, y_train, classifier=svm_model)
    plt.xlabel('x_1')
    plt.ylabel('x_2')
    plt.legend(loc='upper left')
    plt.title(f"SWM accuracy = {accuracy_score(y_train, y_train_p_svm).__round__(3)}, C = {c}, gamma = {gama}")
    plt.tight_layout()
    plt.show()

#kernels: rbf,linear,sigmoid
#gamma - curvature of the decision region
do_svm(1,0.01,"rbf")
do_svm(1,0.1, "rbf")
do_svm(2,1.0, "rbf")
do_svm(0.1,1, "rbf")
do_svm(1.0,1, "rbf")
do_svm(10,1, "rbf")

# do_svm(1,0.01,"sigmoid")
# do_svm(1,0.1, "sigmoid")
# do_svm(2,1.0, "sigmoid")
# do_svm(0.1,1, "sigmoid")
# do_svm(1.0,1, "sigmoid")
# do_svm(10,1, "sigmoid")

# do_svm(1,0.01,"linear")
# do_svm(1,0.1, "linear")
# do_svm(2,1.0, "linear")
# do_svm(0.1,1, "linear")
# do_svm(1.0,1, "linear")
# do_svm(10,1, "linear")

#Zad_6.5.4
param_grid = {
    'svc__C': [0.1, 1, 10, 100, 1000],
    'svc__gamma': [0.01, 0.1, 1, 10, 100]
}

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('svc', SVC(kernel='rbf', C=1.0))
])

grid_svm = GridSearchCV(pipe, param_grid=param_grid, scoring='accuracy', n_jobs=-1)
grid_svm.fit(X_train_n, y_train)

print("Best C:", grid_svm.best_params_['svc__C'])
print("Best gamma:", grid_svm.best_params_['svc__gamma'])
print("Best CV accuracy:", grid_svm.best_score_)

do_svm(
    grid_svm.best_params_["svc__C"],
    grid_svm.best_params_["svc__gamma"],
    "rbf"
)

#overfitting - dobar training, a los test
# underfitting - los na treningu



