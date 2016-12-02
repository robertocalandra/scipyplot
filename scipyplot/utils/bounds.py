import numpy as np


class bounds(object):

    def __init__(self, min, max):
        self.min = np.array(min)
        self.max = np.array(max)
        # self.n_dim =
        # assert

    def get_min(self):
        return self.min

    def get_max(self):
        return self.max

    def get_both(self):
        return np.vstack([self.get_min(), self.get_max()])

    def get_list(self):  # Legacy purpose
        return [self.get_min(), self.get_max()]
