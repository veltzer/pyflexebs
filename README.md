
# *pyflexebs* project by Mark Veltzer

![PyPI - Status](https://img.shields.io/pypi/status/pyflexebs)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyflexebs)
![PyPI - License](https://img.shields.io/pypi/l/pyflexebs)
![PyPI - Package Name](https://img.shields.io/pypi/v/pyflexebs)
![PyPI - Format](https://img.shields.io/pypi/format/pyflexebs)

![PyPI - Downloads](https://img.shields.io/pypi/dd/pyflexebs)
![PyPI - Downloads](https://img.shields.io/pypi/dw/pyflexebs)
![PyPI - Downloads](https://img.shields.io/pypi/dm/pyflexebs)

![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)
![Downloads](https://pepy.tech/badge/pyflexebs)
![Downloads](https://pepy.tech/badge/pyflexebs/month)
![Downloads](https://pepy.tech/badge/pyflexebs/week)


pyflexebs will allow you to monitor and expand/contract you ebs in aws

project website: <https://veltzer.github.io/pyflexebs>

# How to build the package

    $ pip install -r requirements.txt
    $ pydmt build
    $ pypitools package

the resulting packages are in the ***dist*** folder.


# How to install the package from a pypi repository

* make sure you have ***pip3*** installed. check with your distribution about how to install it.
* run

    pip3 install pyflexebs


# How to install the package from a .whl or a .tar.gz file

* make sure you have ***pip3*** installed. check with your distribution about how to install it.
* run

    pip3 install [pyflexebs-VERSION-py3-none-any.whl]

or

    pip3 install [pyflexebs-VERSION.tar.gz]

# How to mark a machine not to be resized

Just add a "dont_resize" tag to the machine.
Pyflexebs will inquire about the machines tags and will not do resizing on that machine.

