# Compatibility Python 2/3
from __future__ import division, print_function, absolute_import
from builtins import range
# ----------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
from matplotlib import rcParams


def niceFigure():
    rcParams.update({'figure.autolayout': True})
    # plt.rc('text', usetex=True)
    # plt.rcParams['text.latex.preamble'] = [r"\usepackage{amsmath}"]
    rcParams['xtick.direction'] = 'out'
    rcParams['ytick.direction'] = 'out'
