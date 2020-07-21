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


# How to get all prerequisite packages for this package from pypi.org?

Just run

    $ pypitools prerequisites
