from __future__ import division, print_function  # absolute_import
from builtins import range

import numpy as np
import matplotlib.pyplot as plt


def plotter(index):
    x = np.linspace(0, 10, 200)
    y = np.sin(x*index)
    plt.plot(x, y)
    print('y = sin(' + str(index) + ' * x)')

import scipyplot.plot as rplot

print('To change figure use the arrows')
print('To close the figure press \'q\' ')

rplot.utils.interactivePlot(plotFunction=plotter, nplots=10, initial_idx=1)

