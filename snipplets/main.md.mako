# How to create a package this code?

Make sure you have internet access, as the following commands may pull packages off the internet.

On a yum system:

    $ sudo ./build.yum.sh

On an apt system:
    
    $ sudo ./build.apt.sh

The result is in the ***dist*** folder in a file called ***pyflexebs-[VERSION]***.
This file is an executable that should run on all linux platforms.


# How to install this package as a service?

    $ sudo ./pyflexebs-[version] service_install


# How to remove this package as a service?

    $ sudo ./pyflexebs-[version] service_uninstall
