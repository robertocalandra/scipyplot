from __future__ import division, print_function  # absolute_import

import itertools
import matplotlib.pyplot as plt
from matplotlib import rcParams

import scipyplot.stats as rstats
import numpy as np
import scipy.stats
import seaborn.apionly as sns
from builtins import range

from scipyplot.plot.save2file import save2file

__author__ = 'Roberto Calandra'
__version__ = '0.4'


def rplot_data(data, x=None, typeplot='mean+68+95+99', legend=None, xlabel=None, ylabel=None):
    """

    :param data: list of np.matrix
    :param x: list of np.array (or single np.array) indicating the x axis of the corresponding data
    :param typeplot: String
    :return:
    """
    # TODO: implement me
    # Parse data
    out = typeplot.split("+")
    distribution = "+".join(out[1:])
    Y = []
    V = []
    X = x
    for i in range(len(data)):
        if out[0] == 'median':
            median, quantiles = rstats.median_percentile(data[i])
            Y.append(median)
            V.append(quantiles)
        if out[0] == 'mean':
            mean, variance = rstats.mean_var(data[i])
            Y.append(mean)
            V.append(variance)

    fig = rplot(y=Y, x=X, uncertainty=V, distribution=distribution, xlabel=xlabel, ylabel=ylabel, legend=legend)

    return fig


def rscatter(y, x=None, colors=None, xlabel=None, ylabel=None,
          legend=None, size='halfpage', ratio='4:3', nameFile=False, yticks=None, xticks=None):

    rcParams.update({'figure.autolayout': True})
    # plt.rc('text', usetex=True)
    # plt.rcParams['text.latex.preamble'] = [r"\usepackage{amsmath}"]
    rcParams['xtick.direction'] = 'out'
    rcParams['ytick.direction'] = 'out'

    if size is 'fullpage':
        # TODO: finetune these values
        FONTSIZEFIG = 26
        FONTSIZETICK = 22
        linewidth= 6
        markersize = 18
        legendfontsize = 20
    if size is 'halfpage':
        # TODO: finetune these values
        FONTSIZEFIG = 26
        FONTSIZETICK = 22
        linewidth = 8
        markersize = 18
        legendfontsize = 20

    fig = plt.figure(figsize=(10, 6))  # TODO: use ratio
    ax = fig.add_subplot(1, 1, 1)

    if type(y) is list:
        n_curves = len(y)
    else:
        n_curves = 1

    handle = []
    palette = itertools.cycle(sns.color_palette())
    # Plot central curves
    for i in range(n_curves):
        n_points = y[i].shape[0]
        if x is None:
            t = np.arange(n_points)
        else:
            if isinstance(x, list):
                t = x[i]
            else:
                t = x

        handle.append(plt.scatter(t, y[i], color=next(palette)))

    # Make figure nice
    if xlabel is not None:
        plt.xlabel(xlabel, fontsize=FONTSIZEFIG)
    if ylabel is not None:
        plt.ylabel(ylabel, fontsize=FONTSIZEFIG)
    if legend is not None:
        plt.legend(legend, fontsize=legendfontsize)
    if xticks is not None:
        plt.xticks(xticks, fontsize=FONTSIZETICK)
        # TODO: ax.set_xlim(xticks[0, -1])
    if yticks is not None:
        plt.yticks(yticks, fontsize=FONTSIZETICK)
        # TODO: ax.set_ylim(yticks[0, -1])

    if nameFile is not False:
        save2file(fig, nameFile)  # Save to File
    return fig


def rplot(y, uncertainty=None, x=None, colors=None, alpha=0.60, distribution='68+95+99', xlabel=None, ylabel=None,
          legend=None, size='halfpage', ratio='4:3', nameFile=False, markerspace=0.10, yticks=None, xticks=None, markerbias = 0.03):
    """

    :param y: list of np.array, each being a curve to plot
    :param uncertainty: list of np.array, each representing the distribution to plot (can be either mean/variance or median/percentiles)
    :param x: list of np.array, each being the X of the curve to plot
    :param colors:
    :param alpha: if distribution is not None, this specify the transparency of the percentiles
    :param distribution: if distribution is not None, this specify which percentile to plot
    :param xlabel: string or None
    :param ylabel: string or None
    :param legend:
    :param size: Automatically adjust size fonts based on the final size of the image ('fullpage', 'halfpage')
    :param ratio:
    :return:
    """

    rcParams.update({'figure.autolayout': True})
    # plt.rc('text', usetex=True)
    # plt.rcParams['text.latex.preamble'] = [r"\usepackage{amsmath}"]
    rcParams['xtick.direction'] = 'out'
    rcParams['ytick.direction'] = 'out'

    if size is 'fullpage':
        # TODO: finetune these values
        FONTSIZEFIG = 26
        FONTSIZETICK = 22
        linewidth= 6
        markersize = 18
        legendfontsize = 20
    if size is 'halfpage':
        # TODO: finetune these values
        FONTSIZEFIG = 26
        FONTSIZETICK = 22
        linewidth = 8
        markersize = 18
        legendfontsize = 20

    fig = plt.figure(figsize=(10, 6))  # TODO: use ratio
    ax = fig.add_subplot(1, 1, 1)
    marker = itertools.cycle(('s', 'o', 'v', '^', '*'))
    linestyle = itertools.cycle(('-', '--'))

    if type(y) is list:
        n_curves = len(y)
    else:
        n_curves = 1

    handle = []

    # Plot central curves
    for i in range(n_curves):
        n_points = y[i].shape[0]
        if x is None:
            t = np.arange(n_points)
        else:
            if isinstance(x, list):
                t = x[i]
            else:
                t = x
        # assert len(y[i]) == len(variance), 'Dimensions variance do not match dimensions y'
        assert len(y[i]) == len(t), 'Dimensions x do not match dimensions y'
        # TODO: something funny is happening with markerevery!!! non-uniform. compute sequence of points manually. markerevery = [0,1,2....]
        markerevery = (i*markerbias, markerspace)
        if (uncertainty is None) or (distribution is ''):
            # Plot only curve
            handle.append(plt.plot(t, y[i],
                                   marker=marker.next(), markersize=markersize, markevery=markerevery,
                                   linestyle='-', linewidth=linewidth))
        else:
            # Plot also distribution
            assert isinstance(uncertainty[i], np.ndarray)
            if uncertainty[i].ndim is 1:
                handle.append(gauss_1D(y=y[i], x=t, variance=uncertainty[i], alpha=alpha,
                                       marker=marker.next(), markersize=markersize, markevery=markerevery,
                                       linestyle='-', linewidth=linewidth,
                                       distribution=distribution))
            else:
                handle.append(distribution_1D(y=y[i], x=t, percentiles=uncertainty[i], alpha=alpha,
                                              marker=marker.next(), markersize=markersize, markevery=markerevery,
                                              linestyle='-', linewidth=linewidth,
                                              distribution=distribution))

    # Make figure nice
    if xlabel is not None:
        plt.xlabel(xlabel, fontsize=FONTSIZEFIG)
    if ylabel is not None:
        plt.ylabel(ylabel, fontsize=FONTSIZEFIG)
    if legend is not None:
        plt.legend(legend, fontsize=legendfontsize)
    if xticks is not None:
        plt.xticks(xticks, fontsize=FONTSIZETICK)
        # TODO: ax.set_xlim(xticks[0, -1])
    if yticks is not None:
        plt.yticks(yticks, fontsize=FONTSIZETICK)
        # TODO: ax.set_ylim(yticks[0, -1])

    if nameFile is not False:
        save2file(fig, nameFile)  # Save to File
    return fig


def distribution_1D(y, percentiles, x=None, color=None, alpha=0.60, distribution='68+95+99', linewidth=4, linestyle='-',
                    marker=None, markersize=10, markevery=0.1):
    """
    Plot a distribution
    :param y:
    :param percentiles:
    :param x:
    :param color: Color used for plotting the curve
    :param alpha: Transparency level used for plotting the distributions
    :param distribution: The percentiles of the data that are to be plotter
    :return:
    """
    n_points = len(y)
    if x is None:
        x = np.arange(n_points)
    # assert len(y) == len(variance), 'Dimensions variance do not match dimensions y'
    assert len(y) == len(x), 'Dimensions x do not match dimensions y'
    if color is None:
        handle, = plt.plot(x, y, linewidth=linewidth, linestyle=linestyle,
                           marker=marker, markersize=markersize, markevery=markevery)
    else:
        handle, = plt.plot(x, y, linewidth=linewidth, linestyle=linestyle,
                           marker=marker, markersize=markersize, markevery=markevery, color=color)
    out_des = distribution.split("+")
    # assert out > len()
    out = len(percentiles)
    sub_alpha = str(alpha / out * 2)  # Normalize w.r.t. the number of percentiles
    for i in range(0, out, 2):
        plt.fill_between(x, percentiles[i], percentiles[i+1], color=handle.get_color(), alpha=sub_alpha)
    return handle


def gauss_1D(y, variance, x=None, color=None, alpha=0.60, distribution='68+95+99', linewidth=4, linestyle='-',
             marker=None, markersize=10, markevery=0.1):
    """

    :param y: np.array of dimensions n
    :param variance: np.array of dimensions n
    :param x: np.array of dimensions n
    :param color:
    :param distribution: string composed of the percentiles to be plotted separated by a +
    :param alpha: Transparency level
    :return:
    """
    n_points = len(y)
    if x is None:
        x = np.arange(n_points)
    assert len(y) == len(variance), 'Dimensions variance do not match dimensions y'
    assert len(y) == len(x), 'Dimensions x do not match dimensions y'
    if color is None:
        handle, = plt.plot(x, y, linewidth=linewidth, linestyle=linestyle,
                           marker=marker, markersize=markersize, markevery=markevery)
    else:
        handle, = plt.plot(x, y, linewidth=linewidth, linestyle=linestyle,
                           marker=marker, markersize=markersize, markevery=markevery, color=color)
    out = distribution.split("+")
    n_percentiles = len(out)
    sub_alpha = str(alpha / n_percentiles)  # Normalize w.r.t. the number of percentiles
    for i in range(n_percentiles):
        try:
            percentile = float(out[i])
            assert 0 <= percentile <= 100, 'Percentile must be >0 <100; instead is %f' % percentile
            interval = scipy.stats.norm.interval(percentile/100, loc=y, scale=np.sqrt(variance))
            interval = np.nan_to_num(interval)  # Fix stupid case of norm.interval(0) returning nan
            plt.fill_between(x, interval[0], interval[1], color=handle.get_color(), alpha=sub_alpha)
        except ValueError:
            pass
    return handle
