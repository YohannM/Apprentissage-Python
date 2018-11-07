
import matplotlib.pyplot as mlp

from mpl_toolkits.mplot3d import Axes3D

fig = mlp.figure()
ax = fig.gca(projection='3d')

acceleration_values_x = []
acceleration_values_y = []
acceleration_values_z = []

for i in range(200):
    acceleration_values_x.append(i)
    acceleration_values_y.append(i)
    acceleration_values_z.append(i)

# Axes3D.plot_wireframe(acceleration_values_x, acceleration_values_y)

diag = mlp.plot(acceleration_values_x, acceleration_values_y, acceleration_values_z)

# surf = ax.plot_surface(acceleration_values_x, acceleration_values_y, acceleration_values_z, cmap=cm.coolwarm,
                       # linewidth=0, antialiased=False)

mlp.show()

