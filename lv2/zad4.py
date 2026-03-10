import numpy as np
import matplotlib.pyplot as plt
"""
x=[]
y=[]

for i in range(0,50):
    for j in range(100,50,-1):
        x.append(i)
        y.append(j)
for i in range(50,100):
    for j in range(0,50):
        x.append(i)
        y.append(j)


plt . plot (x , y, "black", linewidth =5, markersize = 1)
plt.axis([0.0 ,100 , 0.0 , 100 ])
plt.show()
"""
black = np.zeros((50, 50))
white = np.ones((50, 50))
upper_half = np.hstack((black, white))
lower_half = np.hstack((white, black))

img = np.vstack((upper_half, lower_half))
plt.axis([0.0 ,100, 100, 0 ] )
plt.imshow(img, cmap='gray')
plt.show()