import inline as inline
import matplotlib
from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt

coordinates = [[0, 0, 0], [1, 0, 0], [2, 0, 0],
               [2, 1, 0],
               [3, 1, 0], [3, 2, 0], [3, 3, 0],
               [4, 3, 0], [4, 4, 0], [4, 5, 0],
               [3, 5, 0],
               [3, 6, 0], [2, 6, 0], [1, 6, 0],
               [1, 7, 0],
               [1, 8, 0], [2, 8, 0],
               [2, 9, 0],
               [3, 9, 0], [3, 10, 0], [3, 11, 0],
               [2, 11, 0],
               [1, 11, 0], [1, 12, 0], [1, 13, 0],
               [0, 13, 0], [-1, 13, 0]
               ]
coo = np.asarray(coordinates)
x = coo[:, 0]
y = coo[:, 1]
z = coo[:, 2]

ax = plt.axes(projection='3d')
ax.plot3D(x, y, z, 'gray')
ax.scatter(x, y, z, c=z)
plt.show()
"""plt.rcParams["figure.figsize"] = [5.50, 3.0]
plt.rcParams["figure.autolayout"] = True

# fig = plt.figure()
# ax = plt.axes(projection='3d')

ax = plt.axes(projection='3d')

# Data for a three-dimensional line
zline = np.linspace(0, 15, 1000)
# print(zline)
xline = np.sin(zline)
# print(xline)
yline = np.cos(zline)
# print(yline)
ax.plot3D(xline, yline, zline, 'gray')

# Data for three-dimensional scattered points
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
# print(f"zdata[0]: {zdata[0]}\nydata[0]: {ydata[0]}\nxdata[0]: {xdata[0]}")
ax.scatter(xdata, ydata, zdata, c=zdata, cmap='Greens')

plt.show()"""
"""plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
data = np.random.random(size=(3, 3, 3))
print(data)
z, x, y = data.nonzero()
ax.scatter(x, y, z, c=z, alpha=1)
plt.show()"""
