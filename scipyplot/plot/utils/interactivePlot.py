from __future__ import division, print_function, absolute_import
from builtins import range, input

import matplotlib.pyplot as plt
from ..save2file import save2file


def interactivePlot(plotFunction, nplots, initial_idx=0):
    """

    :param plotFunction: pointer to the function that render the figures. the function should be in the form
        plotFunction(idx) with 0<idx<nplots
    :param nplots: scalar. number of plots over which to iterate.
    :param initial_idx: index of the plot used to initialize the visualization.
    :return:
    """

    # Inspired by http://stackoverflow.com/questions/18390461/scroll-backwards-and-forwards-through-matplotlib-plots
    global curr_idx
    curr_idx = initial_idx

    def key_event(e):
        global curr_idx

        if (e.key == "right") or (e.key == "up"): # Next plot
            curr_idx += 1
        elif (e.key == "left") or (e.key == "down"):  # Previous plot
            curr_idx -= 1
        elif (e.key == "p"):  # Save to file
            key = input("Insert name file to save: [default: figure].pdf") or 'figure'
            save2file(fig=fig, nameFile=key, fileFormat='pdf')
        elif (e.key == "q"):  # Quit
            plt.close()
            return
        else:
            return
        curr_idx = curr_idx % nplots
        ax.cla()
        plotFunction(curr_idx)
        fig.canvas.draw()

    fig = plt.figure()
    fig.canvas.mpl_connect('key_press_event', key_event)
    ax = fig.add_subplot(111)
    plotFunction(curr_idx)
    plt.show()
