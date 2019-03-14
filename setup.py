#!/usr/bin/env python3
"""
The setup script used to package the se library and executables.

To build the project, enter the project's root directory and do:
python3 setup.py bdist_wheel

After the project has been built, you can install it locally:
pip3 install dist/standardebooks-*.whl

To upload the build to pypi, twine is required:
pip3 install twine
"""

from os import path
from setuptools import setup, find_packages
import se

# Get the long description from the README file
def _get_file_contents(filename):
    """
    Helper function to get README contents
    """

    with open(filename, encoding="utf-8") as file:
        return file.read()

setup(
    name="standardebooks",
    version=se.VERSION,
    description="The toolset used to produce Standard Ebooks epub ebooks.",
    long_description=_get_file_contents(path.join(path.abspath(path.dirname(__file__)), "README.md")),
    long_description_content_type="text/markdown",
    url="https://standardebooks.org",
    author="Standard Ebooks",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5"
    ],
    keywords="ebooks epub",
    packages=find_packages(),
    python_requires=">=3.5", # The latest version installed by default on Ubuntu 16.04 is 3.5.2
    install_requires=[
        "beautifulsoup4==4.6.0", # Good
        "cssselect==1.0.1", # Good
        "ftfy==5.3.0", # Good
        "gitpython==2.1.5", # Good
        "lxml==4.2.3", # Good
        "psutil==5.5.0", # Good
        "pyhyphen==3.0.1", # Good
        # "pyopenssl>=19.0.0",  # Required to allows the `requests` package to use https on Mac OSX, but segfaults when installed on Ubuntu
        "python-magic==0.4.13", # Good
        "regex==2017.7.26", # Good
        "requests>=2.20.0", # Good
        "roman==2.0.0", # Good
        "smartypants==2.0.0", # Good
        "titlecase==0.11.0", # Good
        "termcolor==1.1.0", # Good
        "terminaltables==3.1.0" # Good
    ],
    package_data={
        "se": ["data/*", "data/templates/*", "data/templates/META-INF/*", "completions/*", "completions/*/*"]
    },
    entry_points={
        "console_scripts": [
            "se = se.executables:main",
        ],
    },
    project_urls={
        "Source": "https://github.com/standardebooks/tools/",
    }
)
