import re
try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension


kwds = {}
try:
    kwds['long_description'] = open('README.rst').read()
except IOError:
    pass

# Read version from bsdiff/__init__.py
pat = re.compile(r'__version__\s*=\s*(\S+)', re.M)
data = open('bsdiff4f/__init__.py').read()
kwds['version'] = eval(pat.search(data).group(1))

setup(
    name = "bsdiff4f",
    author = "Ilan Schnell",
    author_email = "ilanschnell@gmail.com",
    url = "https://github.com/ilanschnell/bsdiff4",
    license = "BSD",
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: C",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Utilities",
    ],
    description = "binary diff and patch using the BSDIFF4-format",
    packages = ["bsdiff4f"],
    ext_modules = [Extension(name = "bsdiff4f.core",
                             sources = ["bsdiff4f/core.c", "bsdiff4f/sais.c"])],
    entry_points = {
        'console_scripts': [
            'bsdiff4f = bsdiff4f.cli:main_bsdiff4',
            'bspatch4f = bsdiff4f.cli:main_bspatch4',
        ],
    },
    **kwds
)
