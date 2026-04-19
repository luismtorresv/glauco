import os
from runpy import run_path

from setuptools import find_packages, setup

# read the program version from version.py (without loading the module)
__version__ = run_path('src/glauco/version.py')['__version__']


def read(fname):
    """Utility function to read the README file."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="glauco",
    version=__version__,
    author="Luis M. Torres-Villegas",
    author_email="lmtorresv@eafit.edu.co",
    description="Complementary web app for the Riasco-Goyes 2025 preprint.",
    license="proprietary",
    url="",
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={'glauco': ['res/*']},
    long_description=read('README.md'),
    install_requires=[],
    tests_require=[
        'pytest',
        'pytest-cov',
        'pre-commit',
    ],
    platforms='any',
    python_requires='>=3.10',
)
