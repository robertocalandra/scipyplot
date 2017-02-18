import unittest
import numpy as np
import matplotlib as mpl
mpl.use('Agg')  # http://stackoverflow.com/questions/4931376/generating-matplotlib-graphs-without-a-running-x-server

import scipyplot as spp


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

if __name__ == "__main__":
    unittest.main()
