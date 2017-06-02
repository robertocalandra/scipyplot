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


if __name__ == "__main__":
    unittest.main()
