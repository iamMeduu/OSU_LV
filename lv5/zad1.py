import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                            random_state=213, n_clusters_per_class=1, class_sep=1)

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

#a)
plt.scatter(X_train[:,0], X_train[:,1], c = y_train, cmap="bwr", marker="o", label="Train")
plt.scatter(X_test[:,0],X_test[:,1], c = y_test, cmap="viridis", marker="X", label="Test")
plt.legend()
plt.show()

#b)
LogReg_model = LogisticRegression()
LogReg_model.fit(X_train, y_train)
y_test_predict = LogReg_model.predict(X_test)
#c)
#Parametars of the model
theta0 = LogReg_model.intercept_[0]  # bias
theta1 = LogReg_model.coef_[0][0]    # težina za x1
theta2 = LogReg_model.coef_[0][1]    # težina za x2
print(theta0, theta1, theta2)

x1_values = np.linspace(min(X_train[:,0]), max(X_train[:,0]), 100)
x2_values = -(theta0 + theta1 * x1_values) / theta2

plt.scatter(X_train[:,0], X_train[:,1], c = y_train, cmap="bwr", marker="o", label="Train")
plt.plot(x1_values,x2_values,'r--',linewidth=2)
plt.xlabel('X1')
plt.ylabel('X2')
plt.legend()
plt.show()

#d)
cmf_matrix = ConfusionMatrixDisplay(confusion_matrix(y_test,y_test_predict))
cmf_matrix.plot()
plt.show()
print(classification_report(y_test,y_test_predict))

#e)
positive_predicted = (y_test_predict == y_test)
negative_predicted = (y_test_predict != y_test)
print(len(positive_predicted), len(negative_predicted))
print(negative_predicted)
print(positive_predicted)
plt.scatter(X_test[positive_predicted,0], X_test[positive_predicted,1], c = "green", label = "Positive", marker="o")
plt.scatter(X_test[negative_predicted,0], X_test[negative_predicted,1], c = "black", label = "Negative", marker="x")
plt.plot(x1_values,x2_values,'r--',linewidth=2)
plt.legend()
plt.xlabel('X1')
plt.ylabel('X2')
plt.show()