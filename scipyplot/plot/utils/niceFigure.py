

def niceFigure(useLatex=True):
    from matplotlib import rcParams
    import matplotlib.pyplot as plt
    # rcParams.update({'figure.autolayout': True})
    if useLatex is True:
        plt.rc('text', usetex=True)
        plt.rcParams['text.latex.preamble'] = [r"\usepackage{amsmath}"]
    rcParams['xtick.direction'] = 'out'
    rcParams['ytick.direction'] = 'out'
    rcParams['xtick.major.width'] = 1
    rcParams['ytick.major.width'] = 1
    #
    # cbar.outline.set_edgecolor('black')
    # cbar.outline.set_linewidth(1)
    #
    return 0