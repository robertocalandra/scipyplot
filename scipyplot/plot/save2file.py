# Compatibility Python 2/3
from __future__ import division, print_function, absolute_import
from builtins import range
# ----------------------------------------------------------------------------------------------------------------------

import sys
import scipyplot.log as log
import matplotlib.pyplot as plt


def save2file(nameFile, fig=plt.gcf(), fileFormat='pdf', verbosity=1, indent=0, dpi=100):
    """

    :param fig:
    :param nameFile:
    :param fileFormat:
    :param verbosity:
    :param indent:
    :param dpi:
    :return:
    """
    fullNameFile = nameFile + '.' + fileFormat
    log.cnd_msg(verbosity, 0, 'Saving to file: ' + fullNameFile, indent_depth=indent)
    try:
        fig.savefig(fullNameFile, dpi=dpi, bbox_inches='tight', pad_inches=0)
        status = 0
    except:
        log.cnd_warning(verbosity, 1, str(sys.exc_info()[0]))
        status = -1
    log.cnd_status(verbosity, 0, status)
