import matplotlib.pyplot as plt

"""It's just a plot displayer """


def display(coordinates):
    print(f"displaying : {coordinates.tolist()}")
    x = coordinates[:, 0]
    y = coordinates[:, 1]
    z = coordinates[:, 2]

    ax = plt.axes(projection='3d')
    ax.plot3D(x, y, z, 'gray')
    ax.scatter(x, y, z, c=z)
    plt.show()
