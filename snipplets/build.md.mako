# How to create a package this code?

First get pip3, usually with:

    $ sudo yum install python3-pip

or

    $ sudo apt install python3-pip

Also install python development tools

    $ sudo yum install python3-devel gcc

or

    $ sudo apt install python3-dev

Install all run time dependencies:

    $ pip3 install --user .

Install pyinstaller:
    
    $ pip3 install --user pyinstaller

Run the pyinstaller:

    $ pyinstaller pyflexebs.spec

The result is in the ***dist*** folder in a file called ***pyflexebs-[VERSION]***.
This file is an executable that should run on all linux platforms.
