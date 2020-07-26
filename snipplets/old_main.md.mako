# How to build the package

    $ python3 setup.py sdist bdist_wheel

This will create both a source and binary package in the ***dist*** folder.
***sdist*** will create the source package.
***bdist_wheel*** will create the binary package.
If you do not need both forms of the package you can choose to create just the one you want.

# How to install the package from a pypi repository

* make sure you have ***pip3*** installed. check with your distribution about how to install it.
* run

    $ pip3 install pyflexebs


# How to install the package from a .whl or a .tar.gz file

* make sure you have ***pip3*** installed. check with your distribution about how to install it.
* run

    $ pip3 install [pyflexebs-VERSION.tar.gz]

or

    $ pip3 install [pyflexebs-VERSION-py3-none-any.whl]


# How to mark a machine not to be resized

Just add a "dont_resize" tag to the machine.
Pyflexebs will inquire about the machines tags and will not do resizing on that machine.


# How to get all prerequisite packages for this package from pypi.org?

Just run

    $ pip3 install pypitools
    $ pypitools prerequisites_run

This will package production only prerequisites into a folder named ***wheel***.


# How to create a single file distribution from this package?

Just run

    $ pip3 install pyinstaller
    $ pyinstaller pyflexebs.spec

The result is in the ***dist*** folder in a file called ***pyflexebs-[VERSION]***.
This file is an executable that should run on all linux platforms.
