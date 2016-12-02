
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def training_process_3d(data, fontsizefig=18):
    """

    :param data: List of arrays, each containing a "loss trajectory" as a numpy array [3 x T]
    (Note: The loss trajectories can have different lenght)
    :return:
    """
    n_traj = len(data)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(n_traj):
        assert data[i].shape[0] == 3
        #ax.plot(data[i][0, :], data[i][1, :], data[i][2, :], c='r', marker='-o')
        ax.plot(data[i][0, :], data[i][1, :], data[i][2, :])

    ax.set_xlabel('Training set', fontsize=fontsizefig)
    ax.set_ylabel('Test set', fontsize=fontsizefig)
    ax.set_zlabel('Validation set', fontsize=fontsizefig)
    #plt.xscale('log')
    #plt.yscale('log')
    #plt.zscale('log')
    plt.show()

    return 0


def training_process_2d(data):
    """

    :param data: "loss trajectory" as a numpy array [3 x T]
    :return:
    """
    assert data.shape[0] == 3
    n_traj = len(data)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    h = ax.plot(data.transpose())
    plt.yscale('log')
    ax.legend(h, ['Training set', 'Test set', 'Validation set'])
    plt.show()
    return 0