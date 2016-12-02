from __future__ import division, print_function  # absolute_import
from builtins import range

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import matplotlib.cm as cm
from matplotlib import rcParams
import itertools
import scipy.stats
import seaborn.apionly as sns
from scipyplot.plot.utils.niceFigure import niceFigure


def trajectory(x, y, z=None, interpolate=None, mark_init=True, mark_end=True,
               force_color_init=None, force_color_end=None, cmap=cm.coolwarm, linewidth=2):
    """
    Wrapper for color_over_time
    :param x:
    :param y:
    :param z:
    :param interpolate:
    :param mark_init:
    :param mark_end:
    :param force_color_init:
    :param force_color_end:
    :param cmap:
    :return:
    """
    color_over_time(x=x, y=y, z=z, interpolate=interpolate, mark_init=mark_init, mark_end=mark_end,
                    force_color_init=force_color_init, force_color_end=force_color_end, cmap=cmap)


def color_over_trajectories(x, y, c=None, mark_init=True, mark_end=True, cmap=cm.coolwarm, linewidth=2):

    # Determine number of curves
    # niceFigure()
    x = np.squeeze(x)
    y = np.squeeze(y)
    if type(x).__module__ == np.__name__:
        if x.ndim is 1:
            n_x_curves = 1
        else:
            n_x_curves = x.shape[0]
    if isinstance(x, list):
        n_x_curves = len(x)  # already a list
    if type(y).__module__ == np.__name__:
        if y.ndim is 1:
            n_y_curves = 1
        else:
            n_y_curves = y.shape[0]
    if isinstance(y, list):
        n_y_curves = len(y)  # already a list

    assert (n_y_curves == n_x_curves) or (n_x_curves == 1) or (n_y_curves == 1)
    n_curves = max(n_x_curves, n_y_curves)
    assert (n_curves >= 1)

    # Convert everything to list (if not already)
    if type(x).__module__ == np.__name__:
        if x.ndim is 1:
            x = [x] * n_curves  # Single trajectory
        else:
            list(x)  # Multiple trajectories, decompose into a list
    if type(y).__module__ == np.__name__:
        if y.ndim is 1:
            y = [y] * n_curves  # Single trajectory
        else:
            list(y)  # Multiple trajectories, decompose into a list

    if c is None:
        c = np.linspace(0, 1, n_curves)  # your "time" variable
    else:
        # TODO: Normalize c to 0-1
        pass
    colors = cmap(c)

    niceFigure()
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(1, 1, 1)
    for i in range(n_curves):
        plt.plot(x[i], y[i], color=colors[i], linewidth=linewidth)

        if mark_init:
            plt.plot(x[i][0], y[i][0], 'o', color=colors[i])
        if mark_end:
            plt.plot(x[i][-1], y[i][-1], 'o', color=colors[i])

    return fig


def color_over_time(x, y, z=None, interpolate=None, mark_init=True, mark_end=True,
                    force_color_init=None, force_color_end=None, cmap=cm.coolwarm, linewidth=2):
    """

    :param x:
    :param y:
    :param z:
    :param interpolate: None => Automatic, otherwise set the number of points used for interpolation
    :param mark_init:
    :param mark_end:
    :param force_color_init:
    :param force_color_end:
    :param cmap:
    :return:
    """

    # TODO: use z
    # niceFigure()

    # Inspired by http://stackoverflow.com/questions/13622909/matplotlib-how-to-colorize-a-large-number-of-line-segments-as-independent-gradi/13649811#13649811
    def reshuffle(x, y):
        """Reshape the line represented by "x" and "y" into an array of individual
        segments."""
        points = np.vstack([x, y]).T.reshape(-1, 1, 2)
        points = np.concatenate([points[:-1], points[1:]], axis=1)
        return points

    def interp(data, num=2000):
        """Add "num" additional points to "data" at evenly spaced intervals and
        separate into individual segments."""
        x, y = data.T
        dist = np.hypot(np.diff(x - x.min()), np.diff(y - y.min())).cumsum()
        t = np.r_[0, dist] / dist.max()
        ti = np.linspace(0, 1, num, endpoint=True)
        xi = np.interp(ti, t, x)
        yi = np.interp(ti, t, y)

        # Insert the original vertices
        indices = np.searchsorted(ti, t)
        xi = np.insert(xi, indices, x)
        yi = np.insert(yi, indices, y)
        ti = np.insert(ti, indices, t)

        return reshuffle(xi, yi), ti

    # Determine number of curves
    # x = np.squeeze(x)
    # y = np.squeeze(y)
    if type(x).__module__ == np.__name__:
        if x.ndim is 1:
            n_x_curves = 1
        else:
            n_x_curves = x.shape[0]
    if isinstance(x, list):
        n_x_curves = len(x)  # already a list
    if type(y).__module__ == np.__name__:
        if y.ndim is 1:
            n_y_curves = 1
        else:
            n_y_curves = y.shape[0]
    if isinstance(y, list):
        n_y_curves = len(y)  # already a list

    assert (n_y_curves == n_x_curves) or (n_x_curves == 1) or (n_y_curves == 1)
    n_curves = max(n_x_curves, n_y_curves)
    assert (n_curves >= 1)

    # Convert everything to list (if not already)
    if type(x).__module__ == np.__name__:
        if x.ndim is 1:
            x = [x] * n_curves  # Single trajectory
        else:
            list(x)  # Multiple trajectories, decompose into a list
    if type(y).__module__ == np.__name__:
        if y.ndim is 1:
            y = [y] * n_curves  # Single trajectory
        else:
            list(y)  # Multiple trajectories, decompose into a list

    # colors = []
    niceFigure()
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(1, 1, 1)
    for i in range(n_curves):
        # num_points = x[i].shape[0]
        # colors = np.linspace(0, 1, num_points)

        # Add "num" additional segments to the line
        x[i] = np.expand_dims(x[i], axis=1)
        y[i] = np.expand_dims(y[i], axis=1)
        line = np.concatenate((x[i], y[i]), axis=1)
        # TODO: dynamic number of interpolation points
        segments, color_scalar = interp(line, num=200)
        coll = LineCollection(segments, cmap=cmap, linewidths=linewidth)
        coll.set_array(color_scalar)
        ax = plt.gca()
        ax.add_collection(coll)

        if mark_init:
            if force_color_init is None:
                color = cmap(0)
            else:
                color = force_color_init
            plt.plot(x[i][0], y[i][0], 'o', color=color)
        if mark_end:
            if force_color_end is None:
                color = cmap(255)
            else:
                color = force_color_end
            plt.plot(x[i][-1], y[i][-1], 'o', color=color)

    return fig

