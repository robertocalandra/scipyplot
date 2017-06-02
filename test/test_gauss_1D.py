import unittest
import numpy as np
import matplotlib as mpl
mpl.use('Agg')  # http://stackoverflow.com/questions/4931376/generating-matplotlib-graphs-without-a-running-x-server

import scipyplot as spp


class TestRplot(unittest.TestCase):

    def test_gauss_1D_vector(self):
        y = np.random.rand(100)
        variance = np.random.rand(100)
        h = spp.gauss_1D(y=y, variance=variance)

    def test_gauss_1D_matrix(self):
        y = np.random.rand(100, 1)
        h = spp.gauss_1D(y=y)

    def test_gauss_1D_list1d(self):

        y = [np.random.rand(100), np.random.rand(100)]
        h = spp.gauss_1D(y=y)

    def test_gauss_1D_vector_x(self):
        y = np.random.rand(100)
        x = np.random.rand(100)
        h = spp.gauss_1D(y=y, x=x)

    def test_gauss_1D_matrix1d_x(self):
        y = np.random.rand(100, 1)
        x = np.random.rand(100, 1)
        h = spp.gauss_1D(y=y, x=x)

    # TODO: add use of variances

if __name__ == "__main__":
    unittest.main()
