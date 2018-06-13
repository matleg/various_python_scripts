from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')
# ax=fig.gca(projection="3d")

x = [0, 1, 1, 0]
y = [0, 1, 0, 1]
z = [1, 1, 1, 1]

# ax.plot_wireframe(x, y, z)
# ax.plot_surface(x, y, z, rstride=1, cstride=1, color='b')
ax.plot(x, y, z, 'bo')

plt.show()
