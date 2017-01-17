import unittest
import numpy as np
import matplotlib as mpl
mpl.use('Agg')  # http://stackoverflow.com/questions/4931376/generating-matplotlib-graphs-without-a-running-x-server

import scipyplot as spp


class TestRplot(unittest.TestCase):

    def test_rplot_vector(self):
        y = np.random.rand(100)
        h = spp.rplot(y=y)

    def test_rplot_matrix1d(self):
        y = np.random.rand(100, 1)
        h = spp.rplot(y=y)

    def test_rplot_list1d(self):

        y = [np.random.rand(100), np.random.rand(100)]
        h = spp.rplot(y=y)

    def test_rplot_list(self):

        y = [np.random.rand(100, 1), np.random.rand(100, 1)]
        h = spp.rplot(y=y)

    def test_rplot_matrix(self):

        y = np.random.rand(100, 5)
        h = spp.rplot(y=y)


if __name__ == "__main__":
    unittest.main()
