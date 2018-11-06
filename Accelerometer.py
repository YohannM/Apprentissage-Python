from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED, DIRECTION_MIDDLE
from mpl_toolkits.mplot3d import Axes3D
from time import sleep

import matplotlib.pyplot as plt
import time


if __name__ == "__main__":
    
    sense = SenseHat()
    
    while True:
        event = sense.stick.wait_for_event()

        if event.action == ACTION_PRESSED && event.direction == DIRECTION_MIDDLE:

            while event.action == ACTION_HELD:

                acceleration_values_x = []
                acceleration_values_y = []
                acceleration_values_z = []

                velocity_values_x = []
                velocity_values_y = []
                velocity_values_z = []

                position_values_x = []
                position_values_y = []
                position_values_z = []

                acceleration = sense.get_accelerometer_raw()
                
                x = acceleration['x']
                y = acceleration['y']
                z = acceleration['z']

                acceleration_values_x.append(x)
                acceleration_values_y.append(y)
                acceleration_values_z.append(z)

            for i in range(len(acceleration_values_x - 2)):
                velocity_values_x.append((acceleration_values_x[i] + acceleration_values_x[i+1])/2)
                velocity_values_y.append((acceleration_values_y[i] + acceleration_values_y[i+1])/2)
                velocity_values_z.append((acceleration_values_z[i] + acceleration_values_z[i+1])/2)

            for i in range(len(velocity_values_x - 2)):
                position_values_x.append((velocity_values_x[i] + velocity_values_x[i+1])/2)
                position_values_y.append((velocity_values_y[i] + velocity_values_y[i+1])/2)
                position_values_z.append((velocity_values_z[i] + velocity_values_z[i+1])/2)

            diag = mlp.plot(position_values_x, position_values_y, position_values_z)

            mlp.show()

    # surf = ax.plot_surface(acceleration_values_x, acceleration_values_y, acceleration_values_z, cmap=cm.coolwarm,
                       # linewidth=0, antialiased=False)
    
    # mp.pyplot.plot(acceleration_values_x, acceleration_values_y, acceleration_values_z)

    # Axes3D.plot_wireframe(acceleration_values_x, acceleration_values_y, acceleration_values_z, *args, **kwargs)