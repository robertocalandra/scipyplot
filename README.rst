

SciPyPlot
=========
A Python Toolbox for Creating Scientific Article's Figures

This package offer tools for creating high-quality figures aimed at scientific publications.
Currently most of the functions are aimed at plotting curves (e.g., optimization curves).

If you simply have a matrix of data that you want to use, the main function to use is `rplot_data`.
If you already have processed the data and want to plot a curve (and optionally var/std) you can use `rplot`.

To have more details about the features available on the package have a look at examples.

For simple usage we reccomend to install the master branch.

Master Branch
-------------

.. image:: https://travis-ci.org/robertocalandra/scipyplot.svg?branch=master
    :target: https://travis-ci.org/robertocalandra/scipyplot

.. image:: https://coveralls.io/repos/github/robertocalandra/scipyplot/badge.svg?branch=master
    :target: https://coveralls.io/github/robertocalandra/scipyplot?branch=master

.. image:: https://landscape.io/github/robertocalandra/scipyplot/master/landscape.svg?style=flat
    :target: https://landscape.io/github/robertocalandra/scipyplot/master
    :alt: Code Health

.. image:: https://badge.fury.io/py/scipyplot.svg
    :target: https://badge.fury.io/py/scipyplot


============
Installation
============
To install the last stable build we recommend to use::

   pip install scipyplot

Development Branch
------------------

.. image:: https://travis-ci.org/robertocalandra/scipyplot.svg?branch=development
    :target: https://travis-ci.org/robertocalandra/scipyplot

.. image:: https://coveralls.io/repos/github/robertocalandra/scipyplot/badge.svg?branch=development
    :target: https://coveralls.io/github/robertocalandra/scipyplot?branch=development

.. image:: https://landscape.io/github/robertocalandra/scipyplot/development/landscape.svg?style=flat
    :target: https://landscape.io/github/robertocalandra/scipyplot/development
    :alt: Code Health

This branch is experimental and its use is not reccomended unless you know what you are doing.

============
Installation
============
To install the development branch you will have to clone the repository and manually install the package.
You can do that using::

	git clone https://github.com/robertocalandra/scipyplot.git --branch development
	cd scipyplot
	python setup.py install
	
