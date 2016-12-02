from setuptools import setup, find_packages
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

requires = [
    'numpy >= 1.7'
    'matplotlib'
    ]

dependency_links = [
    ]


def read(fname):
    return open(os.path.join(BASE_DIR, fname)).read()

setup(name='scipyplot',
      version='0.0.1.dev0',
      description='A Python Toolbox for Creating Scientific Article Figures',
      url='https://github.com/robertocalandra/scipyplot',
      author='Roberto Calandra',
      author_email='roberto.calandra@berkeley.edu',
      keywords='visualization',
      long_description=read('README.rst'),
      license='LICENSE.txt',
      packages=find_packages(),
      install_requires=requires,
      dependency_links=dependency_links,
      zip_safe=True
      )
