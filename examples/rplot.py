
import numpy as np
from scypyplot.plot import rplot, distribution_1D, rplot_data
import matplotlib.pyplot as plt
import scipy.stats as stats


# Simple curves
x = np.linspace(0, 2, 10)
y = [np.sin(x), np.cos(x)]
# ---
fig = rplot(x=x, y=y, legend=['curve 1', 'curve 2'])
plt.show()


# Distributions
x = [np.linspace(0, 2, 10), np.linspace(0.5, 3, 10)]
y = [np.sin(x[0]), np.cos(x[1])]
var = [x[0]/20, 0.02*np.ones((x[1].shape))]
# ---
fig = rplot(x=x, y=y, uncertainty=var, legend=['curve 1', 'curve 2'])
plt.show()


# Raw data
x = []
x.append(np.random.rand(100, 30))
x.append(np.random.rand(50, 20)+2)
# ---
fig = rplot_data(data=x)
plt.show()


# Mean vs median
NUM_SAMPLES = 500000  # Number curves within each distribution (e.g., the number of repetitions of each experiment)
NUM_ITER = 10  # Number iterations
SKEW_PARAMS = [-10, 0]  # One skewed distribution and one Gaussian


def randn_skew_fast(N, alpha=0.0, mean=0.0, scale=1.0):
    sigma = alpha / np.sqrt(1.0 + alpha**2)
    u0 = np.random.randn(N)
    v = np.random.randn(N)
    u1 = (sigma*u0 + np.sqrt(1.0 - sigma**2)*v) * scale
    u1[u0 < 0] *= -1
    u1 += mean
    return u1

Y = []
X = [-3, 3]
for index, alpha_skew in enumerate(SKEW_PARAMS):
    t = []
    for i in range(NUM_ITER):
        t.append(randn_skew_fast(N=NUM_SAMPLES, alpha=alpha_skew, mean=X[index]))
    Y.append(np.array(t).transpose())

fig = rplot_data(data=Y, typeplot='mean+68+95+99', legend=['Skewed', 'Gaussian'])
ax = plt.gca()
ax.set_title('Mean + percentiles')

fig = rplot_data(data=Y, typeplot='median+68+95+99', legend=['Skewed', 'Gaussian'])
ax = plt.gca()
ax.set_title('Median + percentiles')
plt.show()
