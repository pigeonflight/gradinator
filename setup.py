import os
from setuptools import setup
from setuptools import find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "gradinator",
    version = "0.0.0",
    author = "David Bain",
    author_email = "pigeonflight@gmail.com",
    description = ("A automated grading system, the beginnings"),
    license = "BSD",
    keywords = "grading code",
    url = "http://packages.python.org/gradinator",
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['gradinator'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    long_description=read('README'),
    install_requires=[
        'GitPython',],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)