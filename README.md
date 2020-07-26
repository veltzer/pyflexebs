
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

# How to create a package this code?

Make sure you have internet access, as the following commands may pull packages off the internet.

On a yum system:

    $ ./build.yum.sh

On an apt system:
    
    $ ./build.apt.sh

The result is in the ***dist*** folder in a file called ***pyflexebs-[VERSION]***.
This file is an executable that should run on all linux platforms.


# How to install this package as a service?

    $ sudo ./pyflexebs-[version] service_install


# How to remove this package as a service?

    $ sudo ./pyflexebs-[version] service_uninstall

