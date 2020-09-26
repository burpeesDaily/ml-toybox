"""Setup file for ml-toybox."""

import pathlib
import setuptools

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.rst").read_text()

# This call to setup() does all the work
setuptools.setup(
    name="ml-toybox",
    version="0.0.1",
    description="Machine Learning ToyBox",
    long_description=README,
    long_description_content_type="text/x-rst",
    url="https://github.com/shunsvineyard/ml-toybox",
    author="Shun Huang",
    author_email="shunsvineyard@protonmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8"
    ],
    keywords="Machine Learning",
    packages=setuptools.find_packages(exclude=["examples", "tests"]),
    python_requires=">=3.8"
)
