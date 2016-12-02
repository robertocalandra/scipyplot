
from __future__ import print_function
import sys
import scipyplot.log as log


def save2file(fig, nameFile, fileFormat='pdf', verbosity=1, indent=0, dpi=100):
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
        fig.savefig(fullNameFile, dpi=dpi, bbox_inches='tight')
        status = 0
    except:
        log.cnd_warning(verbosity, 1, str(sys.exc_info()[0]))
        status = -1
    log.cnd_status(verbosity, 0, status)
