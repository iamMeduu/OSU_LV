import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("data.csv", delimiter=",", skip_header=1)
height= data[:,1]
weight=data[:,2]
heightB = data[::50,1]
weightB = data[::50,2]
heightC=data[:,1]
arrE = data[data[:,0]==1]
print("Najmanja visina je: ", heightC.min(),"cm")
print("Najveca visina je: ", heightC.max(),"cm")
print("Srednja vrijednost visine je: ", heightC.mean(),"cm")
print("Najmanja visina muskaraca je: ", arrE[:,1].min(),"cm")
print("Najveca visina muskaraca je: ", arrE[:,1].max(),"cm")
print("Srednja vrijednost visine muskaraca je: ", arrE[:,1].mean(),"cm")
plt.scatter(height,weight)
plt.scatter(heightB,weightB)
plt.xlabel("Height [cm]")
plt.ylabel("Weight [kg]")
plt.title("Odnos visine i mase")
plt.show()
print(len(data))