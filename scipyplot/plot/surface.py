# Compatibility Python 2/3
from __future__ import division, print_function, absolute_import
from builtins import range
# ----------------------------------------------------------------------------------------------------------------------

import numpy as np
from dotmap import DotMap
import matplotlib.pyplot as plt
from matplotlib import cm


def surface_bounds(f, bounds, cmap=cm.magma_r, resolution=[100, 100], type='2D'):
    """
    Plot a function over a grid
    :param f: function to plot in Z
    :param bounds:
    :param cmap: cmap
    :param resolution:
    :param type: '2D' or '3D'
    :return:
    """
    resolution = np.array(resolution)
    assert bounds.get_n_dim() == 2, 'Bounds are not 2D'

    x = np.linspace(start=bounds.get_min(0), stop=bounds.get_max(0), num=resolution[0])
    y = np.linspace(start=bounds.get_min(1), stop=bounds.get_max(1), num=resolution[1])
    X, Y = np.meshgrid(x, y)
    Z = f(np.vstack((X.flatten(), Y.flatten())).T).reshape(X.shape)  # Evaluate grid on the function
    surface(X=X, Y=Y, Z=Z, type=type, cmap=cmap)


# def surface_grid(f, x, y)


def surface(X, Y, Z, type='2D', cmap=cm.magma_r):
    """
    Plot a surface either in 2D or 3D
    :param X:
    :param Y:
    :param Z:
    :param type:
    :param cmap: colormap
    :return:
    """
    if type == '2D':
        h = plt.imshow(Z, origin="lower", extent=[X.min(), X.max(), Y.min(), Y.max()], cmap=cmap)
        # TODO: tight axis
        # TODO: nicefigure

    if type == '3D':
        # surf = ax.plot_surface(xx, yy, Y_plot.reshape(100, 100), cmap=colormap)
        pass

    return h