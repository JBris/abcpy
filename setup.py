# Always prefer setuptools over distutils
import sys
from setuptools import setup, find_packages
from os import path

try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements
    
try: # for pip >= 19.3
    from pip._internal.network.session import PipSession
except ImportError:
    try: # for pip < 19.3 and >=10
        from pip._internal.download import PipSession
    except ImportError: # for pip <= 9.0.3
        from pip.download import PipSession

here = path.abspath(path.dirname(__file__))

install_reqs_raw = parse_requirements('requirements.txt', session=PipSession())

try:
    install_reqs = [str(ir.req) for ir in install_reqs_raw]
except AttributeError:
    install_reqs = [str(ir.requirement) for ir in install_reqs_raw]

with open(path.join(here, 'VERSION')) as f:
    version = f.readline().strip()
    file_tgz = 'v' + version + '.tar.gz'

setup(
    name='abcpy',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=version,

    description='A framework for approximate Bayesian computation (ABC) that speeds up inference by parallelizing computation on single computers or whole clusters.',
    long_description='ABCpy is a highly modular, scientific library for approximate Bayesian computation (ABC) written in Python. It is designed to run all included ABC algorithms in parallel, either using multiple cores of a single computer or using an Apache Spark or MPI enabled cluster. The modularity helps domain scientists to easily apply ABC to their research without being ABC experts; using ABCpy they can easily run large parallel simulations without much knowledge about parallelization, even without much additional effort to parallelize their code. Further, ABCpy enables ABC experts to easily develop new inference schemes and evaluate them in a standardized environment, and to extend the library with new algorithms. These benefits come mainly from the modularity of ABCpy.',

    # The project's main homepage.
    url='https://github.com/eth-cscs/abcpy',
    download_url = 'https://github.com/eth-cscs/abcpy/archive/' + file_tgz,

    # Author details
    author='The abcpy authors',
    author_email='',

    # Choose your license
    license='BSD-3',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    # What does your project relate to?
    keywords='abcpy',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    # install_requires=['numpy', 'scipy'],
    install_requires=install_reqs,


    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    #extras_require={
    #    'dev': ['check-manifest'],
    #    'test': ['coverage'],
    #},

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    # package_data={
    #     'sample': ['package_data.dat'],
    # },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    #data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    #entry_points={
    #    'console_scripts': [
    #        'sample=sample:main',
    #    ],
    #},
)
