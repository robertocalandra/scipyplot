import unittest
import numpy as np
import matplotlib as mpl
mpl.use('Agg')  # http://stackoverflow.com/questions/4931376/generating-matplotlib-graphs-without-a-running-x-server

import scipyplot as spp
import matplotlib.pyplot as plt


class TestRplot(unittest.TestCase):

    def test_rplot_data_1(self):
        y = [np.random.rand(100, 100)]
        h = spp.rplot_data(data=y)

    def test_rplot_data_2(self):
        y = [np.random.rand(100, 100)]
        x = [np.random.rand(100)]
        h = spp.rplot_data(data=y)

    def test_rplot_data_3(self):
        y = [np.random.rand(100, 100)]
        x = np.random.rand(100)
        h = spp.rplot_data(data=y)

    def test_rplot_data_yscale(self):
        y = [np.absolute(np.random.rand(100, 100)) + 0.00001]
        x = np.random.rand(100)
        h = spp.rplot_data(data=y)
        plt.yscale('log')

    def test_rplot_data_matrix(self):
        y = np.random.rand(100, 100)
        h = spp.rplot_data(data=y)

if __name__ == "__main__":
    unittest.main()
