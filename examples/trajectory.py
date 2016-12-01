from __future__ import division, print_function  # absolute_import

import matplotlib.pyplot as plt

import numpy as np
from builtins import range

from code.plot import color_over_time, color_over_trajectories, save2file

# Generate some data
n_curves = 10
x = np.linspace(0, 1, 100)
y = [np.sin(x+i*0.02) for i in range(n_curves)]
t = np.linspace(0, 1, n_curves)

# Plot trajectories where the color change across time
fig = color_over_time(x=x, y=y)
save2file(fig, 'trajectory1', fileFormat='png')
plt.show()

# Plot trajectories where the color change across the trajectories
fig = color_over_trajectories(x=x, y=y)
save2file(fig, 'trajectory2', fileFormat='png')
# ax = plt.gca()
# print(ax)
# print(fig)
# fig.colorbar(ax)
plt.show()


