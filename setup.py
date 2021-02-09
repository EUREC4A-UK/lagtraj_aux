#!/usr/bin/env python
from setuptools import setup, find_packages
import versioneer

INSTALL_REQUIRES = open("requirements.txt").readlines()

setup(
    name="lagtraj_aux",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Utility for sampling auxiliary fields along trajectories",
    url="https://github.com/EUREC4A-UK/lagtraj_aux",
    maintainer="Leif Denby",
    maintainer_email="l.c.denby@leeds.ac.uk",
    py_modules=["lagtraj_aux"],
    packages=find_packages(include=["lagtraj_aux"]),
    package_data={"": ["*.csv", "*.yml", "*.html"]},
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)
