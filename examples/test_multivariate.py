from __future__ import division, print_function  # absolute_import
from builtins import range

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import itertools
import scipy.stats
import R.stats as rstats
from R.plot.gauss_1D import gauss_1D

y = np.random.normal(0, 1, 100000) #[np.sin(x), np.sin(x+0.5), np.sin(x+0.1)]

# def randn_skew_fast(N, alpha=0.0, mean=0.0, scale=1.0):
#     sigma = alpha / np.sqrt(1.0 + alpha**2)
#     u0 = np.random.randn(N)
#     v = np.random.randn(N)
#     u1 = (sigma*u0 + np.sqrt(1.0 - sigma**2)*v) * scale
#     u1[u0 < 0] *= -1
#     u1 += mean
#     return u1


distribution = '68+95+99'

print(y.shape)

mean, variance = rstats.mean_var(y)
print(mean, np.sqrt(variance))
median, percentile = rstats.median_percentile(y, distribution)
print(median, percentile)
mean2, percentile2 = rstats.mean_percentile(y, distribution)
print(mean2, percentile2)


print('-------')
print(median)
print(mean)
print(mean2)
print('-------')
print(rstats.distribution.percentileFromGaussian(mean=mean, variance=variance, percentile=68))
print(np.percentile(y, 68, axis=0))
print('-------')
print(percentile)
print(percentile2)

# out = distribution.split("+")
# n_percentiles = len(out)
# for i in range(n_percentiles):
#     percentile = float(out[i])
#     interval = scipy.stats.norm.interval(percentile / 100, loc=y, scale=np.sqrt(variance))


fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)
plt.plot(x=x, y=y)


# -------------------------------------------
x = np.linspace(0, 1, 100)
y = np.random.normal(0, 1, (5000, 100)) #[np.sin(x), np.sin(x+0.5), np.sin(x+0.1)]
m, v = rstats.mean_var(y)

fig = plt.figure(figsize=(10, 6))  # TODO: use ratio
ax = fig.add_subplot(1, 1, 1)

gauss_1D(m, variance=v, x=x, distribution='68+95+99')

handle = plt.plot(x, m, color='green')

std = np.sqrt(v)
handle = plt.plot(x, m+std, color='orange', linestyle=':')
handle = plt.plot(x, m-std, color='orange', linestyle=':')
handle = plt.plot(x, m+2*std, color='yellow', linestyle=':')
handle = plt.plot(x, m-2*std, color='yellow', linestyle=':')


n_v1 = scipy.stats.norm.interval(0.68, loc=m, scale=std)
n_v5 = scipy.stats.norm.interval(0.954, loc=m, scale=std)
n_v2 = scipy.stats.norm(loc=m, scale=std).ppf(1-0.682)
n_v3 = scipy.stats.norm(loc=m, scale=std).ppf(0.954)
n_v4 = scipy.stats.norm(loc=m, scale=std).ppf(1-0.954)
plt.plot(x, n_v1[0], color='red', linestyle='--', marker='^')
plt.plot(x, n_v1[1], color='red', linestyle='--', marker='^')
plt.plot(x, n_v5[0], color='purple', linestyle='--', marker='^')
plt.plot(x, n_v5[1], color='purple', linestyle='--', marker='^')

plt.show()
