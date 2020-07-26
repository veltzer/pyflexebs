# How to create a package this code?

Make sure you have internet access, as the following commands may pull packages off the internet.

Install git

On a yum system:

    $ sudo yum install git

On an apt system:

    $ sudo apt install git

Clone the repository:

    $ git clone https://github.com/veltzer/pyflexebs

CD into the repository:

    $ cd pyflexebs

Build the executable

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

<%include file="../snipplets/reduce.md.mako" />
