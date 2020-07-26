# How to create a package this code?

First get pip3, usually with:

    $ sudo yum install python3-pip

or

    $ sudo apt install python3-pip

The run:

    $ pip3 install --user pyinstaller
    $ pyinstaller pyflexebs.spec

The result is in the ***dist*** folder in a file called ***pyflexebs-[VERSION]***.
This file is an executable that should run on all linux platforms.
