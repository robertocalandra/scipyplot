import numpy as np
import scipy.stats

__author__ = 'Roberto Calandra'
__version__ = '0.4'


def mean_var(data):
    # TODO: assert is a np.array
    mean = np.nanmean(data, axis=0)
    var = np.nanvar(data, axis=0)
    return [mean, var]


def mean_std(data):
    # TODO: assert is a np.array
    mean = np.nanmean(data, axis=0)
    std = np.nanstd(data, axis=0)
    return [mean, std]


def mean_percentile(data, des_percentiles='68+95+99'):
    """

    :param data:
    :param des_percentiles:
    :return:
    """
    mean, variance = mean_var(data=data)
    out = np.array(map(int, des_percentiles.split("+")))
    for i in range(out.size):
        assert 0 <= out[i] <= 100, 'Percentile must be >0 <100; instead is %f' % out[i]
    percentiles = percentileFromGaussian(mean=mean, variance=variance, percentile=out)
    return [mean, percentiles]


def median_percentile(data, des_percentiles='68+95+99'):
    """

    :param data:
    :param des_percentiles: string with +separated values of the percentiles
    :return:
    """
    median = np.nanmedian(data, axis=0)
    out = np.array(map(int, des_percentiles.split("+")))
    for i in range(out.size):
        assert 0 <= out[i] <= 100, 'Percentile must be >0 <100; instead is %f' % out[i]
    list_percentiles = np.empty((2*out.size,), dtype=out.dtype)
    list_percentiles[0::2] = out        # Compute the percentile
    list_percentiles[1::2] = 100 - out  # Compute also the mirror percentile
    percentiles = np.nanpercentile(data, list_percentiles, axis=0)
    return [median, percentiles]


def percentileFromGaussian(mean, variance, percentile='68+95+99'):
    """

    :param mean:
    :param variance:
    :param percentile:
    :return:
    """
    # assert 0 <= percentile <= 100, 'Percentile must be >0 <100; instead is %f' % percentile  # TODO: assert for both numpy.array and single numbers
    a = np.array([0.68, 0.95, 0.99])
    std = np.sqrt(variance)
    out = scipy.stats.norm.interval(a, loc=mean, scale=std)
    out = np.ravel(np.column_stack((out[1], out[0])))
    return np.nan_to_num(out)
